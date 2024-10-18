import urllib.request
import requests

# opener = urllib.request.build_opener()
# response = opener.open('http://www.google.com')
# print(response.read())
#
# response = requests.get('https://www.google.com.ua/?hl=uk')
# print(response.content)
# print(response.text)

response = requests.post('https://httpbin.org/post', data="Hello B2114", headers={'Content-Type': 'text/html'})
print(response.text)