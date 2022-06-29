class Codec:
    
    def __init__(self):
        self.url_dict ={}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter+=1
        short = f"http://tinyurl.com/{self.counter}"
        self.url_dict[short]=longUrl
        
        return short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))