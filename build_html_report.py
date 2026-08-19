# -*- coding: utf-8 -*-
"""
生成《抖音爆款账号复刻策略汇报》单文件 HTML。
图片以 base64 内嵌，保证单文件自包含、可直接发给领导。
数据来源：benchmarks/ 下 6 份复刻路径汇总 + 抖音账号/ 下收集截图。
"""
import os
import base64

BASE = r"D:\TOJOY\AI内容运营开源项目调研"
IMG_DIR = os.path.join(BASE, "抖音账号")

def b64(path):
    """读取图片转 base64 data uri。"""
    full = os.path.join(IMG_DIR, path)
    ext = os.path.splitext(full)[1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    with open(full, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/{mime};base64,{data}"

# ---------------------------------------------------------------------------
# 1. 账号数据（链接 + 抖音号 + 粉丝/获赞 + 代表截图）
# ---------------------------------------------------------------------------
# 字段：cat(大类) sub(子类) name url douyin fans likes img(相对IMG_DIR) note(爆款/公式要点)
ACCOUNTS = [
    # ===== 创意娱乐 - AI萌宠 =====
    dict(cat="创意娱乐视频", sub="AI 萌宠类", name="胖橘什么猫",
         url="https://v.douyin.com/p2oNHdVsNMQ/", douyin="61189914847",
         fans="未获取（样本可见万赞级爆款）", likes="—",
         img=r"AI萌宠类视频\胖橘什么猫\72419e6416ffe34e2f2ad847cade4ae8.jpg",
         note="单猫歌舞 + 经典老歌 BGM；第50集《笑红尘》1.7万赞/转发率22%"),
    dict(cat="创意娱乐视频", sub="AI 萌宠类", name="拾宠不昧",
         url="https://v.douyin.com/8WDYKQRKu58/", douyin="43900322217",
         fans="1.7 万", likes="67.7 万",
         img=r"AI萌宠类视频\拾宠不昧\7bf837f2afab1e9c87366aa5dcef5106.jpg",
         note="猫狗双人播客吐槽；第38集 7233赞/转发率166%"),
    dict(cat="创意娱乐视频", sub="AI 萌宠类", name="打工小狗的日常",
         url="https://v.douyin.com/php2gmYySAE/", douyin="177036811",
         fans="3.2 万", likes="47 万",
         img=r"AI萌宠类视频\打工小狗的日常\70caca8ee0975aec82c35f3931dad637.jpg",
         note="单狗犬傲天人设 + 跳舞；第45集《鸿雁》3.7万赞/5.3万转"),
    dict(cat="创意娱乐视频", sub="AI 萌宠类", name="可爱胖橘的日常",
         url="https://v.douyin.com/sJOTk12UPMA/", douyin="56098129649",
         fans="4.9 万", likes="109.1 万",
         img=r"AI萌宠类视频\可爱胖橘的日常\60caa2680c170c7a8e66599f2f8f3db8.jpg",
         note="胖橘夫妻CP + 生活矛盾反转；第31集 3.1万赞/5.9万转"),
    dict(cat="创意娱乐视频", sub="AI 萌宠类", name="Pearl.",
         url="https://v.douyin.com/5LJU8gGzbD0/", douyin="92581278016",
         fans="5847", likes="70.7 万",
         img=r"AI萌宠类视频\Pearl.\e652abf353608ba52cc38f532425b71c.jpg",
         note="Seedance2.5 电影感 + 经典IP；蜘蛛侠 25.2万赞/38.7万转"),
    # ===== 创意娱乐 - 数字人跳舞 =====
    dict(cat="创意娱乐视频", sub="数字人跳舞类", name="芊芊baby",
         url="https://v.douyin.com/11SDhJt5LFc/", douyin="76257569422",
         fans="低粉（样本数百赞）", likes="—",
         img=r"数字人跳舞类视频\芊芊baby\7ed39c112f86fa38519f886d08b8aaf1.jpg",
         note="固定AI数字人 + 每日换装 + 简单跳舞 + 购物车；收藏率35%-50%"),
    # ===== 创意娱乐 - 数字人唱歌 =====
    dict(cat="创意娱乐视频", sub="数字人唱歌类", name="张十二",
         url="", douyin="",
         fans="23.3 万", likes="306.9 万",
         img=r"数字人唱歌类视频\张十二\4c04b8bee39b938ee808b91166385a23.jpg",
         note="固定AI僧人 + 禅意场景 + 梵音；《野心家》15.1万赞/3.9万转"),
    dict(cat="创意娱乐视频", sub="数字人唱歌类", name="疯子！",
         url="", douyin="",
         fans="12.3 万", likes="79.1 万",
         img=r"数字人唱歌类视频\疯子！\8d1f20aa7944cc50e888659d85f8e782.jpg",
         note="固定AI女歌手 + 舞台 + 老歌翻唱；《最真的梦》7.8万赞/1.2万转"),
    dict(cat="创意娱乐视频", sub="数字人唱歌类", name="初心&",
         url="", douyin="66125897008",
         fans="7.0 万", likes="38.1 万",
         img=r"数字人唱歌类视频\初心&\5804b1fe519199fecc5529e7d9adc709.jpg",
         note="固定AI烟嗓女声 + 录音棚；《Andy》5.9万赞/1.1万转"),
    dict(cat="创意娱乐视频", sub="数字人唱歌类", name="棉袄伴歌行",
         url="", douyin="",
         fans="11.9 万", likes="78.1 万",
         img=r"数字人唱歌类视频\棉袄伴歌行\40f88ec78ecd5f9b09d0c7ba99b7d7c9.jpg",
         note="固定AI父女组合 + 吉他弹唱；《热血颂》8.9万赞/7757转"),
    # ===== 情感鸡汤 =====
    dict(cat="情感鸡汤类视频", sub="情感鸡汤类", name="若初情感",
         url="https://v.douyin.com/x4_u339J3bo/", douyin="86866849286",
         fans="7.3 万", likes="65.5 万",
         img=r"情感鸡汤类视频\若初情感\18e20b3595d4f6a002d8862f4e3479a2.jpg",
         note="温柔女声 + 夜景 + 大字情绪文案；《在我最难的时候》10.3万赞"),
    dict(cat="情感鸡汤类视频", sub="情感鸡汤类", name="云朵电台",
         url="https://v.douyin.com/elxv8aOj0Sw/", douyin="80961763765",
         fans="8093", likes="67.8 万",
         img=r"情感鸡汤类视频\云朵电台\6a3dc558aa9dd29b21b63c3403fa5e0f.jpg",
         note="早安日签 + 固定街道 + 热点；《8月18发财日》14.3万赞/转发率81%"),
    # ===== 玄学命理 =====
    dict(cat="玄学命理类视频", sub="玄学命理讲解类", name="止语",
         url="https://v.douyin.com/c2FqCSB75M0/", douyin="86866849286",
         fans="29.8 万", likes="284.1 万",
         img=r"玄学命理类视频\止语\2bb130262fcbcbc06bef4dcf321f5b9f.jpg",
         note="AI黑金道长 + 现代情绪痛点；《背叛你的人替你挡灾》1.9万赞"),
    dict(cat="玄学命理类视频", sub="玄学命理讲解类", name="柏言国学安迪师兄",
         url="https://v.douyin.com/aXLUhVT7VAw/", douyin="fuxi867",
         fans="4.1 万", likes="49.2 万",
         img=r"玄学命理类视频\柏言国学安迪师兄\6db285a77c135fa92c1537fd06311972.jpg",
         note="国学导师 + 书房 + 问句标题；《穿衣颜色》13.1万赞/10.3万转"),
]

# 样式类参考图（无具体账号，纯样式）
STYLE_IMGS = {
    "health_3d": r"健康小贴士\3D轻拟物信息图\2c306ae7e7c68ff700f4f10fc8142fd3.jpg",
    "health_plan": r"健康小贴士\健康计划信息图\158d0b96ff997c2a2d321d1817257115.jpg",
    "health_draw": r"健康小贴士\手绘扁平插画信息图\2e6d8d6b1c13f4e116b49aeeee204258.jpg",
    "fortune": r"玄学命理类视频\每日运势图文\3710a42f165d1efa15feceaf59a02543.jpg",
    "dance_hot": r"数字人跳舞类视频\最近抖音热门舞蹈\d7b4faaa140eb3efa1f8ec36b04a0a47.jpg",
}

# ---------------------------------------------------------------------------
# 2. HTML 片段生成
# ---------------------------------------------------------------------------
def account_card(a):
    link = f'<a href="{a["url"]}" target="_blank" rel="noopener">🔗 打开主页</a>' if a["url"] else '<span class="muted">链接未提供</span>'
    dy = a["douyin"] if a["douyin"] else "—"
    return f"""
    <div class="card">
      <div class="thumb"><img src="{b64(a['img'])}" alt="{a['name']}"></div>
      <div class="card-body">
        <div class="card-head">
          <span class="tag tag-sub">{a['sub']}</span>
          <h4>{a['name']}</h4>
        </div>
        <div class="metrics">
          <div><span class="m-label">粉丝</span><span class="m-val">{a['fans']}</span></div>
          <div><span class="m-label">获赞</span><span class="m-val">{a['likes']}</span></div>
          <div><span class="m-label">抖音号</span><span class="m-val small">{dy}</span></div>
        </div>
        <div class="links">{link}</div>
        <p class="note">{a['note']}</p>
      </div>
    </div>"""

def account_grid(cat, sub=None):
    items = [a for a in ACCOUNTS if a["cat"] == cat and (sub is None or a["sub"] == sub)]
    cards = "\n".join(account_card(a) for a in items)
    return f'<div class="grid">\n{cards}\n</div>'

# CSS
CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
  color: #1f2933; background: #f4f6fb; line-height: 1.65; font-size: 15px; }
a { color: #2563eb; text-decoration: none; }
a:hover { text-decoration: underline; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px 80px; }

/* 顶部 */
header.hero { background: linear-gradient(135deg,#0f2c52 0%,#1d4e89 60%,#2d6fb3 100%);
  color:#fff; padding: 48px 20px 40px; margin-bottom: 0; }
header.hero .inner { max-width: 1180px; margin: 0 auto; }
header.hero h1 { font-size: 30px; font-weight: 800; letter-spacing: 1px; }
header.hero .sub { opacity:.9; margin-top: 10px; font-size: 15px; }
header.hero .meta { margin-top: 18px; display:flex; gap: 26px; flex-wrap: wrap; font-size: 13px; opacity:.85; }

/* 导航 */
nav.toc { position: sticky; top: 0; z-index: 50; background: #fff; border-bottom: 1px solid #e3e8f0;
  box-shadow: 0 2px 8px rgba(0,0,0,.04); }
nav.toc .inner { max-width: 1180px; margin: 0 auto; display: flex; gap: 4px; flex-wrap: wrap; padding: 10px 20px; }
nav.toc a { padding: 6px 12px; border-radius: 999px; font-size: 13px; color: #334155; background:#f1f5f9; }
nav.toc a:hover { background:#dbeafe; color:#1d4e89; text-decoration:none; }

/* 区块 */
section { margin-top: 46px; }
.sec-head { display:flex; align-items: baseline; gap: 12px; border-left: 5px solid #1d4e89; padding-left: 14px; margin-bottom: 18px; }
.sec-head h2 { font-size: 23px; color:#0f2c52; font-weight: 800; }
.sec-head .en { color:#94a3b8; font-size: 14px; }
.sub-head { font-size: 18px; font-weight: 700; color:#1d4e89; margin: 26px 0 14px;
  padding-bottom: 6px; border-bottom: 2px dashed #cbd5e1; }
.lead { background:#eef4fb; border:1px solid #d3e2f5; border-radius: 12px; padding: 16px 20px; margin: 14px 0; color:#243b53; }
.lead b { color:#0f2c52; }

/* 卡片网格 */
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px,1fr)); gap: 18px; margin-top: 8px; }
.card { background:#fff; border:1px solid #e6ebf2; border-radius: 14px; overflow: hidden;
  box-shadow: 0 4px 14px rgba(15,44,82,.06); transition: .18s; display:flex; flex-direction:column; }
.card:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(15,44,82,.12); }
.thumb { height: 200px; background:#eef1f6; overflow:hidden; }
.thumb img { width:100%; height:100%; object-fit: cover; }
.card-body { padding: 14px 16px 16px; display:flex; flex-direction:column; gap:10px; flex:1; }
.card-head { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
.card-head h4 { font-size:16px; color:#0f2c52; }
.tag { font-size:11px; padding:2px 9px; border-radius:999px; font-weight:600; }
.tag-sub { background:#e0ecfb; color:#1d4e89; }
.metrics { display:flex; gap:10px; background:#f8fafc; border-radius:10px; padding:10px; }
.metrics > div { flex:1; text-align:center; }
.m-label { display:block; font-size:11px; color:#94a3b8; }
.m-val { display:block; font-size:14px; font-weight:700; color:#0f2c52; }
.m-val.small { font-size:12px; word-break:break-all; }
.links { font-size:13px; }
.note { font-size:13px; color:#475569; background:#f8fafc; border-left:3px solid #cbd5e1; padding:8px 10px; border-radius:0 8px 8px 0; }

/* 表格 */
table { width:100%; border-collapse: collapse; margin: 14px 0; background:#fff; font-size:13.5px;
  border:1px solid #e6ebf2; border-radius:10px; overflow:hidden; }
th, td { padding: 10px 12px; text-align:left; border-bottom:1px solid #edf1f6; vertical-align: top; }
thead th { background:#1d4e89; color:#fff; font-weight:600; }
tbody tr:nth-child(even) { background:#f7fafd; }
.pri { font-weight:700; color:#b45309; }
.high { color:#16a34a; font-weight:700; }
.med { color:#ca8a04; font-weight:700; }
.low { color:#94a3b8; }
.muted { color:#94a3b8; }

/* 步骤条 */
.steps { counter-reset: step; margin: 14px 0; padding: 0; list-style:none; }
.steps li { position:relative; padding: 10px 10px 10px 46px; border-left:2px solid #cdd9ea; margin-left: 18px; }
.steps li::before { counter-increment: step; content: counter(step); position:absolute; left:-16px; top:8px;
  width:30px; height:30px; border-radius:50%; background:#1d4e89; color:#fff; font-weight:700;
  display:flex; align-items:center; justify-content:center; font-size:14px; }
.steps li:last-child { border-left-color: transparent; }
.steps b { color:#0f2c52; }

/* 警示框 */
.warn { background:#fff7ed; border:1px solid #fed7aa; border-radius:12px; padding:14px 18px; margin:14px 0; }
.warn h4 { color:#c2410c; margin-bottom:6px; }
.danger { background:#fef2f2; border-color:#fecaca; }
.danger h4 { color:#b91c1c; }

/* 两列 */
.two-col { display:grid; grid-template-columns: 1fr 1fr; gap:18px; }
@media (max-width: 760px){ .two-col{ grid-template-columns:1fr; } .sec-head h2{font-size:19px;} }

footer { margin-top: 60px; padding: 24px; text-align:center; color:#94a3b8; font-size:13px; border-top:1px solid #e3e8f0; }
"""

# 内容区块
def build():
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>抖音爆款账号复刻策略汇报</title>
<style>{CSS}</style>
</head>
<body>
<header class="hero"><div class="inner">
  <h1>抖音爆款账号复刻策略汇报</h1>
  <div class="sub">从「爆款拆解」到「转化为我们自己的视频」—— 4 大类别 · 14 个对标账号 · 可落地复刻路径</div>
  <div class="meta">
    <span>📅 日期：2026-08-19</span>
    <span>📁 数据：benchmarks/ 汇总 + 抖音账号/ 截图</span>
    <span>🎯 目标：直接复刻成自己的娱乐账号</span>
  </div>
</div></header>
<nav class="toc"><div class="inner">
  <a href="#overview">核心结论</a>
  <a href="#ent">一、创意娱乐视频</a>
  <a href="#health">二、健康小贴士</a>
  <a href="#emotion">三、情感鸡汤</a>
  <a href="#meta">四、玄学命理</a>
  <a href="#priority">五、起步优先级</a>
  <a href="#compliance">六、合规红线</a>
</div></nav>
<div class="wrap">
""")

    # ===== 核心结论 =====
    parts.append("""
<section id="overview">
  <div class="sec-head"><h2>核心结论</h2><span class="en">Executive Summary</span></div>
  <div class="lead">
    本汇报拆解了 <b>4 大类、14 个对标账号</b>，提炼出可直接复刻的爆款公式。核心判断：<br>
    ① <b>爆款能被复刻的是「结构、节奏、传播触发点」，不是具体角色和文案</b>——换角色、换场景、换 BGM、改文案即可规避搬运；<br>
    ② <b>制作门槛从低到高</b>：情感鸡汤 ≈ 健康图文 &lt; AI 萌宠 ≈ 数字人唱歌 &lt; 数字人跳舞 &lt; 玄学电影感；<br>
    ③ <b>建议起步顺序</b>：情感鸡汤（验证生产系统）→ 健康小贴士（图文模板化）→ AI 萌宠 B/D 路径 → 数字人唱歌 → 玄学命理；<br>
    ④ <b>合规是两条赛道的生死线</b>：数字人唱歌（歌曲版权/声音权/形象权）、玄学命理（必须免责声明、不做个人预测）。
  </div>
  <table>
    <thead><tr><th>大类</th><th>对标账号数</th><th>复刻形态</th><th>起步优先级</th><th>核心风险</th></tr></thead>
    <tbody>
      <tr><td><b>创意娱乐视频</b><br><span class="muted">AI萌宠 / 数字人唱跳</span></td><td>11</td><td>AI角色表演 / 对口型 / 动作迁移</td><td class="med">中（萌宠B/D优先）</td><td>歌曲版权、形象权</td></tr>
      <tr><td><b>健康小贴士</b></td><td>样式3类</td><td>信息图模板（图文）</td><td class="high">高（模板化日更）</td><td>低</td></tr>
      <tr><td><b>情感鸡汤类视频</b></td><td>2</td><td>固定模板 + TTS + 大字文案</td><td class="high">最高（验证系统）</td><td>低</td></tr>
      <tr><td><b>玄学命理类视频</b></td><td>2 + 图文</td><td>AI角色口播 / 运势图文</td><td class="med">中</td><td>迷信合规红线</td></tr>
    </tbody>
  </table>
</section>
""")

    # ===== 一、创意娱乐 =====
    parts.append("""
<section id="ent">
  <div class="sec-head"><h2>一、创意娱乐视频</h2><span class="en">Creative & Entertainment</span></div>
  <div class="lead">本类是直接"换皮成自己娱乐账号"的核心。爆款公式高度一致：<b>固定角色壳 + 强冲突/强共鸣内容 + 转发触发点</b>。
  覆盖 AI 萌宠（5账号）、数字人跳舞（1账号+热舞素材）、数字人唱歌（4账号）。</div>
""")

    # 1.1 AI萌宠
    parts.append("""<h3 class="sub-head">1.1 AI 萌宠类 · 5 条复刻路径</h3>""")
    parts.append(account_grid("创意娱乐视频", "AI 萌宠类"))
    parts.append("""
  <table>
    <thead><tr><th>路径</th><th>原账号</th><th>原公式</th><th>你换什么</th><th>难度</th><th>优先级</th></tr></thead>
    <tbody>
      <tr><td><b>A</b></td><td>胖橘什么猫</td><td>单猫歌舞 + 经典老歌BGM</td><td>换动物+换BGM+换口型歌词</td><td>中</td><td>中</td></tr>
      <tr><td><b>B</b></td><td>拾宠不昧</td><td>猫狗双人播客 + 吐槽话题</td><td>换动物组合+换场景+换话题</td><td>低</td><td class="high">高</td></tr>
      <tr><td><b>C</b></td><td>打工小狗的日常</td><td>单狗人设 + 跳舞/对口型</td><td>换动物+换人设道具+换BGM</td><td>中高</td><td>中</td></tr>
      <tr><td><b>D</b></td><td>可爱胖橘的日常</td><td>双动物CP + 生活矛盾反转</td><td>换CP组合+换矛盾主题+换场景</td><td>中</td><td class="high">高</td></tr>
      <tr><td><b>E</b></td><td>Pearl.</td><td>电影感 + 经典IP改编</td><td>换IP+换动物主角+换场景</td><td>高</td><td class="low">低(旗舰)</td></tr>
    </tbody>
  </table>
  <ul class="steps">
    <li><b>换角色壳</b>：用即梦/Midjourney 生成固定动物形象（参考图锁定一致性）。</li>
    <li><b>换内容</b>：保留"表演+反转/吐槽/共鸣"结构，替换成你的话题赛道。</li>
    <li><b>加转发触发</b>：标题/结尾写"@你那个XX的朋友""是不是你"，主攻私聊/群聊转发。</li>
    <li><b>避坑</b>：禁止直接搬运原视频；同一账号调性不切换；纯展示无冲突必扑街。</li>
  </ul>
""")

    # 1.2 数字人跳舞
    parts.append("""<h3 class="sub-head">1.2 数字人跳舞类 · 低粉带货模型 + 动作迁移</h3>""")
    parts.append(account_grid("创意娱乐视频", "数字人跳舞类"))
    parts.append(f"""
  <div class="two-col">
    <div>
      <p><b>公式</b>：固定 AI 数字人美女 + 每日换装 + 简单跳舞 + 种草标题 + 购物车带货。
      本质不是做娱乐爆款，而是<b>低粉精准带货</b>；指标看收藏率(35%-50%)、转发率(46%-68%)、加购，而非点赞。</p>
      <p class="note">代表热舞素材（已收集）：jumpstyle、三人拖拉机、梦的翅膀受了伤DJ、满级病友舞、正太扭腰舞、加麻不加辣。</p>
    </div>
    <div><img src="{b64(STYLE_IMGS['dance_hot'])}" style="width:100%;border-radius:12px;border:1px solid #e6ebf2;"></div>
  </div>
  <h4 style="margin:16px 0 6px;color:#0f2c52;">AI 舞蹈动作迁移 SOP（5 步）</h4>
  <ul class="steps">
    <li><b>选参考 + 预处理</b>：选抖音爆款热舞，按 ≤15s 切段，面部遮挡。</li>
    <li><b>生成绿幕白模动作视频</b>：上传参考视频到 AI 画布，生成红白素体动作（锁动作/运镜/节奏）。</li>
    <li><b>准备替换素材</b>：你的数字人三视图 + 场景图。</li>
    <li><b>合并生成最终片段</b>：白模视频 + 角色图 + 场景图三合一，提示词用 @ 对应位置。</li>
    <li><b>剪辑拼接 + 配乐</b>：多段扔进剪辑软件拼合，重新配乐出成品。</li>
  </ul>
""")

    # 1.3 数字人唱歌
    parts.append("""<h3 class="sub-head">1.3 数字人唱歌类 · 4 条路径 + 版权合规</h3>""")
    parts.append(account_grid("创意娱乐视频", "数字人唱歌类"))
    parts.append("""
  <table>
    <thead><tr><th>路径</th><th>来源</th><th>核心公式</th><th>你的复刻类型</th></tr></thead>
    <tbody>
      <tr><td><b>A 禅意国风</b></td><td>张十二</td><td>固定AI僧人 + 禅意场景 + 梵音改编</td><td>原创虚拟国风角色 + 老歌新编</td></tr>
      <tr><td><b>B 舞台女声</b></td><td>疯子！</td><td>固定AI女歌手 + 舞台 + 老歌翻唱</td><td>原创虚拟女歌手 + 金曲翻唱</td></tr>
      <tr><td><b>C 烟嗓情绪</b></td><td>初心&</td><td>固定AI烟嗓 + 录音棚近景 + 热歌cover</td><td>原创虚拟烟嗓 + 港风/摇滚</td></tr>
      <tr><td><b>D 双人弹唱</b></td><td>棉袄伴歌行</td><td>固定AI父女 + 吉他弹唱 + 温馨</td><td>原创虚拟双人 + 民谣对唱</td></tr>
    </tbody>
  </table>
  <div class="warn danger">
    <h4>⚠ 版权与合规（数字人唱歌重点）</h4>
    • <b>歌曲版权</b>：用抖音/汽水音乐版权曲库，或自己翻唱/录干声；账号起量后必须切合规音源。<br>
    • <b>声音权</b>：绝对不用明星/可识别真人声音；用平台授权 TTS 或自己录；发布勾选「内容由 AI 生成」。<br>
    • <b>形象权</b>：角色必须原创 AI，不传真人明星照，不做写实撞脸。<br>
    • 技术链路：角色图 → 音频 → AI对口型模型 → 剪辑成品。先用 RunningHub 现成工作流验证。
  </div>
""")

    # ===== 二、健康小贴士 =====
    parts.append("""
<section id="health">
  <div class="sec-head"><h2>二、健康小贴士</h2><span class="en">Health Tips</span></div>
  <div class="lead">本类无具体对标账号，是<b>样式参考</b>。爆款壳不是"画得多好看"，而是"一眼能收藏、一图能转发"。
  三条路径共用同一套逻辑：<b>固定版式壳 + 替换主题/食材/文案 + 统一视觉资产库</b>。</div>
  <div class="grid">
""")
    for key, cap, desc in [
        ("health_3d", "A. 3D 轻拟物信息图", "左右双栏对比 + 3D食物图标 + 高饱和背景；适配食物红黑榜/成分对比。优先级高。"),
        ("health_plan", "B. 健康计划信息图", "一周计划表/数字步骤卡片/长文列表；B1一周计划表量产友好度最高。优先级最高。"),
        ("health_draw", "C. 手绘扁平插画信息图", "水彩纸纹理 + 手绘食物 + 功效卡片；适配时令养生。优先级中。"),
    ]:
        parts.append(f"""
    <div class="card">
      <div class="thumb"><img src="{b64(STYLE_IMGS[key])}" alt="{cap}"></div>
      <div class="card-body"><div class="card-head"><h4>{cap}</h4></div><p class="note">{desc}</p></div>
    </div>""")
    parts.append("""
  </div>
  <table>
    <thead><tr><th>选题方向</th><th>推荐样式</th><th>理由</th></tr></thead>
    <tbody>
      <tr><td>食物红黑榜 / 营养对比</td><td class="high">A 3D对比</td><td>对比冲击强，第一眼就懂</td></tr>
      <tr><td>一周食谱 / 每日习惯</td><td class="high">B1 一周计划</td><td>结构清晰，系列化最简单</td></tr>
      <tr><td>节气 / 时令养生</td><td class="med">C 手绘</td><td>文艺感强，符合养生调性</td></tr>
      <tr><td>食材功效科普</td><td class="med">C 手绘</td><td>插画+详解，信息密度适中</td></tr>
    </tbody>
  </table>
  <p class="note"><b>起步优先级</b>：B1 一周计划表（门槛最低、可日更）→ A 3D对比图（收藏率高）→ B2 数字步骤 → C 手绘。
  同一账号内不要混发多种风格。</p>
""")

    # ===== 三、情感鸡汤 =====
    parts.append("""
<section id="emotion">
  <div class="sec-head"><h2>三、情感鸡汤类视频</h2><span class="en">Emotional Healing</span></div>
  <div class="lead">本类是<b>制作门槛全类别最低</b>：不需要 AI 角色/动作，只要 1 段背景循环 + 1 段 TTS + 字幕，剪映模板化即可日更。
  两个账号是同一套生产系统的两种"时间模块"。</div>
""")
    parts.append(account_grid("情感鸡汤类视频"))
    parts.append("""
  <table>
    <thead><tr><th>维度</th><th>路径A：若初情感（深夜陪伴）</th><th>路径B：云朵电台（早安日签）</th></tr></thead>
    <tbody>
      <tr><td>公式</td><td>温柔女声 + 夜景 + 大字情绪文案</td><td>少女声 + 固定街道 + 日期可视化 + 热点</td></tr>
      <tr><td>爆款驱动</td><td>情绪共鸣 → 收藏/转发</td><td>热点/吉语 + 互动指令 → 转发/评论</td></tr>
      <tr><td>黄金发布</td><td>21:00–24:00</td><td>6:00–8:00</td></tr>
      <tr><td>制作难度</td><td>低</td><td>低（热点运营是重点）</td></tr>
    </tbody>
  </table>
  <div class="warn"><h4>通用避坑</h4>
    • 不要露脸（背影/侧影/虚化更有代入感）；音乐不抢戏，人声必须清晰；<br>
    • 同一账号视觉统一（字体/色调/音乐）；路径B必须绑定热点/日历/吉语才破圈；<br>
    • 背景固定不常换（云朵电台同一条街道反复出现）；发布时间固定培养追更。
  </div>
""")

    # ===== 四、玄学命理 =====
    parts.append("""
<section id="meta">
  <div class="sec-head"><h2>四、玄学命理类视频</h2><span class="en">Metaphysics & Fortune</span></div>
  <div class="lead">本类合并「讲解类视频」与「每日运势图文」两条方向。三条路径共用选题库，只换角色与体裁。
  <b>合规是这条赛道的生死线</b>。</div>
""")
    parts.append(account_grid("玄学命理类视频", "玄学命理讲解类"))
    parts.append(f"""
  <div class="two-col" style="margin-top:14px;">
    <div>
      <h4 style="color:#0f2c52;margin-bottom:8px;">C. 每日运势图文（样式参考）</h4>
      <p class="note">固定版式 + 日期模块 + 运势模块（生肖/星座/五行/MBTI）+ 宜避/幸运建议 + 吉语 + 免责声明。
      三类样式：可爱电子黄历 / 水墨传统黄历 / 12生肖运势卡片（量产友好度最高）。同一套模板可多主题轮播。</p>
    </div>
    <div><img src="{b64(STYLE_IMGS['fortune'])}" style="width:100%;border-radius:12px;border:1px solid #e6ebf2;"></div>
  </div>
  <table>
    <thead><tr><th>路径</th><th>来源</th><th>核心公式</th><th>形式</th></tr></thead>
    <tbody>
      <tr><td><b>A 神秘安慰</b></td><td>止语</td><td>AI道长 + 现代情绪痛点 + 祈福弹幕</td><td>视频</td></tr>
      <tr><td><b>B 知识导师</b></td><td>柏言国学安迪师兄</td><td>国学导师 + 生活化选题 + 问句标题 + 双语字幕</td><td>视频</td></tr>
      <tr><td><b>C 每日运势</b></td><td>每日运势图文</td><td>固定版式 + 运势模块 + 对号入座</td><td>图文</td></tr>
    </tbody>
  </table>
  <div class="warn danger"><h4>⚠ 合规红线（通用）</h4>
    • 必须加免责声明：「内容虚构 拒绝迷信 相信科学 无不良引导」；<br>
    • 绝不做个人具体预测（命运/疾病/财运/婚姻）；不碰疾病、投资、法律高危领域；<br>
    • 不用真人/明星形象，角色必须原创 AI；不用恐吓式文案（"不转就倒霉"）；<br>
    • 不在私域/评论区收费算命；调性统一，选定一条主路径再扩展。
  </div>
""")

    # ===== 五、起步优先级 =====
    parts.append("""
<section id="priority">
  <div class="sec-head"><h2>五、跨类别起步优先级</h2><span class="en">Roll-out Priority</span></div>
  <table>
    <thead><tr><th>阶段</th><th>类别 / 路径</th><th>动作</th><th>预期门槛</th><th>关键指标</th></tr></thead>
    <tbody>
      <tr><td><b>第1周</b></td><td>情感鸡汤 A 深夜陪伴</td><td>剪映建模板，写10条文案跑通</td><td class="low">最低</td><td>完播、收藏</td></tr>
      <tr><td><b>第1-2周</b></td><td>健康小贴士 B1 一周计划</td><td>定版式壳，批量换主题</td><td class="low">低</td><td>收藏、转发</td></tr>
      <tr><td><b>第2-3周</b></td><td>AI 萌宠 B 播客 / D 双CP</td><td>即梦生成固定动物 + 配音</td><td class="med">中</td><td>转发率</td></tr>
      <tr><td><b>第3-4周</b></td><td>数字人唱歌 B/C</td><td>原创角色 + 对口型工作流验证</td><td class="med">中</td><td>完播、收藏</td></tr>
      <tr><td><b>第4周+</b></td><td>玄学命理 A 神秘安慰</td><td>原创AI角色 + 黑金模板</td><td class="med">中</td><td>收藏、转发</td></tr>
      <tr><td>进阶</td><td>数字人跳舞带货 / 萌宠E电影感</td><td>动作迁移 / Seedance 旗舰</td><td class="high">高</td><td>加购 / 传播</td></tr>
    </tbody>
  </table>
</section>
""")

    # ===== 六、合规红线 =====
    parts.append("""
<section id="compliance">
  <div class="sec-head"><h2>六、通用合规红线与避坑清单</h2><span class="en">Compliance & Pitfalls</span></div>
  <div class="warn danger"><h4>⚠ 全类别通用红线</h4>
    ① 不搬运原视频：必须换角色、换场景、换BGM、改文案；<br>
    ② AI 生成内容必须标注「内容由 AI 生成」，虚拟人需平台注册、实名；<br>
    ③ 数字人唱歌：歌曲走平台曲库/自翻唱，声音不撞真人，形象原创；<br>
    ④ 玄学命理：免责声明 + 不做个人预测 + 不碰高危领域 + 不收费算命；<br>
    ⑤ 形象必须固定一致，形成账号资产；调性不随意切换。
  </div>
  <table>
    <thead><tr><th>坑</th><th>后果</th><th>解法</th></tr></thead>
    <tbody>
      <tr><td>直接搬运原视频</td><td>被判重/限流/封号</td><td>换角色+换场景+换BGM+改文案</td></tr>
      <tr><td>形象不固定</td><td>观众记不住，无账号资产</td><td>每个路径锁定1-2个固定角色</td></tr>
      <tr><td>纯展示无冲突</td><td>数据扑街</td><td>加吐槽/对比/反转/互动</td></tr>
      <tr><td>调性突然切换</td><td>伤粉</td><td>一个账号先打透一种情绪</td></tr>
      <tr><td>无转发触发点</td><td>只有赞没有转</td><td>"@你那个XX的朋友""是不是你"</td></tr>
      <tr><td>不做AI标识</td><td>平台处罚</td><td>发布勾选「内容由AI生成」</td></tr>
    </tbody>
  </table>
</section>

<footer>
  抖音爆款账号复刻策略汇报 · 数据来源：benchmarks/ 汇总报告与 抖音账号/ 收集截图 · 生成于 2026-08-19<br>
  本报告仅用于内部复刻策略参考，所有对标账号内容版权归原作者所有。
</footer>
</div>
</body>
</html>
""")

    out = "\n".join(parts)
    out_path = os.path.join(BASE, "抖音爆款账号复刻策略汇报.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print("written:", out_path, "size:", len(out), "bytes")

if __name__ == "__main__":
    build()
