import requests
from bs4 import BeautifulSoup

def scrape_facebook_public(page_name):
    try:
        url = f"https://www.facebook.com/{page_name}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to access Facebook page for {page_name}."

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.text if soup.title else "Title not available."
        description = soup.find('meta', attrs={"name": "description"})['content'] if soup.find('meta', attrs={"name": "description"}) else "Description not available."

        # Scrape Recent Posts
        post_texts = []
        posts = soup.find_all('div', class_='userContentWrapper', limit=5)  # Limit to 5 posts
        for post in posts:
            post_texts.append(post.get_text(strip=True))

        return {"page_name": page_name, "title": title, "description": description, "posts": post_texts}
    except Exception as e:
        return f"Error scraping Facebook: {e}"
