#!/bin/bash
# setup.sh - Cài đặt môi trường và tải tool Bacon Bypass

echo "⏳ Đang cập nhật Termux..."
yes | pkg update
yes | pkg upgrade

echo "⏳ Đang cài đặt Python và thư viện..."
yes | pkg install python -y
pip install requests rich

echo "⏳ Đang tải tool Bacon Bypass..."
curl -Ls "https://raw.githubusercontent.com/TEN_GITHUB_CUA_BAN/bacon-bypass-tool/main/bacon_tool.py" -o $HOME/bacon_tool.py

echo "✅ Cài đặt hoàn tất!"
echo "👉 Chạy tool bằng lệnh: python ~/bacon_tool.py <link>"
