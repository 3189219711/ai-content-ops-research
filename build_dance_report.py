import base64
import io
import os
from PIL import Image

OUT = "D:/TOJOY/AI内容运营开源项目调研/账号分类复刻/抖音舞蹈大V盘点与复刻规划_汇报版.html"

BASE = "D:/TOJOY/AI内容运营开源项目调研/抖音账号/抖音舞蹈大V"

DATA = [
    {
        "category": "美女类",
        "name": "代古拉 k",
        "imgs": [
            (f"{BASE}/美女类-代古拉 k/1a6197d2a18dd011d5843179c0d3e33a.jpg", "主页"),
            (f"{BASE}/美女类-代古拉 k/06427d0d62ca72aa27688cc4fc707425.jpg", "作品列表"),
        ],
        "tags": ["潮流热舞", "多人共创"],
        "followers": "2112.4万", "likes": "5.2亿", "works": "435",
        "positioning": "高颜值潮流热舞，强共创与人气美女联动，feed 封面靠脸驱动点击。",
        "learn": "固定 AI 数字人美女形象 + 热门编舞 + 换装/多人共创，走颜值驱动路线。"
    },
    {
        "category": "美女类",
        "name": "宸荨樱桃",
        "imgs": [
            (f"{BASE}/美女类-宸荨樱桃/2276929efcc7f58d4a7086b365f00778.jpg", "主页"),
            (f"{BASE}/美女类-宸荨樱桃/9ecfdd4907128beb19906f19697b1e90.jpg", "作品列表"),
        ],
        "tags": ["国风民族", "变装热舞"],
        "followers": "1394.1万", "likes": "3.4亿", "works": "166",
        "positioning": "「五十六个民族舞」系列，国风/民族变装 + 对应舞蹈，差异化强于纯热舞。",
        "learn": "固定 AI 数字人美女 + 民族/古风换装 + 对应舞蹈，做有记忆点的变装号。"
    },
    {
        "category": "团舞类",
        "name": "不齐舞团",
        "imgs": [
            (f"{BASE}/团舞类-不齐舞团/a73c28c6f9eb0b5a3f2a6d4eae171828.jpg", "主页"),
            (f"{BASE}/团舞类-不齐舞团/374f075293853267393222c21a16b67b.jpg", "作品列表"),
        ],
        "tags": ["街头街舞", "男团齐舞", "共创"],
        "followers": "2075.1万", "likes": "4.0亿", "works": "643",
        "positioning": "街头街舞男团，队形整齐、卡点爽感强，户外共创 + 高互动。",
        "learn": "多人虚拟角色团 + 街头/实景 + 队形卡点，把真人团换成风格化角色。"
    },
    {
        "category": "团舞类",
        "name": "舞三",
        "imgs": [
            (f"{BASE}/团舞类-舞三/93b20773b58ef82a5f1a82f65550f218.png", "主页"),
            (f"{BASE}/团舞类-舞三/5232a762c9b353bb89964439b36fa2a0.png", "作品列表"),
        ],
        "tags": ["匿名面具", "角色团", "视觉冲击"],
        "followers": "63.9万", "likes": "2270.4万", "works": "—",
        "positioning": "匿名面具角色团，不露脸、强视觉、动作同步，单粉产出极高。",
        "learn": "虚拟角色团（面具/匿名）+ 统一场景 + 动作同步，与真人原版差异最大，最适合 AI 复刻起步。"
    }
]

ATTRACTION = {
    "美女类": {
        "cover": [
            "AI 数字人特写占画面 70% 以上，脸清晰、妆容精致",
            "高饱和/高对比色调（红、金、国风蓝绿），Feed 中一眼跳出",
            "变装前/后分屏或「3 秒前→3 秒后」强烈反差",
            "舞蹈动作定格在最张力的瞬间（甩头、踢腿、回眸）",
            "民族/古风元素服饰直接出镜，强化差异化记忆",
            "标题大字压在画面下方 1/3 处，不超过 10 个字"
        ],
        "copy": [
            "悬念型：「这身衣服，你看像哪个民族？」",
            "数字/挑战型：「3 秒变装挑战，别眨眼」",
            "互动型：「第 3 秒开始，评论区喊出舞名」",
            "情绪型：「这支舞，只跳给懂的人看」",
            "地域梗：「傣味十足」「西域风情」「苗疆少女」"
        ],
        "driver": "颜值吸引、身材展示、变装反差、民族/古风好奇心、热门舞蹈熟悉感"
    },
    "团舞类": {
        "cover": [
            "多人整齐动作定格，用「阵列感」制造视觉冲击",
            "统一 IP 角色站位（如师徒四人一字排开）强化识别",
            "面具/匿名特写制造神秘感，引发「是谁」的好奇",
            "统一服装 + 强烈配色（黑金、红金、赛博霓虹）",
            "大字标题卡/角色名牌直接贴在画面上",
            "镜面/分屏特效预告，暗示「这不是普通舞蹈」"
        ],
        "copy": [
            "IP 反差型：「师徒四人跳科目三？」",
            "整齐挑战型：「这整齐度，你能忍几秒不点赞」",
            "悬念型：「揭开面具，你猜我是谁」",
            "梗结合型：「西游天团申请出战」",
            "号召型：「艾特你最不齐的朋友来看」"
        ],
        "driver": "集体整齐爽感、经典 IP 反差、匿名好奇、角色萌帅、卡点节奏"
    }
}

IP_EXAMPLES = [
    {
        "group": "经典 IP 团",
        "examples": [
            ("西游记", "唐僧、孙悟空、猪八戒、沙僧 — 师徒一起跳热舞，反差萌极强"),
            ("三国英雄", "刘备、关羽、张飞、赵云 — 五虎将齐舞，情怀+整齐"),
            ("封神少年", "哪吒、敖丙、杨戬、雷震子 — 神话少年团，国漫感"),
        ]
    },
    {
        "group": "国潮 / 神话团",
        "examples": [
            ("山海经", "九尾狐、饕餮、应龙、白泽 — 神秘国潮，视觉冲击强"),
            ("国潮动物", "熊猫、醒狮、锦鲤、仙鹤 — 萌+吉祥，转发率高"),
            ("敦煌飞天", "伎乐天、反弹琵琶、飞天 — 仙气舞蹈，适合国风音乐"),
        ]
    },
    {
        "group": "风格 / 职业团",
        "examples": [
            ("赛博朋克", "霓虹战士、机械姬、未来警察 — 科技光效+卡点"),
            ("古风江湖", "书生、侠客、仙子、剑客 — 古风剧情+舞蹈"),
            ("职业制服", "牛仔、医生、飞行员、消防员 — 制服诱惑+整齐反差"),
        ]
    },
    {
        "group": "节日 / 主题团",
        "examples": [
            ("神仙拜年", "财神、月老、寿星、福娃 — 春节/节日营销"),
            ("十二生肖", "鼠牛虎兔龙蛇马羊 — 生肖年热点，内容可持续一年"),
        ]
    }
]


def img_to_base64(path, max_width=600, quality=75):
    with Image.open(path) as im:
        # 转换为 RGB（处理 PNG/RGBA）
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        # 等比缩放
        w, h = im.size
        if w > max_width:
            ratio = max_width / w
            new_size = (max_width, int(h * ratio))
            im = im.resize(new_size, Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality, optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{b64}"


CSS = """<style>
  :root{ --bg:#0f1117; --card:#181b23; --card-hover:#20242e; --text:#e8eaed; --text2:#9aa0a6; --accent:#8ab4f8; --accent2:#fbbc04; --border:#2c313c; --ok:#81c995; }
  *{ box-sizing:border-box; }
  body{ margin:0; padding:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
  header{ padding:48px 24px 36px; text-align:center; background:linear-gradient(180deg,#1a1d26 0%,#0f1117 100%); border-bottom:1px solid var(--border); }
  header h1{ margin:0 0 12px; font-size:32px; font-weight:600; letter-spacing:-0.5px; }
  header .sub{ color:var(--text2); font-size:15px; margin-bottom:6px; }
  header .date{ color:var(--text2); font-size:13px; }
  .container{ max-width:1100px; margin:0 auto; padding:32px 24px 64px; }
  .summary{ margin-bottom:40px; }
  .summary-cards{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:24px; }
  .summary-card{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:20px; text-align:center; }
  .summary-card .num{ font-size:28px; font-weight:700; color:var(--accent); }
  .summary-card .label{ color:var(--text2); font-size:13px; margin-top:4px; }
  .summary p{ color:var(--text2); font-size:14px; margin:0; }
  h2{ font-size:22px; margin:48px 0 20px; padding-bottom:10px; border-bottom:1px solid var(--border); }
  .category-desc{ color:var(--text2); font-size:14px; margin:-12px 0 20px; }
  .blogger-grid{ display:grid; grid-template-columns:1fr; gap:24px; }
  .blogger-card{ background:var(--card); border:1px solid var(--border); border-radius:16px; overflow:hidden; transition:background .2s,border-color .2s; }
  .blogger-card:hover{ background:var(--card-hover); border-color:#3c4352; }
  .blogger-imgs{ display:grid; grid-template-columns:1fr 1fr; gap:0; background:#0a0c10; }
  .blogger-imgs figure{ margin:0; position:relative; border-right:1px solid #0a0c10; }
  .blogger-imgs figure:last-child{ border-right:none; }
  .blogger-imgs img{ width:100%; height:auto; display:block; cursor:zoom-in; background:#111; }
  .blogger-imgs figcaption{ position:absolute; top:10px; left:10px; background:rgba(0,0,0,.65); color:#fff; font-size:11px; padding:3px 9px; border-radius:5px; letter-spacing:.5px; }
  .blogger-body{ padding:22px 24px 24px; }
  .blogger-name{ font-size:22px; font-weight:600; margin:0 0 10px; }
  .tags{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px; }
  .tag{ font-size:12px; color:var(--accent); background:rgba(138,180,248,.12); border:1px solid rgba(138,180,248,.25); border-radius:999px; padding:3px 10px; }
  .stats{ display:flex; flex-wrap:wrap; gap:16px; margin-bottom:16px; }
  .stat{ font-size:14px; color:var(--text2); }
  .stat b{ color:var(--text); font-size:18px; margin-right:4px; }
  .section-title{ font-size:12px; color:var(--text2); text-transform:uppercase; letter-spacing:.5px; margin:14px 0 6px; }
  .section-text{ font-size:14px; color:var(--text); margin:0; }
  .learn{ border-left:3px solid var(--accent2); padding-left:12px; }
  .hl{ color:var(--accent2); font-weight:600; }
  /* 吸引力设计区 */
  .attr-section{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:24px; margin-bottom:24px; }
  .attr-section h3{ margin:0 0 16px; font-size:18px; color:var(--accent); }
  .attr-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
  .attr-card{ background:rgba(138,180,248,.05); border:1px solid var(--border); border-radius:12px; padding:16px; }
  .attr-card .attr-title{ font-size:13px; font-weight:700; color:var(--accent2); margin:0 0 10px; }
  .attr-card ul{ margin:0; padding-left:16px; }
  .attr-card li{ font-size:13px; color:var(--text2); margin-bottom:6px; line-height:1.5; }
  .attr-card li:last-child{ margin-bottom:0; }
  .driver{ font-size:14px; color:var(--text); margin-top:14px; padding-top:14px; border-top:1px solid var(--border); }
  .driver b{ color:var(--ok); }
  /* IP 示例区 */
  .ip-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:16px; }
  .ip-card{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:20px; }
  .ip-card h4{ margin:0 0 14px; font-size:16px; color:var(--accent); }
  .ip-item{ display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; }
  .ip-item:last-child{ margin-bottom:0; }
  .ip-badge{ flex-shrink:0; background:rgba(251,188,4,.12); color:var(--accent2); font-size:12px; font-weight:700; padding:3px 10px; border-radius:999px; }
  .ip-desc{ font-size:13px; color:var(--text2); line-height:1.5; }
  /* 流程区 */
  .flow{ display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:8px; }
  .flow-step{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:24px; position:relative; }
  .flow-step .step-no{ display:inline-block; background:var(--accent); color:#0f1117; font-weight:700; font-size:13px; padding:3px 12px; border-radius:999px; margin-bottom:12px; }
  .flow-step h3{ margin:0 0 14px; font-size:18px; }
  .flow-list{ list-style:none; padding:0; margin:0; }
  .flow-list li{ font-size:14px; color:var(--text); padding:8px 0 8px 22px; position:relative; border-bottom:1px solid var(--border); }
  .flow-list li:last-child{ border-bottom:none; }
  .flow-list li:before{ content:"▸"; position:absolute; left:4px; color:var(--accent); }
  .arrow{ text-align:center; font-size:26px; color:var(--accent); display:flex; align-items:center; justify-content:center; }
  .callout{ background:rgba(251,188,4,.08); border:1px solid rgba(251,188,4,.4); border-left:4px solid var(--accent2); border-radius:12px; padding:18px 20px; margin-top:24px; }
  .callout .ct{ font-size:15px; font-weight:700; color:var(--accent2); margin:0 0 10px; }
  .callout .ct .star{ margin-right:6px; }
  .type-badges{ display:flex; flex-wrap:wrap; gap:10px; margin-top:8px; }
  .type-badge{ background:rgba(138,180,248,.12); border:1px solid rgba(138,180,248,.3); border-radius:10px; padding:10px 14px; flex:1; min-width:150px; }
  .type-badge b{ display:block; color:var(--accent); font-size:14px; margin-bottom:2px; }
  .type-badge span{ font-size:12px; color:var(--text2); }
  .next{ margin-top:48px; padding:24px; background:var(--card); border:1px solid var(--border); border-radius:16px; }
  .next h2{ margin:0 0 14px; padding:0; border:none; }
  .next p{ color:var(--text2); font-size:14px; margin:0 0 8px; }
  .lightbox{ display:none; position:fixed; inset:0; background:rgba(0,0,0,.92); z-index:1000; align-items:center; justify-content:center; cursor:zoom-out; }
  .lightbox img{ max-width:90vw; max-height:90vh; border-radius:8px; box-shadow:0 20px 60px rgba(0,0,0,.6); }
  @media (max-width:820px){ .summary-cards{ grid-template-columns:1fr; } .attr-grid,.ip-grid,.flow{ grid-template-columns:1fr; } .blogger-imgs{ grid-template-columns:1fr; } .blogger-imgs figure{ border-right:none; border-bottom:1px solid #0a0c10; } }
</style>"""

HTML_HEAD = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>抖音热门舞蹈大V盘点与复刻规划</title>
{CSS}
</head>
<body>
  <header>
    <h1>抖音热门舞蹈大V盘点与复刻规划</h1>
    <div class="sub">创意娱乐内容 · 账号分类复刻 · 汇报版</div>
    <div class="date">2026-08-20</div>
  </header>
  <div class="container">
    <section class="summary">
      <div class="summary-cards">
        <div class="summary-card"><div class="num">4</div><div class="label">标杆账号</div></div>
        <div class="summary-card"><div class="num">2</div><div class="label">内容分类</div></div>
        <div class="summary-card"><div class="num">亿级</div><div class="label">总获赞池</div></div>
      </div>
      <p>已按「美女类」「团舞类」筛选 4 个高数据标杆账号作为舞蹈复刻内容线参考样本。每个账号均给出粉丝/获赞数据、风格定位及复刻借鉴点，并配套吸引力设计与标准化复刻流程，支撑后续多类型数字人复刻决策。</p>
    </section>
"""


def build_attraction_html():
    html = ['    <section id="attraction">\n      <h2>内容吸引力设计：为什么让人想点击</h2>\n      <p class="category-desc">按美女类、团舞类两条线，分别设计封面、文案、点击驱动力；并提供可直接套用的角色团 IP 示例。</p>']
    for cat in ["美女类", "团舞类"]:
        a = ATTRACTION[cat]
        cover_li = "".join(f"<li>{x}</li>" for x in a["cover"])
        copy_li = "".join(f"<li>{x}</li>" for x in a["copy"])
        html.append(f'''
      <div class="attr-section">
        <h3>{cat}</h3>
        <div class="attr-grid">
          <div class="attr-card">
            <p class="attr-title">封面怎么设计</p>
            <ul>{cover_li}</ul>
          </div>
          <div class="attr-card">
            <p class="attr-title">文案怎么写</p>
            <ul>{copy_li}</ul>
          </div>
          <div class="attr-card">
            <p class="attr-title">点击驱动力</p>
            <p class="section-text" style="margin:0;font-size:13px;color:var(--text2);">{a["driver"]}</p>
          </div>
        </div>
      </div>''')

    html.append('      <h3 style="margin-top:40px;">角色团 IP 示例：具体可复用的角色组合</h3>')
    html.append('      <div class="ip-grid">')
    for g in IP_EXAMPLES:
        items = ""
        for name, desc in g["examples"]:
            items += f'<div class="ip-item"><span class="ip-badge">{name}</span><span class="ip-desc">{desc}</span></div>'
        html.append(f'''
        <div class="ip-card">
          <h4>{g["group"]}</h4>
          {items}
        </div>''')
    html.append('      </div>')
    html.append('    </section>')
    return "\n".join(html)


WORKFLOW = """
    <section id="workflow">
      <h2>复刻生产流程</h2>
      <p class="category-desc">两步闭环：先采集筛选，再复刻生产；运营全程人工拍板，不自动发布。</p>
      <div class="flow">
        <div class="flow-step">
          <span class="step-no">第一步</span>
          <h3>内容采集与选题</h3>
          <ul class="flow-list">
            <li>输入抖音大 V 主页链接</li>
            <li>设定时间范围</li>
            <li>按 <span class="hl">点赞量 / 转发量 / 评论量</span> 排序</li>
            <li>运营人工选定要复刻的舞蹈视频</li>
          </ul>
        </div>
        <div class="flow-step">
          <span class="step-no">第二步</span>
          <h3>复刻生产</h3>
          <ul class="flow-list">
            <li><span class="hl">确定主体形象（多类型数字人）</span></li>
            <li>确定配套要素：服饰 + 场景</li>
            <li>提取原视频动作 / 卡点 / 镜头</li>
            <li>生成 AI 视频</li>
            <li>质检修复 → 剪辑包装 → <span class="hl">封面直出数字人形象</span></li>
            <li><span class="hl">合规审核</span>（音乐版权 / 形象权 / 动作版权）→ 人工发布</li>
          </ul>
        </div>
      </div>
      <div class="callout">
        <p class="ct"><span class="star">★</span>核心设计：一套流程支持多类型数字人</p>
        <p style="margin:0 0 4px;font-size:14px;color:var(--text);">复刻主体不限于一种脸，支持三类形象切换，同一套动作资产可被不同形象复用：</p>
        <div class="type-badges">
          <div class="type-badge"><b>真人风格数字人</b><span>美女类（潮流 / 国风），靠脸吸引点击</span></div>
          <div class="type-badge"><b>萌宠形象</b><span>把热门舞蹈套到萌宠身上二次复刻</span></div>
          <div class="type-badge"><b>角色团</b><span>西游/封神/山海经等 IP 多角色，强视觉冲击</span></div>
        </div>
      </div>
    </section>
"""

HTML_FOOT = """
    <section class="next">
      <h2>下一步</h2>
      <p>确定美女类 / 团舞类数字人具体风格（写实甜美 / 国风 / 西游/封神角色团等），启动首个模板跑通；按娱乐性质持续扩展第二类、第三类复刻内容。</p>
      <p>详见同目录《热门舞蹈复刻流程规范.md》。</p>
    </section>
  </div>
  <div class="lightbox" id="lb" onclick="this.style.display='none'">
    <img id="lb-img" src="" alt="">
  </div>
  <script>
    document.querySelectorAll('.blogger-imgs img').forEach(img => {
      img.addEventListener('click', function(){
        document.getElementById('lb-img').src = this.src;
        document.getElementById('lb').style.display='flex';
      });
    });
  </script>
</body>
</html>
"""

categories = []
for d in DATA:
    if d["category"] not in categories:
        categories.append(d["category"])

parts = [HTML_HEAD]
for cat in categories:
    parts.append(f'    <section id="{cat}">')
    parts.append(f'      <h2>{cat}</h2>')
    if cat == "美女类":
        parts.append('      <div class="category-desc">高颜值单人/多人热舞，封面靠脸驱动点击；分潮流共创线与国风变装线两条复刻方向。</div>')
    else:
        parts.append('      <div class="category-desc">多人队形/卡点齐舞，强视觉冲击与角色化；分街头男团与匿名面具角色团两条复刻方向。</div>')
    parts.append('      <div class="blogger-grid">')
    for d in DATA:
        if d["category"] != cat:
            continue
        imgs_html = ""
        for ip, lbl in d["imgs"]:
            b64 = img_to_base64(ip)
            imgs_html += f'<figure><img src="{b64}" alt="{d["name"]}{lbl}"><figcaption>{lbl}</figcaption></figure>'
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in d["tags"])
        works_html = f'<div class="stat"><b>{d["works"]}</b>作品</div>' if d["works"] != "—" else ""
        parts.append(f'''      <div class="blogger-card">
        <div class="blogger-imgs">{imgs_html}</div>
        <div class="blogger-body">
          <div class="blogger-name">{d["name"]}</div>
          <div class="tags">{tags_html}</div>
          <div class="stats">
            <div class="stat"><b>{d["followers"]}</b>粉丝</div>
            <div class="stat"><b>{d["likes"]}</b>获赞</div>
            {works_html}
          </div>
          <div class="section-title">风格定位</div>
          <p class="section-text">{d["positioning"]}</p>
          <div class="section-title">复刻借鉴</div>
          <p class="section-text learn">{d["learn"]}</p>
        </div>
      </div>''')
    parts.append('      </div>')
    parts.append('    </section>')

parts.append(build_attraction_html())
parts.append(WORKFLOW)
parts.append(HTML_FOOT)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(parts))

size_mb = os.path.getsize(OUT) / 1024 / 1024
print(f"已生成: {OUT} ({size_mb:.2f} MB)")
