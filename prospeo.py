import requests
from config import PROSPEO_API_KEY


def get_contacts(companies):

    print("\n[Stage 2] Prospeo")

    contacts = []

    for company in companies:

        try:

            url = "https://api.prospeo.io/search-person"

            headers = {
                "X-KEY": PROSPEO_API_KEY,
                "Content-Type": "application/json"
            }

            payload = {
                "page": 1,
                "filters": {
                    "company": {
                        "websites": {
                            "include": [company]
                        }
                    }
                }
            }

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            data = response.json()

            results = data.get("results", [])

            if len(results) > 0:

                person = results[0].get("person", {})

                contacts.append({
                    "company": company,
                    "name": person.get("full_name", "Unknown"),
                    "email": person.get("email", {}).get("email", "Not Available")
                })

            else:

                contacts.append({
                    "company": company,
                    "name": "No Contact Found",
                    "email": "Not Available"
                })

        except Exception:

            contacts.append({
                "company": company,
                "name": "API Error",
                "email": "Not Available"
            })

    return contacts