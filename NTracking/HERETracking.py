import requests

def get_location(phone_number, api_key):
    base_url = "https://geocoder.ls.hereapi.com/6.2/geocode.json"
    
    params = {
        "searchtext": phone_number,
        "apiKey": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and "Response" in data and "View" in data["Response"]:
        location = data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Label"]
        return f"Standort: {location}"
    else:
        return "Fehler bei der Abfrage des Standorts"

# Beispielnummer und HERE API-Schlüssel (ersetze diese durch deine eigenen Werte)
phone_number = "+497666857193"
here_api_key = ""

result = get_location(phone_number, here_api_key)
print(result)
