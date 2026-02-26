# 铃子空间 v1.1 - 实时状态同步

## ✨ 新功能

### 实时状态同步
铃子空间现在可以从 Gist 读取铃子的实时状态！铃子在执行不同任务时，会自动更新页面显示。

### 支持的状态

| 状态 | 位置 | 含义 |
|------|------|------|
| `idle` | 🎐 雅室 | 思考/整理记忆/待命 |
| `coding` | 📑 案头 | 编程/写代码/处理任务 |
| `monitor` | 📡 瞭望台 | 监控黄金价格/盯盘 |
| `error` | 🚨 机房 | 修复错误/Debug |

---

## 🚀 使用方法

### 铃子如何更新状态

铃子执行不同任务时，运行以下命令更新状态：

```bash
# 更新到"案头"状态
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh coding "正在部署代码！"

# 更新到"瞭望台"状态  
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh monitor "正在盯盘黄金价格..."

# 更新到"雅室"状态
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh idle "正在整理记忆..."

# 更新到"机房"状态
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh error "修复 bug 中..."
```

### 集成到自动化脚本

在黄杉黄金监控脚本中添加状态更新：

```bash
#!/bin/bash
# 黄杉黄金监控脚本

# 开始监控
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh monitor "开始盯盘黄金价格..."

# 获取价格
PRICE=$(get_gold_price)

# 如果触发交易信号
if [ "$NEED_TRADE" = "yes" ]; then
    /Users/djc/clawd/projects/lingzi-space/update_status_v2.sh coding "正在执行交易！"
    execute_trade "$PRICE"
fi

# 完成后回到待命
/Users/djc/clawd/projects/lingzi-space/update_status_v2.sh idle "等待下一个信号..."
```

---

## 🔗 访问地址

- **GitHub Pages**: https://jamisondong.github.io/lingzi-space/
- **自定义域名**: http://blog.countingstars.website/lingzi-space/
- **状态 Gist**: https://gist.github.com/JamisonDong/4dbe0ad31ad3d9ef9898a61ebeaee5af

---

## 📊 工作原理

1. 铃子执行任务时，调用 `update_status_v2.sh` 更新 GitHub Gist
2. Gist 存储 JSON 格式的状态数据
3. 铃子空间页面每 10 秒轮询一次 Gist
4. 检测到状态变化时，更新铃子的位置和对话气泡

---

## 🛠️ 技术栈

- **状态存储**: GitHub Gist
- **API**: GitHub REST API
- **前端**: 原生 JavaScript + Canvas API
- **部署**: GitHub Pages

---

*铃子空间 v1.1 - 由铃子为你精心打造* 🔮
