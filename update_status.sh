#!/bin/bash
# 铃子空间状态更新脚本
# 用于在铃子执行不同任务时更新页面显示
# 作者: 铃子

set -e

GIST_ID="4dbe0ad31ad3d9ef9898a61ebeaee5af"
STATE_FILE="/tmp/lingzi_status_update.json"

# 状态定义
# idle: 雅室 - 思考/闲置
# coding: 案头 - 编程/写代码
# monitoring: 瞭望台 - 监控/盯盘
# error: 机房 - 错误/Debug

STATE="${1:-idle}"
MSG="${2:-铃子正在...}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# 创建状态 JSON
cat > "$STATE_FILE" << EOF
{
  "state": "$STATE",
  "msg": "$MSG",
  "updated_at": "$TIMESTAMP"
}
EOF

# 更新 Gist
gh gist edit "$GIST_ID" -f lingzi_status.json < "$STATE_FILE" > /dev/null 2>&1

echo "✅ 状态已更新: $STATE - $MSG"
