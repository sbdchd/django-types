from http import cookies

SimpleCookie = cookies.SimpleCookie[str]

def parse_cookie(cookie: str) -> dict[str, str]: ...
