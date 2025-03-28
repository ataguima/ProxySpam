# Iplogger Flood

This script floods Iploggers using proxies. It leverages `requests` for sending requests and `ThreadPoolExecutor` to run multiple tests in parallel, improving efficiency.

## 🔧 Requirements
- Python 3+
- `requests` library

To install the required library:
```bash
pip install requests
```

## 🚀 Usage
1. Edit the script to define the `target_url`.
2. Save your proxy list in the `proxylist.txt` file, one per line.
3. Run the script:
```bash
python script.py
```

## 📁 Project Structure
```
Proxy-Checker/
│-- script.py
│-- proxylist.txt
│-- README.md
```

## ⚠️ Disclaimer
This script is for educational purposes and connectivity testing only. Misuse may violate website and network terms of service.

---
**Author:** ataguima

