# Thanks, cyberstart moon base l03c03
# You aren't limited to using raw sockets to make network connections.
# Python can make HTTP requests quite easily.

# First you'll need to import the necessary urllib modules.
import urllib.request, urllib.error, urllib.parse

# Then you need to open the URL:
response = urllib.request.urlopen("http://127.0.0.1:8080")

# Now you just need to read the contents of the response:
html = response.read()
print(html)

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.

conn = urllib.request.urlopen("http://127.0.0.1:8080/winning")
print(conn.read())
