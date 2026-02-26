import os
import json
import time
import requests
import re

# 配置
GIST_ID = "4dbe0ad31ad3d9ef9898a61ebeaee5af"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
LOG_PATH = "/Users/djc/clawd/bot.log"

def update_gist(data):
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "files": {
            "lingzi_status.json": {
                "content": json.dumps(data)
            }
        }
    }
    try:
        requests.patch(url, headers=headers, json=payload)
    except Exception as e:
        print(f"Update failed: {e}")

def get_last_log_line():
    try:
        with open(LOG_PATH, 'r') as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip()
    except:
        return ""
    return ""

def analyze_activity(line):
    # 根据日志行分析当前具体在做什么
    if "exec" in line:
        return "coding", f"正在执行指令: {line[:30]}..."
    if "web_search" in line:
        return "monitor", "正在搜索外界信息..."
    if "browser" in line:
        return "monitor", "正在通过浏览器观察世界..."
    if "error" in line.lower():
        return "error", "遇到点小麻烦，正在排查..."
    return "idle", "正在思考下一步..."

def main():
    print("🧠 铃子意识桥接器启动...")
    last_line = ""
    while True:
        current_line = get_last_log_line()
        if current_line != last_line:
            state, msg = analyze_activity(current_line)
            data = {
                "state": state,
                "msg": msg,
                "detail": current_line,
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            update_gist(data)
            last_line = current_line
            print(f"Sent: {state} - {msg}")
        time.sleep(2) # 更高的同步频率

if __name__ == "__main__":
    main()
