# codethedream
Pre-work application
# Countries Explorer 🌍

## Overview

Countries Explorer is a Python command-line tool that retrieves and analyzes country information from the [countries.dev API](https://countries.dev/docs).

The tool allows users to explore countries around the world and learn about their population, geographic area, region, languages, capital city, and other available information.

## API Used

- **API:** [countries.dev](https://countries.dev/docs)
- **Base Endpoint:** `https://countries.dev/countries`
- **Purpose:** Retrieve country data for searching, filtering, and comparing countries.
- **Data Format:** JSON

The application uses the countries.dev API to retrieve country information instead of maintaining its own database.

## Features

The tool is designed to support the following features:

- **List countries:** Display countries returned by the API.
- **Filter by region:** Find countries belonging to a specific region.
- **Largest country:** Identify the country with the largest geographic area.
- **Most populous country:** Find the country with the highest population.
- **Compare countries:** Compare two countries using available information, such as population, area, capital city, and languages.

*Note: The available features depend on the functionality implemented in the Python script and the fields returned by the API.*


## Installation

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Install the required dependency:

```bash
pip install requests
```

## How to Run

Run the Python script from your terminal:

```bash
python main.py
```

If your script has a different filename, replace `main.py` with the appropriate filename.

Follow the on-screen instructions to explore country data, if an interactive menu is implemented.

## Example API Request

The following Python example retrieves country data from the API:

```python
import requests

url = "https://countries.dev/countries"

response = requests.get(url, timeout=10)
response.raise_for_status()

countries = response.json()

print(countries)
```

This example sends an HTTP GET request to the API, checks for HTTP errors, and prints the JSON response.



## Project Purpose

This project demonstrates how to work with a public REST API in Python, process JSON data, and build a command-line application for exploring and comparing countries.


