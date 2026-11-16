
import requests
import pandas as pd

# Explore data 

## API configuration
url = "https://countries.dev/countries"

## Get data from API
response = requests.get(url)
data = response.json()

## 1. Check the top-level data type
print("1.What type of data is it:")
print(f"The data is a {type(data).__name__}")

## 2. Display fields and first five records
df = pd.DataFrame(data)

print("\n2. Fields in the records:")
print(df.columns.tolist())

print("\nFirst five countries:")
print(df.head())

## 3. Check for nested dictionaries and lists
print("\n3. Nested fields:")

nested_fields = set()

for record in data:
    for field, value in record.items():
        if isinstance(value, (dict, list)):
            nested_fields.add((field, type(value).__name__))

if nested_fields:
    for field, value_type in sorted(nested_fields):
        print(f'Column "{field}" contains a {value_type}')
else:
    print("No nested dictionaries or lists found.")

## 4. Check for missing and null values
print("\n4. Missing and null values:")

for column in df.columns:
    missing = sum(column not in record for record in data)
    null = sum(
        column in record and record[column] is None
        for record in data
    )

    if missing > 0:
        print(f'Missing data in column "{column}": {missing}')

    if null > 0:
        print(f'Null data in column "{column}": {null}')


#Project 

# Country Explorer
#
# A user runs the Country Explorer program and is prompted to enter
# a country name or type 'quit' to exit.
#
# The program fetches country data from the countries.dev API and
# allows the user to search by entering a full or partial country name.
#
# If a matching country is found, the program displays its flag,
# name, capital, region, population, area, languages, and currencies.
#
# If multiple countries match, the program displays all matching
# names and asks the user to be more specific.
#
# If the user enters an empty search or no countries match,
# the program displays a helpful message.
#
# The program also handles connection errors, unsuccessful API
# responses, and invalid JSON data without crashing.
#
# When the user types 'quit', the program displays a goodbye message
# and exits.
#
# Data source: https://countries.dev/countries

API_URL = "https://countries.dev/countries"


def get_countries():
    """Download the country list. Returns None if something goes wrong."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # raises an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException:
        print("Could not load the country data. Check your internet and try again.")
        return None
    except ValueError:
        print("The server sent data we could not read.")
        return None


def find_countries(countries, text):
    """Return every country whose name contains the text."""
    matches = []
    for country in countries:
        if text.lower() in country.get("name", "").lower():
            matches.append(country)
    return matches


def show_country(country):
    """Print the details of one country. .get() gives a default if a field is missing."""
    names_of_languages = []
    for language in country.get("languages", []):
        names_of_languages.append(language["name"])

    names_of_currencies = []
    for currency in country.get("currencies", []):
        names_of_currencies.append(currency["name"])

    print(country.get("flag", ""), country.get("name", "Unknown"))
    print("  Capital:   ", country.get("capital", "N/A"))
    print("  Region:    ", country.get("region", "N/A"))
    print("  Population:", country.get("population", "N/A"))
    print("  Area (km²):", country.get("area", "N/A"))
    print("  Languages: ", ", ".join(names_of_languages) or "N/A")
    print("  Currencies:", ", ".join(names_of_currencies) or "N/A")


def main():
    countries = get_countries()
    if countries is None:
        return  # stop the program, the error was already printed

    while True:
        text = input("\nCountry name (or 'quit'): ").strip()

        if text.lower() == "quit":
            print("Goodbye!")
            break

        if text == "":
            print("Please type a country name.")
            continue

        matches = find_countries(countries, text)

        if len(matches) == 0:
            print("No countries found matching", text)
        elif len(matches) == 1:
            show_country(matches[0])
        else:
            print("Several matches, please be more specific:")
            for country in matches:
                print("  -", country["name"])


main()
