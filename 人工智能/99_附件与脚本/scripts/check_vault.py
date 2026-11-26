"""
Obsidian 知识库健康度自动校验脚本
功能：
1. 检查全库 Markdown 文件的 UTF-8 编码与 YAML Frontmatter 完整性
2. 检查双向链接 [[...]] 是否能解析到真实存在的笔记或目录
3. 检查图片相对路径 ![...](...) 是否指向真实存在的文件
4. 检查 Mermaid 代码块是否成对闭合
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]


def collect_vault_files():
    md_files = []
    all_note_stems = set()
    all_rel_paths = set()
    for path in VAULT_ROOT.rglob("*"):
        if ".obsidian" in path.parts or ".git" in path.parts:
            continue
        rel = path.relative_to(VAULT_ROOT).as_posix()
        all_rel_paths.add(rel)
        if path.is_file() and path.suffix.lower() == ".md":
            md_files.append(path)
            all_note_stems.add(path.stem)
    return md_files, all_note_stems, all_rel_paths


def check_file(md_path: Path, all_note_stems: set[str], all_rel_paths: set[str]):
    issues = []
    try:
        text = md_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["非 UTF-8 编码文件"]

    # 1. 检查 Frontmatter（模板文件除外）
    if "templates" not in md_path.parts:
        if not text.startswith("---\n"):
            issues.append("缺少 YAML Frontmatter 开头 `---`")
        elif text.count("\n---\n") < 1:
            issues.append("YAML Frontmatter 未正常闭合")

    # 2. 检查代码块闭合（含 Mermaid）
    fence_count = len(re.findall(r"(?m)^```", text))
    if fence_count % 2 != 0:
        issues.append(f"代码块围栏 ``` 数量为奇数 ({fence_count})，存在未闭合块")

    # 3. 检查图片相对路径 ![alt](path)（忽略代码块、行内代码以及模板/规范示例）
    stripped_code = re.sub(r"```[\s\S]*?```", "", text)
    stripped_inline = re.sub(r"`[^`]+`", "", stripped_code)
    if "templates" not in md_path.parts and md_path.name != "NOTE_STANDARD.md":
        for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", stripped_inline):
            img_ref = m.group(1).strip()
            if img_ref.startswith(("http://", "https://")):
                continue
            resolved = (md_path.parent / img_ref).resolve()
            if not resolved.exists():
                issues.append(f"图片路径不存在: {img_ref}")

    # 4. 检查双向链接 [[target|alias]]（报告尚未创建的章节占位链接作为提示，不混同严重错误）
    missing_links = []
    for m in re.finditer(r"\[\[([^\]]+)\]\]", stripped_code):
        raw = m.group(1).split("|")[0].split("#")[0].strip()
        if not raw:
            continue
        # 支持文件夹链接或文件名链接
        if raw.endswith("/"):
            if not (VAULT_ROOT / raw.rstrip("/")).exists():
                missing_links.append(raw)
        elif raw not in all_note_stems and f"{raw}.md" not in all_rel_paths:
            missing_links.append(raw)

    return issues, missing_links


def main():
    md_files, all_note_stems, all_rel_paths = collect_vault_files()
    print(f"扫描知识库: {VAULT_ROOT}")
    print(f"Markdown 文件总数: {len(md_files)}\n")

    error_count = 0
    pending_target_count = 0
    for md_path in sorted(md_files):
        rel = md_path.relative_to(VAULT_ROOT).as_posix()
        res = check_file(md_path, all_note_stems, all_rel_paths)
        if isinstance(res, list):
            issues, missing = res, []
        else:
            issues, missing = res

        if issues:
            error_count += len(issues)
            print(f"[格式/路径错误] {rel}:")
            for it in issues:
                print(f"  - {it}")
        if missing:
            pending_target_count += len(missing)
            print(f"[待建目标链接] {rel}: {len(missing)} 处（如 {', '.join(missing[:3])}）")

    print(f"\n校验完成：格式/路径错误 {error_count} 处，待整理章节/专题占位链接 {pending_target_count} 处。")


if __name__ == "__main__":
    main()
