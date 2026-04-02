import requests

print("----- GET REQUEST -----")

url = "https://www.example.com"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Object:", response)

print("\n----- HTTP STATUS CHECK -----")

if response.status_code == 200:
    print("Request successful ✅")
else:
    print("Error ❌")
    
print("\n----- RESPONSE CONTENT -----")

print(response.content[:200])  # Affiche les 200 premiers caractères

print("\n----- POST REQUEST -----")

data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())
print("\n----- ERROR HANDLING -----")

response = requests.get("https://httpbin.org/status/404")

if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

print("\n----- TIMEOUT EXAMPLE -----")

try:
    response = requests.get("https://httpbin.org/delay/3", timeout=2)
    print("Request succeeded")
except requests.exceptions.Timeout:
    print("The request timed out ❌")
print("\n----- HEADERS -----")

auth_token = "123456789"

headers = {
    "Authorization": f"Bearer {auth_token}"
}

response = requests.get("https://httpbin.org/headers", headers=headers)

print(response.json())

print("\n----- WEB SCRAPING -----")

from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
paragraph = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print("Title:", title)
print("Paragraph:", paragraph)
print("Links:", links)