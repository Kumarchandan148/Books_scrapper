import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/117.0.0.0 Safari/537.36"),
    "Accept-Language": "en-US,en;q=0.9"
}

def rating_to_int(class_list):
    # 'star-rating Three' -> 3
    mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for c in class_list:
        if c in mapping:
            return mapping[c]
    return None

def scrape_books(base_url="http://books.toscrape.com/", max_pages=None, delay=0.8, output_csv="books.csv"):
    url = base_url
    page = 1
    results = []

    while True:
        print(f"Scraping page {page}: {url}")
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Each product is in article.product_pod
        for item in soup.select("article.product_pod"):
            try:
                title_tag = item.h3.a
                title = title_tag["title"].strip() if title_tag and title_tag.has_attr("title") else title_tag.text.strip()

                rel_link = title_tag["href"]
                product_link = urljoin(url, rel_link)

                price_tag = item.select_one("p.price_color")
                price = price_tag.text.strip() if price_tag else "N/A"

                avail_tag = item.select_one("p.instock.availability")
                availability = " ".join(avail_tag.text.split()) if avail_tag else "N/A"

                rating_p = item.select_one("p.star-rating")
                rating = rating_to_int(rating_p.get("class", [])) if rating_p else None

                results.append({
                    "Title": title,
                    "Price": price,
                    "Availability": availability,
                    "Rating": rating,
                    "Link": product_link
                })
            except Exception as e:
                # skip problematic items but continue
                print("   Skipped an item due to:", e)
                continue

        # Find next page link
        next_li = soup.select_one("li.next > a")
        if not next_li:
            break

        next_href = next_li["href"]
        url = urljoin(url, next_href)
        page += 1
        if max_pages and page > max_pages:
            break
        time.sleep(delay)

    # Save to CSV
    if results:
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Title", "Price", "Availability", "Rating", "Link"])
            writer.writeheader()
            writer.writerows(results)
        print(f"\n Saved {len(results)} books to {output_csv}")
    else:
        print("No results scraped.")

    return results

if __name__ == "__main__":
    # Example: set max_pages to 2 during dev to speed up testing
    scraped = scrape_books(max_pages=None, delay=0.6, output_csv="books_all.csv")
    # print first 5
    for i, r in enumerate(scraped[:5], start=1):
        print(f"{i}. {r['Title']} — {r['Price']} — Rating: {r['Rating']}")