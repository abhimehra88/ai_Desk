import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


class WebSearch:

    @staticmethod
    def search(query, max_results=5):

        try:
            # DuckDuckGo HTML search
            url = f"https://html.duckduckgo.com/html/?q={quote(query)}"

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0.0.0 Safari/537.36"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            results = []

            # DuckDuckGo result blocks
            for result in soup.select(".result")[:max_results]:

                title_elem = result.select_one(".result__title a")
                snippet_elem = result.select_one(".result__snippet")

                if not title_elem:
                    continue

                title = title_elem.get_text(strip=True)
                link = title_elem.get("href", "")
                snippet = (
                    snippet_elem.get_text(strip=True)
                    if snippet_elem else ""
                )

                results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet
                })

            return {
                "success": True,
                "query": query,
                "results": results
            }

        except Exception as error:

            return {
                "success": False,
                "query": query,
                "error": str(error),
                "results": []
            }