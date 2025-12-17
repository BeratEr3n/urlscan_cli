# urlscan_cli

`urlscan_cli` is a command-line tool that uses the **urlscan.io** API to perform:  
- URL scanning (submit + poll)  
- domain / IP / URL / hash searches  

directly from the terminal.

---

## 🚀 Features

- **URL Scan** (submit → poll → parse)
- Domain / IP (IPv4 & IPv6) / URL / Hash **Search**
- Automatic target type detection (`--target`)
- Safe query generation against Elasticsearch syntax errors

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/BeratEr3n/urlscan_cli.git
cd urlscan_cli
```

### 2. Virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### Create a `.env` file
```bash
copy .env.example .env
```

### `.env` content
```env
URLSCAN_API_KEY=YOUR_API_KEY_HERE
```

> API key: https://urlscan.io/user/login/

---

## ▶️ Usage

```bash
python src/main.py <command> [options]
```

---

## 🧪 Commands

### 🔹 URL Scan

```bash
python src/main.py scan --url https://example.com
```

#### Set visibility
```bash
python src/main.py scan --url https://example.com --visibility unlisted
```

---

### 🔹 Search

#### Auto-detect (recommended)
```bash
python src/main.py search --target example.com
python src/main.py search --target https://example.com
python src/main.py search --target 8.8.8.8
python src/main.py search --target 2606:4700:4700::1111
```

> ⚠️ If the URL contains characters like `&`, **wrap it in quotes**
```bash
python src/main.py search --target "https://example.com/?a=1&b=2"
```

---

#### Domain
```bash
python src/main.py search --domain example.com
```

#### IP (IPv4 / IPv6)
```bash
python src/main.py search --ip 1.1.1.1
python src/main.py search --ip 2606:4700:4700::1111
```

#### URL
```bash
python src/main.py search --url https://example.com
```

#### Hash (downloaded files only)
```bash
python src/main.py search --hash <sha256>
```

#### Result limit
```bash
python src/main.py search --target example.com --limit 20
```

---

## 🛠 Notes

- urlscan does **not** support file uploads or sandbox execution  
- Scan operations are available **only for URLs**
- Hash search works only for **files downloaded during previous scans**
- The Search API may temporarily return **HTTP 503** due to high load
- Default search limit can be configured in `settings.py`
- The parser layer is intentionally minimal and can be extended later

---

## 📄 License

MIT
