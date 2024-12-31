import requests
from bs4 import BeautifulSoup

def scrape_linkedin_public(profile_url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(profile_url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to access LinkedIn profile at {profile_url}."

        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Name not available."
        headline = soup.find('h2').get_text(strip=True) if soup.find('h2') else "Headline not available."

        return {"profile_url": profile_url, "name": name, "headline": headline}
    except Exception as e:
        return f"Error scraping LinkedIn: {e}"
