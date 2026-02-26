#!/bin/bash
# 铃子空间状态更新脚本 v2
# 使用 GitHub API 直接更新 Gist
# 作者: 铃子

set -e

GIST_ID="4dbe0ad31ad3d9ef9898a61ebeaee5af"
TOKEN="${GITHUB_TOKEN:-$(gh auth token)}"
STATE="${1:-idle}"
MSG="${2:-铃子正在...}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# 获取当前 Gist 内容以获取 SHA
CURRENT_DATA=$(curl -s -H "Authorization: token $TOKEN" \
  "https://api.github.com/gists/$GIST_ID")

FILE_SHA=$(echo "$CURRENT_DATA" | grep -o '"sha": "[^"]*"' | head -1 | cut -d'"' -f4)

# 更新 Gist
UPDATE_DATA=$(cat << EOF
{
  "description": "Lingzi Space Real-time Status",
  "files": {
    "lingzi_status.json": {
      "content": "$(cat << INNER_EOF
{
  "state": "$STATE",
  "msg": "$MSG",
  "updated_at": "$TIMESTAMP"
}
INNER_EOF
)"
    }
  }
}
EOF
)

curl -s -X PATCH \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$UPDATE_DATA" \
  "https://api.github.com/gists/$GIST_ID" > /dev/null

echo "✅ 状态已更新: $STATE - $MSG"
