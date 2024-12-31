from data_collection.instagram_scraper import scrape_instagram_public
from data_collection.facebook_scraper import scrape_facebook_public
from data_collection.linkedin_scraper import scrape_linkedin_public
from data_collection.google_search import scrape_google_reviews
from data_collection.reviews_scraper import scrape_google_reviews, scrape_local_ch_reviews
from data_collection.website_scraper import scrape_website_metrics

def main():
    print("Welcome to Online Presence Report (Public)!")
    print("Press Enter to skip a section if you don't have the input.")
    
    data = ""

    # Instagram scraping
    instagram_username = input("Enter the Instagram username: ")
    if instagram_username:
        instagram_data = scrape_instagram_public(instagram_username)
        data += "\n--- Instagram Data ---\n" + str(instagram_data) + "\n"

    # Facebook scraping
    facebook_page_name = input("Enter the Facebook page name: ")
    if facebook_page_name:
        facebook_data = scrape_facebook_public(facebook_page_name)
        data += "\n--- Facebook Data ---\n" + str(facebook_data) + "\n"

    # LinkedIn scraping
    linkedin_url = input("Enter the LinkedIn profile URL: ")
    if linkedin_url:
        linkedin_data = scrape_linkedin_public(linkedin_url)
        data += "\n--- LinkedIn Data ---\n" + str(linkedin_data) + "\n"

    # Google search scraping
    search_query = input("Enter the Google search query: ")
    if search_query:
        google_results = scrape_google_search(search_query)
        data += "\n--- Google Search Results ---\n"
        for result in google_results:
            data += f"Position: {result['position']}\n"
            data += f"Title: {result['title']}\n"
            data += f"URL: {result['url']}\n"
            data += f"Description: {result['description']}\n\n"

    # Website scraping
    website_url = input("Enter the company website URL: ")
    domain = website_url.replace("https://", "").replace("http://", "").split('/')[0] if website_url else None
    if website_url and domain:
        website_data = scrape_website_metrics(domain, website_url)
        data += "\n--- Website Data ---\n" + str(website_data) + "\n"

    # Google reviews scraping
    google_review_url = input("Enter the Google Reviews URL: ")
    if google_review_url:
        google_reviews = scrape_google_reviews(google_review_url)
        data += "\n--- Google Reviews ---\n" + str(google_reviews) + "\n"

    # Local.ch reviews scraping
    local_ch_url = input("Enter the Local.ch Reviews URL: ")
    if local_ch_url:
        local_reviews = scrape_local_ch_reviews(local_ch_url)
        data += "\n--- Local.ch Reviews ---\n" + str(local_reviews) + "\n"

    # Save data to file
    with open("output/public_data.txt", "w") as f:
        f.write(data)

    print("Scraping complete. Data saved to output/public_data.txt.")

if __name__ == "__main__":
    main()
