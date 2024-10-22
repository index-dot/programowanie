import requests
from typing import Optional


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: str, country: str,
                 website_url: Optional[str]):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self):
        return (f"Brewery ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Type: {self.brewery_type}\n"
                f"City: {self.city}, State: {self.state}, Country: {self.country}\n"
                f"Website: {self.website_url if self.website_url else 'No website available'}\n")


def fetch_breweries(limit: int = 20):
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return []


def main():
    breweries_data = fetch_breweries(20)

    breweries_list = [
        Brewery(
            id=brewery['id'],
            name=brewery['name'],
            brewery_type=brewery['brewery_type'],
            city=brewery['city'],
            state=brewery['state'],
            country=brewery['country'],
            website_url=brewery.get('website_url')
        )
        for brewery in breweries_data
    ]

    for brewery in breweries_list:
        print(brewery)
        print("-" * 40)


if __name__ == "__main__":
    main()
