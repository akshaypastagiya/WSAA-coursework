
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url,verify=False)
data = response.json()
print(data['northern-ireland']['events'][0])