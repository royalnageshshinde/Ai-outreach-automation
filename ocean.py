import requests
from config import OCEAN_API_KEY


def get_similar_companies(domain):

    print("\n[Stage 1] Ocean.io")

    url = "https://api.ocean.io/v3/search/companies"

    headers = {
        "x-api-token": OCEAN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "size": 5,
        "companiesFilters": {
            "lookalikeDomains": [
                domain
            ]
        },
        "fields": [
            "domain",
            "name",
            "companySize",
            "industries"
        ]
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        companies = []

        for company in data.get("companies", []):

            company_info = company.get("company", {})

            domain_name = company_info.get("domain")

            if domain_name:
                companies.append(domain_name)

        return companies

    except Exception as e:

        print("Ocean Error:", e)
        return []