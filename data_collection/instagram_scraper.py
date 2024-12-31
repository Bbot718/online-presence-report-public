import requests
from bs4 import BeautifulSoup

def scrape_instagram_public(username):
    try:
        url = f"https://www.instagram.com/{username}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to access Instagram profile for {username}."

        soup = BeautifulSoup(response.text, 'html.parser')

        bio = soup.find('meta', property='og:description')['content'] if soup.find('meta', property='og:description') else "Bio not available."
        profile_pic = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else "Profile picture not available."

        # Extract Post Count
        scripts = soup.find_all('script', type='text/javascript')
        post_count = None
        for script in scripts:
            if 'edge_owner_to_timeline_media' in script.text:
                try:
                    start_idx = script.text.index('edge_owner_to_timeline_media') + len('edge_owner_to_timeline_media')
                    post_count = int(script.text[start_idx:].split(':')[1].split(',')[0])
                except:
                    post_count = "Unknown"

        return {"username": username, "bio": bio, "profile_picture": profile_pic, "post_count": post_count}
    except Exception as e:
        return f"Error scraping Instagram: {e}"
