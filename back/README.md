
example petition
http://192.168.1.106:8080/search?q=machine+learning&format=json&pageno=2&category=science&language=es-ES&time_range=month
http://192.168.1.106:8080/search?q=machine+learning&format=json&category=images&language=es-ES&time_range=day&safesearch=2
http://192.168.1.106:8080/search?q=machine+learning&format=json&category=videos&language=es-ES&time_range=day&safesearch=2


```bash
 1393  poetry add fastapi[standard]
 1397  poetry run uvicorn main:app --reload
```



search image es tipo post
```bash
curl 'http://192.168.1.106:8080/search' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Accept-Encoding: gzip, deflate' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: null' -H 'DNT: 1' -H 'Sec-GPC: 1' -H 'Connection: keep-alive' -H 'Cookie: session=.eJyFkVuPokAUhP_KhudBm7uYmI0XkEVQlpuXF9JAIyigdjciTua_r4bdZN727atKpXJS55OJrghXsEY1ZcYUN-iDgQ3N_3FyqbPiyIw_mbi8JGdmzDAfPUa0oCX6bjS47GVyaWqKu16UsD5GRU0RzmCCvnkEQZzkvVG_uKcrRhnbN-WUXsfDIafyA04eDbgBB-SxBAAY_nynEEZ1gsikWSr72a9Za8S3dnQTrWNgJS0vWH523zgsu_RnXgDl3HaR6zgL9dZpxXwh8c-lLfFrsrmaFOBWx3RfYXpb22c_PBElm4MIL34H-GkR45kbqe7J3cl-aAvfnFrOjjxu0o0-Mtfopvtns3HcJfIsxQttM6juiGgIzfVYMxQM_V2mm9ep7bCiZ6WehiQ5OHHCJiyN-y7v-CfZz1eVsslwq9JZ7d2JcBSVLKUuX0LF6TxF5eVq6-2Ukk8iMSerNGtm7WTyWovQrkRRdUmLrEBpvyCNyV_IUfUePIX4_JL_G5X5-mDOqHv_-kf8Sh4Ed7XdhV641OE-kEyomw-XW1dhVZ7dU3rwOLWxQbqFxsFecznvaTZwBb0NfTB5dzVN8b5ISKDKAQ6yGUIqK0JOZEd8DFiZ4yFSY1GNAWS-_gAwTMt_.Z3MH8Q.pBsRfy-CKryHADnMZN7UQueu4_Y' -H 'Upgrade-Insecure-Requests: 1' -H 'Priority: u=0, i' --data-raw 'q=machine+learning&categories=images&language=es-ES&time_range=&safesearch=0&theme=simple'
```
```python
import requests
from bs4 import BeautifulSoup

# Realiza la búsqueda en el frontend
url = "http://192.168.1.106:8080/search?q=machine+learning&category=images"
response = requests.get(url)

# Parsea el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra todas las imágenes
images = soup.find_all('img')
for img in images:
    print(img['src'])  # URL de la imagen
```

interface
```python
# page_service.py
from typing import List

class SearchServiceInterface(ABC):
    
    @abstractmethod
    def search(self, q: str) -> List[str]:
        pass

class PageService(SearchServiceInterface):
    def search(self, q: str) -> List[str]:
        # Simulación de búsqueda
        return [f"Resultado para {query} 1", f"Resultado para {query} 2", f"Resultado para {query} 3"]

# web_search_use_case.py
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from page_service import SearchServiceInterface, PageService

def get_search_service() -> SearchServiceInterface:
    return PageService()

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest, search_service: SearchServiceInterface = Depends(get_search_service)):
    try:
        results = search_service.search(request.query)
        return SearchResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        ```