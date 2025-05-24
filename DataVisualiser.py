"""
Name: Jee Eun KIM
ID : 34207147
Generate Date : 10th Oct 2023
Last Updated Date: 22th Oct 2023
Description: This python script is for DataVisualiser class including 3.6, 3.7 functions
"""

from SimpleDataAnalyser import SimpleDataAnalyser 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class DataVisualiser(SimpleDataAnalyser):

    def __init__(self):
        super().__init__()

    # 3.6. Property Value Distribution
    def prop_val_distribution(self, dataframe, suburb="all", target_currency="AUD"):
        """
        This method is responsible for visualising the property values as a histogram so as to easily present to the customers.

        Parameters
        ----------
        dataframe
        suburb : str
        target_currency : str

        """    

        #Given currency exchange rate dictionary.
        currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}
        
        # If the target currency is not in the dictionary, AUD will be used.
        if target_currency not in currency_dict:
            print(f"Target corruncy{target_currency}is not available. AUD will be used for the histogram.")
            target_currency = "AUD"

        # Filtering data based on the given suburb name.
        if suburb == "all":
            filtered_dataframe = dataframe
        else:
            filtered_dataframe = dataframe[dataframe['suburb'].str.lower().str.strip() == suburb.lower().strip()]

        # Notify the user if the filtered DataFrame is empty.
        if filtered_dataframe.empty:
            print(f"{suburb}data is not available. Generating a histogram using data for all suburbs")
            filtered_dataframe = dataframe

        # Exclude records with missing price values.
        filtered_dataframe = filtered_dataframe.dropna(subset=['price'])
        
        # Convert properties values to the target currency.
        exchange_rate = currency_dict[target_currency]
        converted_price = self.currency_exchage(filtered_dataframe,exchange_rate)
    
        # Draw a histogram.
        plt.hist(converted_price, bins=50)
        plt.title(f"{suburb} Properties Value Distribution ({target_currency})")
        plt.xlabel(f"Price({target_currency})")
        plt.ylabel("Frequency")

        # Save a histogram.
        file_name = f"{suburb}_properties_value_distribution_{target_currency}.png"
        plt.savefig(file_name)
        plt.show()

        print(f"The histogram has been saved as {file_name}.")

    # 3.7. Sales Trend
    def sales_trend(self, dataframe):
        """
        This method is to calculate the number of properties sold in each year and visualise the results as a line chart 

        Parameters
        ----------
        dataframe

        """    
        # Convert the 'sold_date' column to datetime format
        dataframe['sold_date'] = pd.to_datetime(dataframe['sold_date'], format='%d/%m/%Y')

        # Group the data by year and calculate the number of properties sold in each year
        sales_per_year = dataframe['sold_date'].dt.year.value_counts()

        years = sales_per_year.index
        counts = sales_per_year.values

        sorted_indices = np.argsort(years)
        sorted_years = years[sorted_indices]
        sorted_counts = counts[sorted_indices]

        # Draw a line chart
        plt.plot(sorted_years, sorted_counts, marker='o')
        plt.title('Yearly Sales Trend')
        plt.xlabel('Year')
        plt.ylabel('Number of Properties Sold')
        plt.grid(True)

        # Save a line chart
        plt.savefig('sales_trend.png')
        plt.show()
