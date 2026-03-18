import requests
from bs4 import BeautifulSoup


def scrape_website(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"Error: Unable to fetch website (Status {response.status_code})"

        soup = BeautifulSoup(response.text, "html.parser")

        # 🔥 Extract only meaningful paragraph text
        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        if not text.strip():
            return "Error: No readable content found"

        return text

    except Exception as e:
        return f"Error: {str(e)}"