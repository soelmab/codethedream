
# Country Explorer 🌍

## Description

Country Explorer is a Python command-line program that allows users to search for information about countries around the world.

The program retrieves live country data from an API and allows users to search for a country by entering its full or partial name.

For each matching country, the program displays useful information, including:
- Country name and flag
- Capital city
- Region
- Population
- Area (km²)
- Languages
- Currencies

If multiple countries match the search, the program displays their names and asks the user to enter a more specific search.

## API Used

**API:** Countries.dev

**API URL:** https://countries.dev/countries

The program uses the `requests` library to retrieve country data from the API.

It processes the JSON response and uses the following fields:
- `name` – Country name
- `flag` – Country flag
- `capital` – Capital city
- `region` – Geographic region
- `population` – Number of people living in the country
- `area` – Country area in square kilometers
- `languages` – Languages spoken in the country
- `currencies` – Currencies used in the country

The program also uses nested data for languages and currencies.

## Requirements

Make sure Python is installed on your computer.

Install the required Python libraries:

```bash
pip install requests pandas
```

## How to Run

1. Download or clone the project.
2. Open the project folder in your terminal or code editor.
3. Make sure the required libraries are installed.
4. Run the Python file:

```bash
python country_explorer.py
```

5. Enter a country name when prompted.

## Example

```text
Country name (or 'quit'): Germany

🇩🇪 Germany
  Capital:    Berlin
  Region:     Europe
  Population: 83240525
  Area (km²): 357114
  Languages:  German
  Currencies: Euro

Country name (or 'quit'): quit

Goodbye!
```


## Error Handling

The program includes error handling to prevent unexpected crashes.

- **Connection errors:** Displays a message if the API cannot be reached.
- **HTTP errors:** Handles unsuccessful responses from the server.
- **Invalid JSON:** Displays an error if the returned data cannot be read.
- **Empty input:** Asks the user to enter a country name.
- **No matching results:** Informs the user when no countries match the search.


## Project Structure

The program is organized into separate functions:

- `get_countries()` – Retrieves country data from the API.
- `find_countries()` – Searches for countries using full or partial names.
- `show_country()` – Displays country information in a readable format.
- `main()` – Controls the program and handles user interaction.

## Exit the Program

Type `quit` at any time when prompted to exit the program.

---

**Data Source:** https://countries.dev/countries
