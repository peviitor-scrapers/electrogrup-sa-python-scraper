# ELECTROGRUP SA — Python Scraper

Scraper Python pentru joburile ELECTROGRUP SA, publicate în [peviitor.ro](https://peviitor.ro)
prin API-ul v1 (`api.peviitor.ro/v1`).

## Structură

```
.
├── scraper/                    # codul scraperului
│   ├── index.py                # punctul de intrare (python scraper/index.py)
│   ├── api.py                  # client API peviitor v1 (firme/jobs)
│   ├── anaf.py                 # validare companie via ANAF + fallback CUIScan
│   ├── company.py              # logica de validare/pregătire companie
│   ├── job_validator.py        # validare URL-uri de job (head/content)
│   ├── validate_jobs.py        # CLI: python -m scraper.validate_jobs
│   ├── get_county.py           # oraș → județ
│   ├── markdown_generator.py   # generață docs/jobs.md
│   └── config/                 # sursa unică de adevăr (company.json, scraper.json)
├── ai/                         # documentație pentru agenți AI
├── tests/
│   ├── unit/                   # teste unitare (mock HTTP)
│   ├── integration/            # teste live (skip dacă rețeaua lipsește)
│   ├── e2e/                    # scrape real al board-ului
│   └── consistency/            # identitate repo, workflow-uri, root files
├── docs/
│   ├── index.html              # GitHub Pages
│   ├── jobs.md                 # lista joburilor scrape-ate
│   └── company.json            # copie a configului companiei
└── .github/workflows/          # CI/CD
```

## Rulare

```bash
python3 -m pip install -r requirements.txt
python3 -m scraper.index
```

## Testare

```bash
python3 -m pytest tests/unit tests/consistency
python3 -m pytest tests/e2e          # necesită acces la board
```

## Configurație

- `scraper/config/company.json` — CIF, nume, brand, locații, `scraperFile`
- `scraper/config/scraper.json` — API base, path, department filter

## Publicare

Scraperul publică prin API-ul v1 peviitor (`/v1/firme/company/add/`, `/v1/scraper/jobs/upload/`),
eliminând joburile stale prin `/v1/scraper/jobs/delete/`.
