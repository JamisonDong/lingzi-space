# 铃子空间 (Lingzi Space) - 部署指南

## 🌐 当前预览

铃子空间现在已经在本地运行了！

**访问地址**:
- 本地访问: `http://localhost:8888/lingzi/index.html`
- 局域网访问: `http://[你的本地IP]:8888/lingzi/index.html`

## 🚀 GitHub Pages 部署（推荐）

### 步骤 1: 创建 GitHub 仓库

在 GitHub 上创建一个新仓库:
1. 访问 https://github.com/new
2. 仓库名称: `lingzi-space`
3. 设置为 **Public**
4. 点击 "Create repository"

### 步骤 2: 本地初始化和推送

```bash
cd /Users/djc/clawd/projects/lingzi-space

# 初始化 Git
git init
git add .
git commit -m "Initial commit: 铃子空间 1.0"

# 添加远程仓库（替换成你的 GitHub URL）
git remote add origin https://github.com/jamisondong/lingzi-space.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 访问你的仓库: https://github.com/jamisondong/lingzi-space/settings/pages
2. 在 "Source" 下选择:
   - Branch: `main`
   - Folder: `/root`（或选择 `/`）
3. 点击 "Save"

等待 1-2 分钟，你的铃子空间就会上线了！

**最终访问地址**: https://jamisondong.github.io/lingzi-space/

---

## 🎮 铃子空间功能

### 当前版本 1.0
- ✅ 四个房间区域（雅室、案头、瞭望台、机房）
- ✅ 北京天气同步（晴朗/3°C）
- ✅ 座右铭展示
- ✅ 铃子角色动态位置
- ✅ 对话气泡系统

### 计划功能 v1.1
- 🔄 实时状态同步（连接 OpenClaw API）
- 📊 黄杉黄金价格监控集成
- 🌤️ 动态天气效果（雨/雪动画）
- 🎵 背景音乐/音效
- 📱 移动端适配

---

## 🛠️ 本地开发

### 启动开发服务器

```bash
cd /Users/djc/clawd/projects/lingzi-space/public
python3 -m http.server 8888 --bind 0.0.0.0
```

访问: http://localhost:8888/

### 停止服务器

按 `Ctrl+C` 停止服务器

---

## 📁 项目结构

```
lingzi-space/
├── public/
│   ├── index.html          # 主页面
│   └── lingzi/             # 铃子空间页面
│       └── index.html      # 铃子空间 v1.0
├── scripts/
│   ├── browser_login.sh   # Polymarket 登录
│   ├── browser_fetch_market.sh  # 市场数据抓取
│   └── browser_verify_data.sh   # 数据验证
├── README.md              # 项目说明
└── DEPLOYMENT.md          # 部署指南（本文件）
```

---

## 🎨 自定义配置

### 修改座右铭

编辑 `public/lingzi/index.html`，找到:
```html
<div class="motto-banner">没有人是一座孤岛，每个人都是陆地的一部分。</div>
```

修改为你喜欢的座右铭。

### 修改房间颜色

找到房间定义部分:
```javascript
// 雅室 (闲置/思考区)
ctx.fillStyle = '#d8bfd8'; // 修改这个颜色代码
```

### 修改铃子的座右铭

找到底部区域:
```javascript
<div style="margin-top:10px; color:#bdc3c7; font-size:12px;">
    "慧雅于心，美紫于行；万物皆有回响，而我，是你的回音。"
</div>
```

---

## 🔗 相关链接

- **OpenClaw 文档**: https://docs.openclaw.ai
- **Counting Stars**: https://countingstars.website
- **GitHub**: https://github.com/jamisondong

---

## 📞 支持

如果有问题，在 `#golden-ideas` 频道直接@铃子！

---

*铃子空间 1.0 - 由铃子为你精心打造* 🔮
