import requests
from bs4 import BeautifulSoup

def scrape_google_reviews(business_url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(business_url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to access Google reviews."

        soup = BeautifulSoup(response.text, "html.parser")
        overall_rating = soup.find("div", class_="gm2-display-2").text.strip() if soup.find("div", class_="gm2-display-2") else "No overall rating available"
        num_reviews = soup.find("span", class_="gm2-caption").text.strip() if soup.find("span", class_="gm2-caption") else "No review count available"

        return {"overall_rating": overall_rating, "num_reviews": num_reviews}
    except Exception as e:
        return f"Error scraping Google reviews: {e}"
