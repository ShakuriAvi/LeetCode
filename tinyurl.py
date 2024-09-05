'''

12\05\24

535. Encode and Decode TinyURL

Dict

Medium

https://leetcode.com/problems/encode-and-decode-tinyurl/description/

Accepted
258K
Submissions
298.7K
Acceptance Rate
86.4%

Memory
16.47
MB
Beats
76.70%
of users with Python3

Runtime
36
ms
Beats
62.64%
of users with Python3
'''


class Codec:
    url_length = 7
    counter = 0
    encoding = dict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = "http://tinyurl.com/"+str(self.counter) + ("0"*(self.url_length - len(str(self.counter))))
        self.encoding[shortUrl] = longUrl
        self.counter += 1
        return shortUrl


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.encoding:
            return self.encoding[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
    codec = Codec()
    print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))