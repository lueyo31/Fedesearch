from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from app.common.user_config import params, xng_params

class QueryParamsDTO(BaseModel):
    q: str = Field(params.get("q", ""), description="Search query")  # Campo obligatorio
    page: int = Field(params.get("page", 1), ge=1, description="Page number")  # Debe ser >= 1
    format: Optional[str] = params.get("format", None)
    category: Optional[str] = params.get("category", None)
    language: Optional[str] = params.get("language", None)
    time_range: Optional[str] = params.get("time_range", None)
    safesearch: Optional[int] = params.get("safesearch", None)

class XngParamsDTO(BaseModel):
    q: str = xng_params.get("q", "")  # Required
    categories: Optional[str] = xng_params.get("categories", None)  # Comma-separated list
    engines: Optional[str] = xng_params.get("engines", None)  # Comma-separated list
    language: Optional[str] = xng_params.get("language", None)  # Language code
    page: Optional[int] = xng_params.get("page", 1)  # Default 1
    time_range: Optional[Literal["day", "month", "year"]] = xng_params.get("time_range", None)  # [day, month, year]
    format: Optional[Literal["json", "csv", "rss"]] = xng_params.get("format", None)  # [json, csv, rss]
    results_on_new_tab: Optional[Literal[0, 1]] = xng_params.get("results_on_new_tab", 0)  # [0, 1], default 0
    image_proxy: Optional[bool] = xng_params.get("image_proxy", None)  # [True, False], default from server
    autocomplete: Optional[
        Literal[
            "google", "dbpedia", "duckduckgo", "mwmbl", "startpage", 
            "wikipedia", "stract", "swisscows", "qwant"
        ]
    ] = xng_params.get("autocomplete", None)  # Autocomplete service
    safesearch: Optional[Literal[0, 1, 2]] = xng_params.get("safesearch", None)  # [0, 1, 2], default from search
    theme: Optional[str] = xng_params.get("theme", "simple")  # Default "simple"
    enabled_plugins: Optional[List[str]] = xng_params.get("enabled_plugins", None)  # List of enabled plugins
    disabled_plugins: Optional[List[str]] = xng_params.get("disabled_plugins", None)  # List of disabled plugins
    enabled_engines: Optional[List[str]] = xng_params.get("enabled_engines", None)  # List of enabled engines
    disabled_engines: Optional[List[str]] = xng_params.get("disabled_engines", None)  # List of disabled engines