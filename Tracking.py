import phonenumbers
from phonenumbers import geocoder

def get_location(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        location = geocoder.description_for_number(parsed_number, "tr")  # Hier "de" für deutsche Ausgabe - Ändere dies entsprechend für andere Sprachen
        country = geocoder.country_name_for_number(parsed_number, "en")  # "en" für englische Ländernamen - Ändere dies entsprechend für andere Sprachen
        return f"Standort: {location}, Land: {country}"
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return f"Fehler beim Parsen der Telefonnummer: {e}"

# Beispielnummer
phone_number = "+491234567890"  # Ersetze dies durch deine Telefonnummer

result = get_location(phone_number)
print(result)