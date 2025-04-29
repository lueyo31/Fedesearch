from fastapi import APIRouter, Depends, Query, HTTPException
from app.common.ioc import get_web_search_use_case, get_full_search_use_case
from app.services.usecases.web_search_use_case import WebSearchUseCase
from app.services.usecases.full_search_use_case import FullSearchUseCase
from app.schemas.params_schema import QueryParamsDTO
from app.schemas.page_schema import PageDTO  # Added import
import asyncio  # Added for timeout handling

router = APIRouter()

@router.get(
    "",
    summary="Search for results",
    description="Performs a search based on the provided query parameters.",
    response_description="A single page of search results.",
    response_model=PageDTO,  # Specify the response model
)
async def search(
    q: str = Query(..., description="Search query string", example="example query"),
    page: int = Query(1, description="Page number (default: 1)", example=1),
    format: str = Query(None, description="Format of the results (e.g., json, rss)", example="json"),
    category: str = Query(None, description="Category of the search (e.g., web, images, videos)", example="web"),
    language: str = Query(None, description="Language of the search results", example="es"),
    time_range: str = Query(None, description="Time range for the search (e.g., day, week, month)"),
    safesearch: int = Query(None, description="Safe search filter (0: off, 1: moderate, 2: strict)", example=0),
    use_case: WebSearchUseCase = Depends(get_web_search_use_case),
):
    """
    Perform a search using the provided query parameters.
    """
    try:
        params = QueryParamsDTO(
            q=q,
            page=page,
            format=format,
            category=category,
            language=language,
            time_range=time_range,
            safesearch=safesearch,
        )
        print("search_router.search called with params:", params.dict())
        result: PageDTO = use_case.exec(params)  # Removed await
        print("PageDTO object returned from use case:", result)
        return result  # Return a PageDTO
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Search operation timed out")  # Gateway Timeout
    except ValueError as e:
        if "503" in str(e):
            raise HTTPException(status_code=503, detail="Search API service unavailable")  # Service Unavailable
        if "404" in str(e):
            raise HTTPException(status_code=404, detail="Search API endpoint not found")  # Not Found
        raise HTTPException(status_code=400, detail=str(e))  # Bad Request
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Internal Server Error

@router.get(
    "/all",
    summary="Perform a full search",
    description="Fetches all results across multiple pages based on the provided query parameters.",
    response_description="A list of all search results across pages.",
    response_model=list[PageDTO],  # Specify the response model
)
async def full_search(
    q: str = Query(..., description="Search query string", example="example query"),
    page: int = Query(1, description="Starting page number (default: 1)", example=1),
    format: str = Query(None, description="Format of the results (e.g., json, rss)", example="json"),
    category: str = Query(None, description="Category of the search (e.g., general, images)", example="general"),
    language: str = Query(None, description="Language of the search results", example="en"),
    time_range: str = Query(None, description="Time range for the search (e.g., day, week, month)", example="week"),
    safesearch: int = Query(None, description="Safe search filter (0: off, 1: moderate, 2: strict)", example=1),
    use_case: FullSearchUseCase = Depends(get_full_search_use_case),
):
    """
    Perform a full search across multiple pages using the provided query parameters.
    """
    try:
        params = QueryParamsDTO(
            q=q,
            page=page,
            format=format,
            category=category,
            language=language,
            time_range=time_range,
            safesearch=safesearch,
        )
        print("search_router.full_search called with params:", params.dict())
        result = use_case.exec(params)  # Removed await
        return [PageDTO.from_page(page) for page in result]  # Return a list of PageDTOs
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Full search operation timed out")  # Gateway Timeout
    except ValueError as e:
        if "503" in str(e):
            raise HTTPException(status_code=503, detail="Search API service unavailable")  # Service Unavailable
        if "404" in str(e):
            raise HTTPException(status_code=404, detail="Search API endpoint not found")  # Not Found
        raise HTTPException(status_code=400, detail=str(e))  # Bad Request
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Internal Server Error
