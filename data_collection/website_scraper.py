from bs4 import BeautifulSoup
import requests

# Scrape website content and headings
def scrape_website_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Error: Unable to access {url}"
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract paragraphs
        paragraphs = soup.find_all('p')
        text_content = "\n".join([p.get_text(strip=True) for p in paragraphs[:10]])  # Limit to first 10 paragraphs

        # Extract headings
        headings = {
            "h1": [h.get_text(strip=True) for h in soup.find_all('h1')],
            "h2": [h.get_text(strip=True) for h in soup.find_all('h2')],
            "h3": [h.get_text(strip=True) for h in soup.find_all('h3')],
        }

        return {"url": url, "content": text_content, "headings": headings}
    except Exception as e:
        return f"Error scraping website content: {e}"

# Fetch technology stack (BuiltWith API)
def fetch_website_tech(domain):
    try:
        api_key = "YOUR_BUILTWITH_API_KEY"  # Replace with your BuiltWith API key
        url = f"https://api.builtwith.com/v18/api.json?KEY={api_key}&LOOKUP={domain}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Unable to fetch technology stack for {domain}"
    except Exception as e:
        return f"Error fetching technology stack: {e}"

# Scrape traffic metrics (SimilarWeb)
def scrape_similarweb_traffic(domain):
    try:
        url = f"https://www.similarweb.com/website/{domain}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape traffic and global rank
        traffic = soup.find('span', class_='engagementInfo-valueNumber').text.strip()
        rank = soup.find('div', class_='globalRank-value').text.strip()
        
        return {"monthly_visits": traffic, "global_rank": rank}
    except Exception as e:
        return f"Error scraping traffic metrics: {e}"

# Fetch SEO data (Semrush API)
def fetch_seo_data(domain):
    try:
        api_key = "YOUR_SEMRUSH_API_KEY"  # Replace with your Semrush API key
        url = f"https://api.semrush.com/?type=domain_ranks&key={api_key}&domain={domain}&database=us"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text  # Customize as needed to extract data
        else:
            return f"Error: Unable to fetch SEO data for {domain}"
    except Exception as e:
        return f"Error fetching SEO data: {e}"

# Unified website scraper
def scrape_website_metrics(domain, website_url):
    try:
        results = {}

        # Scrape website content and headings
        content_data = scrape_website_content(website_url)
        results["content"] = content_data["content"] if "content" in content_data else content_data
        results["headings"] = content_data["headings"] if "headings" in content_data else {}

        # Fetch technology stack
        tech_data = fetch_website_tech(domain)
        results["tech_stack"] = tech_data

        # Scrape traffic metrics
        traffic_data = scrape_similarweb_traffic(domain)
        results["traffic"] = traffic_data

        # Fetch SEO data
        seo_data = fetch_seo_data(domain)
        results["seo"] = seo_data

        return results
    except Exception as e:
        return f"Error scraping website metrics: {e}"
