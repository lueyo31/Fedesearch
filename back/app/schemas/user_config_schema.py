from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ParamsDTO(BaseModel):
    q: Optional[str] = None
    page: Optional[int] = None
    format: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    time_range: Optional[str] = None
    safesearch: Optional[int] = None

class XngParamsDTO(BaseModel):
    q: Optional[str] = None
    categories: Optional[str] = None
    engines: Optional[str] = None
    language: Optional[str] = None
    page: Optional[int] = None
    time_range: Optional[str] = None
    format: Optional[str] = None
    results_on_new_tab: Optional[int] = None
    image_proxy: Optional[bool] = None
    autocomplete: Optional[bool] = None
    safesearch: Optional[int] = None
    theme: Optional[str] = None
    enabled_plugins: Optional[List[str]] = None
    disabled_plugins: Optional[List[str]] = None
    enabled_engines: Optional[List[str]] = None
    disabled_engines: Optional[List[str]] = None

class UserConfigDTO(BaseModel):
    params: Optional[Dict[str, Any]] = None  # Allow arbitrary fields in params
    xng_params: Optional[Dict[str, Any]] = None  # Allow arbitrary fields in xng_params
