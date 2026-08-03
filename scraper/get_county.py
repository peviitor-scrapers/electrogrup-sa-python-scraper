"""
County resolution module.

Maps Romanian cities/localities to their county (equivalent of the Node.js
GetCounty helper used in the based_scraper_py ecosystem).
"""

import unicodedata

COUNTIES = {
    "Alba Iulia": "Alba",
    "Arad": "Arad",
    "Pitesti": "Arges",
    "Bacau": "Bacau",
    "Oradea": "Bihor",
    "Bistrita": "Bistrita-Nasaud",
    "Botosani": "Botosani",
    "Braila": "Braila",
    "Brasov": "Brasov",
    "Bucuresti": "Bucuresti",
    "Buzau": "Buzau",
    "Calarasi": "Calarasi",
    "Resita": "Caras-Severin",
    "Cluj-Napoca": "Cluj",
    "Constanta": "Constanta",
    "Sfantu Gheorghe": "Covasna",
    "Targoviste": "Dambovita",
    "Craiova": "Dolj",
    "Galati": "Galati",
    "Giurgiu": "Giurgiu",
    "Targu Jiu": "Gorj",
    "Miercurea Ciuc": "Harghita",
    "Deva": "Hunedoara",
    "Slobozia": "Ialomita",
    "Iasi": "Iasi",
    "Buftea": "Ilfov",
    "Baia Mare": "Maramures",
    "Drobeta-Turnu Severin": "Mehedinti",
    "Targu-Mures": "Mures",
    "Piatra-Neamt": "Neamt",
    "Slatina": "Olt",
    "Ploiesti": "Prahova",
    "Zalau": "Salaj",
    "Satu Mare": "Satu Mare",
    "Sibiu": "Sibiu",
    "Suceava": "Suceava",
    "Alexandria": "Teleorman",
    "Timisoara": "Timis",
    "Tulcea": "Tulcea",
    "Vaslui": "Vaslui",
    "Ramnicu Valcea": "Valcea",
    "Ramnicu-Valcea": "Valcea",
    "Focsani": "Vrancea",
}

_CITY_ALIASES = {
    "bucuresti": "Bucuresti",
    "bucharest": "Bucuresti",
    "cluj": "Cluj-Napoca",
    "cluj_napoca": "Cluj-Napoca",
    "cluj-napoca": "Cluj-Napoca",
    "targu-mures": "Targu-Mures",
    "targu_mures": "Targu-Mures",
    "timișoara": "Timisoara",
    "timisoara": "Timisoara",
    "iași": "Iasi",
    "iasi": "Iasi",
    "brașov": "Brasov",
    "brasov": "Brasov",
    "constanța": "Constanta",
    "constanta": "Constanta",
    "craioVA": "Craiova",
    "craiova": "Craiova",
    "ploiești": "Ploiesti",
    "ploiesti": "Ploiesti",
    "piatra neamt": "Piatra-Neamt",
    "piatra-neamt": "Piatra-Neamt",
    "râmnicu vâlcea": "Ramnicu Valcea",
    "ramnicu valcea": "Ramnicu Valcea",
}


def _normalize(text):
    return unicodedata.normalize("NFC", text).strip()


def get_county(city):
    """Returns the county for a given city name, or None if not found."""
    if not city:
        return None
    city_norm = _normalize(city)
    canonical = _CITY_ALIASES.get(city_norm.lower(), city_norm)
    return COUNTIES.get(canonical)
