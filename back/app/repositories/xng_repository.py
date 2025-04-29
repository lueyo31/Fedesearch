import requests
from abc import ABC, abstractmethod
from app.common.config import SEARCH_API_URL
from app.models.page_model import Page
from app.repositories.mapper.page_repository_mapper import PageXNGMapper
from app.schemas.params_schema import QueryParamsDTO
from bs4 import BeautifulSoup
from datetime import datetime
from app.models.result_model import Result
from urllib.parse import urljoin

from app.common.utils.extract_query_url import decode_url_from_querystring


class IXngRepository(ABC):
    @abstractmethod
    def search(self, params: QueryParamsDTO) -> Page:
        pass

    @abstractmethod
    def search_images(self, params: QueryParamsDTO) -> Page:
        pass

    @abstractmethod
    def search_videos(self, params: QueryParamsDTO) -> Page:
        pass

    @abstractmethod
    def search_news(self, params: QueryParamsDTO) -> Page:
        pass


class XngRepository(IXngRepository):
    def __init__(self):
        self.base_url = SEARCH_API_URL

    def search(self, params: QueryParamsDTO) -> Page:
        print("XngRepository.search called with params:", params.dict())
        try:
            request_params = {
                "q": params.q,
                "format": params.format or "json",
                "pageno": params.page,
                "category": params.category,
                "language": params.language,
                "time_range": params.time_range,
                "safesearch": params.safesearch,
            }
            request_params = {k: v for k, v in request_params.items() if v is not None}
            print(f"{self.base_url}/search", request_params)

            response = requests.get(f"{self.base_url}/search", params=request_params)
            print("Response status code:", response.status_code)

            if response.status_code == 503:
                raise ValueError("API service unavailable (503)")

            if response.status_code == 404:
                raise ValueError("API endpoint not found (404)")
            response.raise_for_status()

            if "application/json" not in response.headers.get("Content-Type", ""):
                print("Non-JSON response received:", response.text[:500])
                raise ValueError(
                    "Expected JSON response but received HTML or other content"
                )

            data = response.json()
            print("Parsed JSON data:", data)
            return PageXNGMapper.map_searx_page(data, params)
        except requests.exceptions.RequestException as e:
            print("RequestException:", e)
            raise ValueError(f"Error during search request: {e}")
        except ValueError as e:
            print("ValueError:", e)
            raise ValueError(f"Invalid response: {e}")

    def search_images(self, params: QueryParamsDTO) -> Page:
        print("XngRepository.search_images called with params:", params.dict())
        try:
            data = {
                "q": params.q,
                "categories": "images",
                "language": params.language,
                "time_range": params.time_range,
                "safesearch": params.safesearch,
                "theme": "simple",  # Default theme
            }
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            response = requests.post(
                f"{self.base_url}/search", data=data, headers=headers
            )
            print("Response status code:", response.status_code)
            response.raise_for_status()

            if not response.text.strip():
                raise ValueError("Empty response from search service")

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract engine name
            engine_tag = soup.find("p", class_="result-engine")
            engine = engine_tag.text.split(":")[-1].strip() if engine_tag else "unknown"

            # Parse image results into a searx_data dictionary
            results = []
            for idx, item in enumerate(
                soup.find_all("article", class_="result-images"), start=1
            ):
                img_tag = item.find("img", class_="image_thumbnail")
                link_tag = item.find("a", class_="result-images-source")
                title_tag = item.find("span", class_="title")
                source_tag = item.find("span", class_="source")

                if not img_tag or not link_tag:
                    continue

                results.append(
                    {
                        "thumbnail": urljoin(self.base_url, link_tag["href"]),
                        "url": decode_url_from_querystring(urljoin(self.base_url, img_tag["src"])),
                        "title": title_tag.text if title_tag else "Image result",
                        "content": source_tag.text if source_tag else "",
                        "engine": engine,
                    }
                )

            # Extract pagination links
            next_page_tag = soup.find("form", class_="next_page")
            next_url = (
                urljoin(self.base_url, next_page_tag["action"])
                if next_page_tag
                else None
            )

            searx_data = {
                "results": results,
                "pagination": {
                    "current": params.page,
                    "next": next_url,
                    "previous": None,  # Adjust if previous page logic is needed
                },
            }

            # Use the mapper to convert searx_data to a Page object
            return PageXNGMapper.map_searx_page(searx_data, params)
        except requests.exceptions.RequestException as e:
            print("RequestException:", e)
            raise ValueError(f"Error during search request: {e}")
        except Exception as e:
            print("Exception:", e)
            raise ValueError(f"Error parsing search results: {e}")

    def search_videos(self, params: QueryParamsDTO) -> Page:
        print("XngRepository.search_videos called with params:", params.dict())
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "null",
                "DNT": "1",
                "Sec-GPC": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Priority": "u=0, i",
            }

            data = {
                "q": params.q,
                "category_videos": "1",
                "pageno": params.page,
                "language": params.language,
                "time_range": params.time_range or "",
                "safesearch": params.safesearch,
                "format": params.format or "json",
            }
            print(f"{self.base_url}/search",headers, data)

            response = requests.post(self.base_url, headers=headers, data=data)
            print("Response status code:", response.status_code)

            response.raise_for_status()

            if "application/json" not in response.headers.get("Content-Type", ""):
                print("Non-JSON response received:", response.text[:500])
                raise ValueError("Expected JSON response but received non-JSON content")

            data = response.json()
            print("Parsed JSON data:", data)

            # Usa el mapper para convertir los datos en un objeto Page
            return PageXNGMapper.map_searx_page(data, params)
        except requests.exceptions.RequestException as e:
            print("RequestException:", e)
            raise ValueError(f"Error during video search request: {e}")
        except Exception as e:
            print("Exception:", e)
            raise ValueError(f"Error parsing video search results: {e}")

    def search_news(self, params: QueryParamsDTO) -> Page:
        print("XngRepository.search_news called with params:", params.dict())
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "null",
                "DNT": "1",
                "Sec-GPC": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Priority": "u=0, i",
            }

            data = {
                "q": params.q,
                "category_news": "1",
                "pageno": params.page,
                "language": params.language,
                "time_range": params.time_range or "",
                "safesearch": params.safesearch,
                "format": params.format or "json",
            }

            response = requests.post(self.base_url, headers=headers, data=data)
            print("Response status code:", response.status_code)

            response.raise_for_status()

            if "application/json" not in response.headers.get("Content-Type", ""):
                print("Non-JSON response received:", response.text[:500])
                raise ValueError("Expected JSON response but received non-JSON content")

            data = response.json()
            print("Parsed JSON data:", data)

            # Use the mapper to convert the data into a Page object
            return PageXNGMapper.map_searx_page(data, params)
        except requests.exceptions.RequestException as e:
            print("RequestException:", e)
            raise ValueError(f"Error during news search request: {e}")
        except Exception as e:
            print("Exception:", e)
            raise ValueError(f"Error parsing news search results: {e}")
