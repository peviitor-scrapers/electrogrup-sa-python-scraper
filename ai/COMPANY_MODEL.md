# Company Model

Company document published to the peviitor company core (`/v1/firme/company/`).

## Source of truth

`scraper/config/company.json` — never edit other copies; they are generated.

## Fields

| Field        | Type   | Description                                                        |
|--------------|--------|--------------------------------------------------------------------|
| `id`         | string | CIF as-is from ANAF (no RO prefix); zero-padded to 8 digits by `scraper/api.py` when calling the peviitor API |
| `company`    | string | Legal name from Trade Register (UPPERCASE, diacritics required)    |
| `brand`      | string | Public brand name                                                  |
| `group`      | string | Parent company group (optional)                                    |
| `status`     | string | `activ` / `suspendat` / `inactiv` / `radiat`                       |
| `location`   | array  | Romanian cities/addresses (diacritics accepted)                    |
| `website`    | array  | Company website (canonical HTTP/HTTPS URL)                         |
| `career`     | array  | Careers/board URL (canonical HTTP/HTTPS URL)                       |
| `lastScraped`| string | Date of last scrape (ISO 8601)                                     |
| `scraperFile`| string | GitHub Actions workflow URL (no raw)                               |

## Notes

- Fields marked `array` are multi-valued arrays stored as arrays in SOLR.
- `status = "activ"` means jobs are kept; otherwise jobs are removed.
- `website` and `career` should be canonical URLs without a trailing slash.
- `scraperFile` must be the full workflow URL, not the raw file URL.

## Upsert behavior

`upsert_company` zero-pads the CIF to 8 digits (`pad_cif`, because the
peviitor API requires exactly 8 digits) and PUTs to `/v1/firme/company/add/`.
The live address/location from ANAF (CUIScan) takes precedence over the
static config when available.

## Example

```json
{
  "id": "9256208",
  "company": "ELECTROGRUP SA",
  "brand": "ELECTROGRUP",
  "status": "activ",
  "location": ["Cluj-Napoca"],
  "website": ["https://electrogrup.ro"],
  "career": ["https://electrogrup.applytojob.com/apply/jobs/"],
  "scraperFile": "https://github.com/peviitor-scrapers/electrogrup-sa-python-scraper/actions/workflows/job-seeker-ro-spider.yml"
}
```
