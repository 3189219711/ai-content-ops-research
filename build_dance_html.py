# -*- coding: utf-8 -*-
"""把 数字人跳舞类账号单拆汇总.md 转成单文件 HTML（图片 base64 内嵌）。"""
import os, re, html, base64

SRC = r"D:/TOJOY/AI内容运营开源项目调研/账号单拆/数字人跳舞类账号单拆汇总.md"
BASE = os.path.dirname(SRC)
OUT = r"D:/TOJOY/AI内容运营开源项目调研/账号单拆/数字人跳舞类账号单拆汇总.html"

def md_inline(text):
    text = html.escape(text)
    text = re.sub(r'&lt;(https?://[^&]+)&gt;',
                  lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>',
                  text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text

def embed_image(relpath, alt):
    abspath = os.path.normpath(os.path.join(BASE, relpath))
    if os.path.exists(abspath):
        with open(abspath, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = abspath.rsplit('.', 1)[-1].lower()
        mime = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg',
                'png': 'image/png', 'webp': 'image/webp', 'gif': 'image/gif'}.get(ext, 'image/jpeg')
        src = f"data:{mime};base64,{b64}"
        return (f'<figure class="shot">'
                f'<img src="{src}" alt="{html.escape(alt)}" loading="lazy" onclick="openLightbox(this)">'
                f'<figcaption>{html.escape(alt)}</figcaption></figure>')
    return f'<p class="missing">[图片缺失: {html.escape(relpath)}]</p>'

def split_row(r):
    r = r.strip().strip('|')
    return [c.strip() for c in r.split('|')]

def parse_table(rows):
    header = split_row(rows[0])
    body = []
    for r in rows[1:]:
        cells = split_row(r)
        if all(set(c) <= set('-: ') for c in cells) and any('-' in c for c in cells):
            continue
        body.append(cells)
    thead = '<tr>' + ''.join(f'<th>{md_inline(c)}</th>' for c in header) + '</tr>'
    tbody = ''.join('<tr>' + ''.join(f'<td>{md_inline(c)}</td>' for c in row) + '</tr>' for row in body)
    return f'<table class="tbl"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'

def slug(text, seen):
    s = re.sub(r'[^\w\u4e00-\u9fff-]', '', text)
    s = s or 'sec'
    base = s
    k = 1
    while s in seen:
        k += 1
        s = f'{base}-{k}'
    seen.add(s)
    return s

lines = open(SRC, encoding='utf-8').read().split('\n')
out, nav, seen = [], [], set()
account_cells = []
i, n = 0, len(lines)

def flush_account_cells():
    if not account_cells:
        return
    out.append('<div class="work-grid">')
    out.extend(account_cells)
    out.append('</div>')
    account_cells.clear()

def parse_ul(start_idx):
    items = []
    j = start_idx
    while j < n and re.match(r'^-\s+', lines[j]):
        items.append('<li>' + md_inline(re.sub(r'^-\s+', '', lines[j])) + '</li>')
        j += 1
    return '<ul>' + ''.join(items) + '</ul>', j

while i < n:
    line = lines[i]
    if line.strip() == '---':
        flush_account_cells()
        out.append('<hr>'); i += 1; continue
    # 连续独立图片 -> 画廊网格
    if re.match(r'^!\[(.*?)\]\((.*?)\)$', line.strip()):
        flush_account_cells()
        imgs = []
        while i < n and re.match(r'^!\[(.*?)\]\((.*?)\)$', lines[i].strip()):
            mm = re.match(r'^!\[(.*?)\]\((.*?)\)$', lines[i].strip())
            imgs.append(embed_image(mm.group(2), mm.group(1)))
            i += 1
        out.append('<div class="gallery">' + ''.join(imgs) + '</div>')
        continue
    mh = re.match(r'^(#{1,4})\s+(.*)$', line)
    if mh:
        lvl = len(mh.group(1)); text = mh.group(2).strip()
        anc = slug(text, seen)
        if lvl == 1:
            flush_account_cells()
            out.append(f'<h{lvl} id="{anc}">{md_inline(text)}</h{lvl}>'); i += 1; continue
        if lvl == 2:
            flush_account_cells()
            nav.append((anc, text))
            out.append(f'<h{lvl} id="{anc}">{md_inline(text)}</h{lvl}>'); i += 1; continue
        if lvl == 3:
            flush_account_cells()
            out.append(f'<h{lvl} id="{anc}">{md_inline(text)}</h{lvl}>'); i += 1; continue
        # h4 是单条舞蹈标题（后面跟 ul + 图片）
        h4_html = f'<h4 id="{anc}">{md_inline(text)}</h4>'
        i += 1
        while i < n and not lines[i].strip():
            i += 1
        ul_html, i = parse_ul(i)
        while i < n and not lines[i].strip():
            i += 1
        fig_html = ''
        if i < n:
            m2 = re.match(r'^!\[(.*?)\]\((.*?)\)$', lines[i].strip())
            if m2:
                fig_html = embed_image(m2.group(2), m2.group(1))
                i += 1
        cell = f'''<div class="work-cell">
  <div class="work-media">{fig_html}</div>
  <div class="work-meta">
    {h4_html}
    {ul_html}
  </div>
</div>'''
        account_cells.append(cell)
        continue
    if line.strip().startswith('```'):
        flush_account_cells()
        buf = []
        i += 1
        while i < n and not lines[i].strip().startswith('```'):
            buf.append(lines[i]); i += 1
        i += 1  # 跳过结束 ```
        out.append('<pre class="codeblock"><code>' + html.escape('\n'.join(buf)) + '</code></pre>')
        continue
    if line.startswith('> '):
        flush_account_cells()
        buf = []
        while i < n and lines[i].startswith('> '):
            buf.append(lines[i][2:]); i += 1
        out.append('<blockquote>' + md_inline(' '.join(buf)) + '</blockquote>'); continue
    if line.strip().startswith('|'):
        flush_account_cells()
        rows = []
        while i < n and lines[i].strip().startswith('|'):
            rows.append(lines[i]); i += 1
        out.append(parse_table(rows)); continue
    if re.match(r'^-\s+', line):
        flush_account_cells()
        items = []
        while i < n and re.match(r'^-\s+', lines[i]):
            items.append('<li>' + md_inline(re.sub(r'^-\s+', '', lines[i])) + '</li>')
            i += 1
        out.append('<ul>' + ''.join(items) + '</ul>'); continue
    if not line.strip():
        i += 1; continue
    flush_account_cells()
    out.append('<p>' + md_inline(line) + '</p>'); i += 1

flush_account_cells()

body_html = '\n'.join(out)
nav_html = '\n'.join(f'<a href="#{a}" class="navlink">{html.escape(t)}</a>' for a, t in nav)

CSS = """
:root{--bg:#f7f8fa;--card:#fff;--ink:#1f2329;--sub:#6b7280;--line:#e5e7eb;--accent:#e8453c;--accent2:#2f6fed;--soft:#fff5f4;}
*{box-sizing:border-box;}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink);line-height:1.75;font-size:15px;}
.hero{background:linear-gradient(135deg,#ff6a5e,#e8453c);color:#fff;padding:38px 24px 30px;}
.hero h1{margin:0 0 6px;font-size:26px;font-weight:800;letter-spacing:.5px;}
.hero p{margin:0;opacity:.92;font-size:13px;}
.nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);display:flex;gap:6px;padding:10px 16px;overflow-x:auto;}
.navlink{flex:0 0 auto;text-decoration:none;color:var(--sub);font-size:13px;padding:6px 12px;border-radius:20px;background:#f0f1f3;white-space:nowrap;}
.navlink:hover{color:#fff;background:var(--accent);}
.wrap{max-width:920px;margin:0 auto;padding:28px 18px 80px;}
h2{font-size:22px;margin:42px 0 16px;padding-left:12px;border-left:5px solid var(--accent);scroll-margin-top:64px;}
h3{font-size:18px;margin:26px 0 10px;color:#2b2f36;scroll-margin-top:64px;}
h4{font-size:16px;margin:18px 0 8px;color:#374151;scroll-margin-top:64px;}
blockquote{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent2);border-radius:10px;padding:14px 18px;margin:16px 0;color:var(--sub);font-size:14px;}
hr{border:none;border-top:1px solid var(--line);margin:28px 0;}
p{margin:10px 0;}
a{color:var(--accent2);word-break:break-all;}
ul{margin:10px 0;padding-left:22px;}
li{margin:5px 0;}
strong{color:#111;}
code{background:#f1f2f4;padding:1px 6px;border-radius:5px;font-size:13px;}
.codeblock{background:#1e2530;color:#e6edf3;border-radius:10px;padding:16px 18px;margin:16px 0;font-size:13px;line-height:1.6;overflow-x:auto;white-space:pre-wrap;word-break:break-all;}
.codeblock code{background:none;padding:0;color:inherit;}
.tbl{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.06);font-size:14px;}
.tbl th,.tbl td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top;}
.tbl thead th{background:#fafafa;font-weight:700;color:#222;}
.tbl tbody tr:nth-child(odd){background:#fcfcfd;}
.shot{margin:14px 0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.shot img{display:block;width:100%;height:auto;cursor:zoom-in;transition:transform .2s;}
.shot img:hover{transform:scale(1.02);}
.shot figcaption{padding:8px 12px;font-size:13px;color:var(--sub);background:#fafafa;border-top:1px solid var(--line);}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px;margin:14px 0;}
.gallery .shot{margin:0;}
.gallery .shot img{cursor:zoom-in;}
.work-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;margin:16px 0;}
.work-cell{background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.05);display:flex;flex-direction:column;}
.work-media{flex:0 0 auto;background:#f8f8f8;}
.work-media .shot{margin:0;border:none;border-radius:0;box-shadow:none;}
.work-media .shot img{display:block;width:100%;height:auto;cursor:zoom-in;transition:transform .2s;}
.work-media .shot img:hover{transform:scale(1.02);}
.work-media .shot figcaption{display:none;}
.work-meta{padding:8px 10px 10px;font-size:12px;flex:1 1 auto;}
.work-meta h4{margin:0 0 6px;font-size:12px;color:var(--ink);line-height:1.4;}
.work-meta ul{margin:0;padding:0;list-style:none;color:var(--sub);}
.work-meta li{margin:2px 0;line-height:1.4;}
@media (max-width:640px){
  .work-grid{grid-template-columns:repeat(3,1fr);gap:10px;}
  .gallery{grid-template-columns:repeat(2,1fr);gap:10px;}
  .work-meta{font-size:11px;}
  .work-meta h4{font-size:11px;}
}
.missing{color:#c0392b;background:#fdecea;padding:8px 12px;border-radius:8px;}
#lightbox{position:fixed;inset:0;background:rgba(0,0,0,.88);display:none;justify-content:center;align-items:center;z-index:200;padding:20px;cursor:zoom-out;}
#lightbox.active{display:flex;}
#lightbox img{max-width:100%;max-height:100%;object-fit:contain;box-shadow:0 10px 40px rgba(0,0,0,.4);border-radius:8px;}
"""

SCRIPT = """
<div id="lightbox" onclick="closeLightbox()"><img id="lightbox-img" src="" alt=""></div>
<script>
function openLightbox(img){
  document.getElementById('lightbox-img').src=img.src;
  document.getElementById('lightbox').classList.add('active');
}
function closeLightbox(){
  document.getElementById('lightbox').classList.remove('active');
}
document.addEventListener('keydown',function(e){
  if(e.key==='Escape') closeLightbox();
});
</script>
"""

html_doc = ("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>数字人跳舞类账号单拆汇总</title>
<style>""" + CSS + """</style>
</head>
<body>
<div class="hero">
  <h1>数字人跳舞类账号单拆汇总</h1>
  <p>单人动作迁移 · 多人团舞 · 最近爆火舞蹈 · 复刻 SOP 与侵权风险 · 内部参考</p>
</div>
<nav class="nav">""" + nav_html + """</nav>
<div class="wrap">
""" + body_html + """
</div>
""" + SCRIPT + """
</body>
</html>""")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html_doc)

size = os.path.getsize(OUT) / 1024 / 1024
print(f"生成成功：{OUT}")
print(f"文件大小：{size:.2f} MB")
print(f"章节（导航）：{len(nav)} 个")
print(f"内嵌图片：{body_html.count('data:image/')} 张")
print(f"代码块：{body_html.count('codeblock')} 个")
