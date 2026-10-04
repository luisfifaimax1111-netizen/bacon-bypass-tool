import requests
import sys
import json
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# --- CẤU HÌNH ---
API_KEY = "YOUR_API_KEY_HERE"  # Thay bằng API key của bạn
API_ENDPOINT = "API_ENDPOINT_HERE"  # Thay bằng endpoint thực tế

def bypass_link(locked_url):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"url": locked_url}
    
    try:
        with console.status("[bold green]Đang bypass link..."):
            response = requests.post(API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            
            bypassed_url = data.get("result") or data.get("destination") or data.get("bypassed_url")
            
            if bypassed_url:
                console.print(f"[bold green]✅ Link đã bypass:[/bold green] {bypassed_url}")
                return bypassed_url
            else:
                console.print("[bold red]❌ Không tìm thấy link trong response.[/bold red]")
                console.print(json.dumps(data, indent=2))
                return None
                
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]❌ Lỗi request:[/bold red] {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        console.print("[yellow]Cách dùng:[/yellow] python bacon_tool.py <link_bị_khóa>")
        sys.exit(1)
    
    link = sys.argv[1]
    console.print(f"[cyan]⏳ Đang xử lý:[/cyan] {link}")
    bypass_link(link)
