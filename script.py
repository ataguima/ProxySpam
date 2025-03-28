import requests
from concurrent.futures import ThreadPoolExecutor

proxy_file = "proxy_file"
target_url = "target_url"

def access_with_proxy(proxy):
    print(f"[+] Trying to access {target_url} with proxy: {proxy}")
    try:
        response = requests.get(target_url, proxies={"http": proxy, "https": proxy}, timeout=3)
        print(f"[+] Success with {proxy}:
{response.text[:200]}")
    except requests.RequestException as e:
        print(f"[-] Failed with {proxy}: {e}")

with open(proxy_file, "r") as file:
    proxies = [line.strip() for line in file if line.strip()]

if proxies:
    with ThreadPoolExecutor(max_workers=10) as executor:
        for proxy in proxies:
            executor.submit(access_with_proxy, proxy)
else:
    print("[!] No proxies loaded.")
