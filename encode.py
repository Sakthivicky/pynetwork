import urllib.parse

url="Hello ! guys this is sakthi & Xmen"
encoded=urllib.parse.quote(url)
print(encoded)

decode=urllib.parse.unquote(encoded)
print(decode)
