class SoupifyException(Exception):
    """Error raised when Soupifying URL page"""

    def __init__(self, url: str):
        self.msg = f"Unable to access or parse URL: {url}"
        super.__init__(self.msg)
