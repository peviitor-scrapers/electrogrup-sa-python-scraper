"""
Job URL Validation Module

Shared validation primitives used by validate_jobs.py and CI workflows.
"""

import re

import requests

HEADERS = {"User-Agent": "job_seeker_ro_spider"}
TIMEOUT = 10

DEFAULT_EXPIRED_KEYWORDS = [
    "not found",
    "no longer accepting",
    "position has been filled",
    "position is no longer",
    "has expired",
    "expired",
    "removed",
    "job is no longer available",
    "this position has been filled",
]


def validate_by_head(url):
    """Returns active/expired/error based on a HEAD request."""
    try:
        res = requests.head(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        if res.ok:
            return {"url": url, "status": "active", "http_status": res.status_code}
        return {"url": url, "status": "expired", "http_status": res.status_code}
    except Exception as err:
        return {"url": url, "status": "error", "error": str(err)}


def validate_by_content(url, keywords=None, timeout=TIMEOUT):
    """Returns active/expired based on page content keywords."""
    keywords = keywords or DEFAULT_EXPIRED_KEYWORDS
    try:
        res = requests.get(url, headers=HEADERS, timeout=timeout)
        if not res.ok:
            return {"url": url, "status": "expired", "http_status": res.status_code}
        body = (res.text or "").lower()
        for kw in keywords:
            if kw.lower() in body:
                return {"url": url, "status": "expired", "http_status": res.status_code}
        return {"url": url, "status": "active", "http_status": res.status_code}
    except Exception as err:
        return {"url": url, "status": "error", "error": str(err)}


def validate_by_browser(url, timeout=30000):
    """Returns active/expired using a real browser (catches JS-based 404s).

    Requires Playwright (python3 -m playwright install chromium).
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"url": url, "status": "error", "error": "playwright not installed"}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            response = page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            body = page.content().lower()
            browser.close()
        if response and not response.ok:
            return {"url": url, "status": "expired", "http_status": response.status}
        for kw in DEFAULT_EXPIRED_KEYWORDS:
            if kw.lower() in body:
                return {"url": url, "status": "expired", "http_status": response.status if response else None}
        return {"url": url, "status": "active", "http_status": response.status if response else None}
    except Exception as err:
        return {"url": url, "status": "error", "error": str(err)}
