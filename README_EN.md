# urlscan_cli

`urlscan_cli` is a CLI tool that uses the **urlscan.io** API to perform:

- URL scan (submit + poll)
- domain / ip / url / hash search

from the command line or programmatically (MCP / LLM).

---

## Features

- URL Scan (submit → poll)
- Domain / IP (IPv4 & IPv6) / URL / Hash search
- Explicit target selection (domain, ip, url, hash)
- API key required, fail-fast behavior

---

## Installation

### Clone the repository
```bash
git clone https://github.com/BeratEr3n/urlscan_cli.git
cd urlscan_cli
```

### Virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## Configuration

In this project:
- API key is required as a parameter

API key:
https://urlscan.io/user/login/

---

## Usage

```bash
python src/main.py --api-key YOUR_API_KEY <command> [options]
```

The program will not run without an API key.

---

## Commands

### URL Scan

```bash
python src/main.py --api-key YOUR_API_KEY scan --url https://example.com
```

Visibility option:
```bash
python src/main.py --api-key YOUR_API_KEY scan --url https://example.com --visibility unlisted
```

---

### Search

#### Domain
```bash
python src/main.py --api-key YOUR_API_KEY search --domain example.com
```

#### IP (IPv4 / IPv6)
```bash
python src/main.py --api-key YOUR_API_KEY search --ip 1.1.1.1
python src/main.py --api-key YOUR_API_KEY search --ip 2606:4700:4700::1111
```

#### URL
```bash
python src/main.py --api-key YOUR_API_KEY search --url https://example.com
```

If the URL contains characters like `&`, use quotes:
```bash
python src/main.py --api-key YOUR_API_KEY search --url "https://example.com/?a=1&b=2"
```

#### Hash (for downloaded files)
```bash
python src/main.py --api-key YOUR_API_KEY search --hash <sha256>
```

#### Result limit
```bash
python src/main.py --api-key YOUR_API_KEY search --domain example.com --limit 20
```

---

## Notes

- urlscan does not provide file upload or sandbox support
- Scan operations are only available for URLs
- Hash search is only valid for files downloaded from previously scanned sites
- Search API may temporarily return HTTP 503 depending on load
- Default search limit is configured in `config/settings.py`
- The tool is suitable for MCP / LLM integration; human CLI UX is not the priority

---

## License

MIT
