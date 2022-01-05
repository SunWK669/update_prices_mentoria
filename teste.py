import requests
import json

url = "https://api-v1.zoom.com.br/restql/run-query/sherlock/serp_items/1"

querystring = {"tenant":"DEFAULT"}

payload = {
    "query": "iphone 12",
    "order": "default",
    "pagination": {
        "hitsPerPage": 36,
        "page": 0
    },
    "refinements": [],
    "enableCategorySuggestion": True,
    "disableRefinementsStats": False,
    "userId": "25eec1f6-0521-41e7-a790-f85852a0e35b",
    "origin": {
        "brand": "zoom",
        "view": "search_page",
        "device": "desktop",
        "traffic": "users"
    }
}
headers = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
x = json.loads(response.content)

print(response.text)