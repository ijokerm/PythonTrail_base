import requests

url = "https://way.jd.com/jisuapi/get?appkey=6816a3395037c07de74a19884f6f2497&channel={{channel}}&num={{num}}&start=0&no=896"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
