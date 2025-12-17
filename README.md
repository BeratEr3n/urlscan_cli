# urlscan_cli

`urlscan_cli`, **urlscan.io** API’sini kullanarak

- URL scan (submit + poll)
- domain / ip / url / hash search

işlemlerini komut satırından veya programatik olarak (MCP / LLM) yapmanı sağlayan bir CLI araçtır.

---

## Features

- URL Scan (submit → poll)
- Domain / IP (IPv4 & IPv6) / URL / Hash search
- Explicit target selection (domain, ip, url, hash)
- API key zorunlu, fail-fast davranış

---

## Installation

### Repo’yu klonla
```bash
git clone https://github.com/BeratEr3n/urlscan_cli.git
cd urlscan_cli
```

### Virtual environment (önerilir)
```bash
python -m venv venv
venv\Scripts\activate
```

### Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```

---

## Configuration

Bu projede:
- API key parametre olarak zorunludur

API key:
https://urlscan.io/user/login/

---

## Usage

```bash
python src/main.py --api-key YOUR_API_KEY <command> [options]
```

API key verilmezse program çalışmaz.

---

## Commands

### URL Scan

```bash
python src/main.py --api-key YOUR_API_KEY scan --url https://example.com
```

Visibility ayarı:
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

URL içinde `&` gibi karakterler varsa tırnak kullanın:
```bash
python src/main.py --api-key YOUR_API_KEY search --url "https://example.com/?a=1&b=2"
```

#### Hash (indirilen dosyalar için)
```bash
python src/main.py --api-key YOUR_API_KEY search --hash <sha256>
```

#### Sonuç limiti
```bash
python src/main.py --api-key YOUR_API_KEY search --domain example.com --limit 20
```

---

## Notes

- urlscan dosya upload veya sandbox desteği sunmaz
- Scan işlemleri yalnızca URL için yapılabilir
- Hash search yalnızca daha önce taranmış sitelerden indirilen dosyalar için geçerlidir
- Search API yoğunluğa bağlı olarak geçici HTTP 503 dönebilir
- Varsayılan search limiti `config/settings.py` üzerinden ayarlanır
- Tool MCP / LLM entegrasyonu için uygundur, insan CLI deneyimi öncelik değildir

---

## License

MIT
