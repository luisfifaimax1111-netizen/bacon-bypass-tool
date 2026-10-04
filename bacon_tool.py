import requests
import sys
import json

# --- CẤU HÌNH ---
API_KEY = "Bacon-f4ff0e1de0a9a1e6461f-51474074a48cbebc96f4"      # Thay bằng API key của bạn
API_ENDPOINT = "API_ENDPOINT_HERE"  # Thay bằng endpoint thực tế

def bypass_link(locked_url):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"url": locked_url}
    
    try:
        print(f"⏳ Đang bypass: {locked_url}")
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        bypassed_url = data.get("result") or data.get("destination") or data.get("bypassed_url")
        
        if bypassed_url:
            print(f"✅ Link đã bypass: {bypassed_url}")
            return bypassed_url
        else:
            print("❌ Không tìm thấy link trong response.")
            print(json.dumps(data, indent=2))
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi request: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Cách dùng: python bacon_tool.py <link_bị_khóa>")
        sys.exit(1)
    
    link = sys.argv[1]
    bypass_link(link)
