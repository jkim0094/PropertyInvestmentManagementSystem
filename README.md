# Property Investment Management System

This project is a Python-based data analysis application for a property investment company operating in Melbourne. It provides a text-based interface that allows users to analyze property sales data, convert currencies, generate statistical summaries, and visualize market trends using object-oriented programming.

---

## Features

### 1. Extracting Property Data

* **Method**: `extract_property_info(file_path)`
* Loads property sales data from a CSV file and returns a `pandas.DataFrame`.

### 2. Currency Exchange

* **Method**: `currency_exchange(dataframe, exchange_rate)`
* Converts property prices in AUD to a target currency using the given exchange rate.
* Returns a `NumPy` array of converted values.

### 3. Suburb Property Summary

* **Method**: `suburb_summary(dataframe, suburb)`
* Displays statistical summaries (mean, std, median, min, max) for bedrooms, bathrooms, and parking spaces in a given suburb or across all suburbs.
* If the suburb is not found, displays an appropriate error message.

### 4. Average Land Size

* **Method**: `avg_land_size(dataframe, suburb)`
* Computes and returns the average land size (`m²`) of properties in the selected suburb.
* Ignores invalid or missing data and handles unit inconsistencies.

### 5. Property Value Distribution

* **Method**: `prop_val_distribution(dataframe, suburb, target_currency="AUD")`
* Generates and saves a histogram of property prices (converted into the selected currency).
* Falls back to AUD if the currency is not supported.
* Handles missing values and invalid suburb names gracefully.

### 6. Sales Trend Visualization

* **Method**: `sales_trend(dataframe)`
* Plots and saves a line chart showing the number of properties sold per year based on the dataset.

### 7. Property Search by Price

* **Method**: `locate_price(target_price, dataframe, target_suburb)`
* Sorts property prices in descending order using a reverse insertion sort.
* Performs a recursive binary search to check if a specific price exists in the target suburb.
* Returns a boolean value.

---

## Structure

The system is structured into separate classes, such as:

* `SimpleDataAnalyser`: for data loading and basic analysis
* `DataVisualiser`: for plotting graphs
* `Investor`: for managing the user interface and command logic

All functionality is accessed via a text-based interface through `main.py`.

---

## How to Use

1. Run `main.py` to launch the investor console.
2. Follow the menu to select one of the features.
3. Provide file paths or input parameters as prompted.
4. Visual outputs (e.g., plots) will be saved in the working directory.


