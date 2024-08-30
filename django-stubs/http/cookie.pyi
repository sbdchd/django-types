from http import cookies

SimpleCookie = cookies.SimpleCookie

def parse_cookie(cookie: str) -> dict[str, str]: ...
