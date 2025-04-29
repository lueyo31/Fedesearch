from urllib.parse import urlparse, parse_qs, urljoin, unquote

def decode_url_from_querystring(url:str) -> str:
        """
        Decodifica una URL codificada en formato query string.
        """
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        encoded_url = query_params.get('url', [None])[0]
        if encoded_url:
            return unquote(encoded_url)  # Decodificar la URL
        return "http://localhost:8000"  # Valor por defecto si no se encuentra la URL