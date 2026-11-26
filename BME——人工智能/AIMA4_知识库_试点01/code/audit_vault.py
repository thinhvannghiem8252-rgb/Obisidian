"""离线扫描 UTF-8、Frontmatter、内链及其标题锚点、附件和 Python 知识点示例。"""
from collections import Counter
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

vault = Path(__file__).resolve().parents[1]


def main():
    notes = sorted(vault.rglob('*.md'))
    targets = {p.stem: p for p in notes}
    assert len(targets) == len(notes), '存在同名笔记'
    texts = {p: p.read_text(encoding='utf8') for p in notes}
    ids = set()
    counts = Counter()
    errors = []
    for p, text in texts.items():
        def check(condition, reason):
            if not condition:
                errors.append(f'{p.relative_to(vault)}: {reason}')
        fields = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        check(fields is not None, '缺 Frontmatter')
        if fields:
            for field in ('id', 'title', 'type', 'status', 'tags'):
                check(re.search(rf'(?m)^{field}:\s*\S', fields[1]), '缺 '+field)
            id = re.search(r'(?m)^id: (.+)',fields[1])[1].strip('"')
            check(id not in ids, '重复 id')
            ids.add(id)
        fences = re.findall(r'(?m)^' + chr(96)*3 + r'([^\n]*)$', text)
        check(len(fences)%2 == 0, '围栏未闭合')
        check(all(t.strip() for t in fences[::2]), '代码块缺语言')
        pattern = chr(96)*3 + r'(\w+)[^\n]*\n(.*?)\n' + chr(96)*3
        for lang, code in re.findall(pattern, text, re.S):
            if lang == 'python':
                exec(compile(code, str(p), 'exec'), {})
                counts['可执行 Python 片段'] += 1
        prose = re.sub(pattern, '', text, flags=re.S)
        check(prose.count('$$') % 2 == 0, '块公式未闭合')
        for raw in re.findall(r'\[\[(.*?)\]\]', prose):
            target = raw.replace('\\|','|').split('|',1)[0]
            name, _, heading = target.partition('#')
            dest = targets.get(name) if name else p
            check(dest is not None, '无目标 '+raw)
            if heading and dest:
                check(re.search(r'^#{1,6} '+re.escape(heading)+r'\s*$', texts[dest], re.M), '标题不存在 '+raw)
            counts['Wiki 链接'] += 1
        for path in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', prose):
            if '://' not in path:
                check((p.parent/path).is_file(),'路径失效 '+path)
                counts['相对文件链接'] += 1
    for svg in vault.rglob('*.svg'):
        ET.parse(svg)
    print(f'{len(notes)} 篇 Markdown；'+ '，'.join(f'{k} {n}' for k,n in counts.items()))
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print('结构、锚点、附件及嵌入 Python 均通过。')


if __name__ == '__main__':
    main()