"""
Name: Jee Eun KIM
ID : 34207147
Generate Date : 10th Oct 2023
Last Updated Date: 22th Oct 2023
Description: This python script is for SimpleDataAnalyser class including 3.2, 3.3, 3.4, 3.5, 3.8 functions
"""

import pandas as pd
import numpy as np

class SimpleDataAnalyser:
    # Initialize the property_data attribute as None.
    def __init__(self):
        self.dataframe = None
    
    # 3.2.  Extracting Property Information  
    def extract_property_info(self, file_path):
        """
        This method is responsible for reading the property information from the data file.

        Parameters
        ----------
        file_path : str
    
        Returns
        -------
        dataframe

        """        
        self.dataframe = pd.read_csv(file_path)
        return self.dataframe

    # 3.3. Currency Exchange  
    def currency_exchage(self, dataframe, exchage_rate):
        """
        This method is responsible for transforming the property prices in Australian dollars into the target currency according to the exchange rate.

        Parameters
        ----------
        dataframe
        exchage_rate : float
    
        Returns
        -------
        NumPy array of transformed prices

        """        
        convertd_price = dataframe['price'] * exchage_rate
        return convertd_price.to_numpy()

    # 3.4. Suburb Property Summary
    def suburb_summary(self, dataframe, suburb):
        """
        This method is to display the summary of the properties with respect to the number of bedrooms, number of bathrooms and number of parking spaces for a given suburb.

        Parameters
        ----------
        dataframe
        suburb : str

        """ 
        if suburb == "all":
            dataframe = dataframe
        else:
            dataframe = dataframe[dataframe['suburb'].str.lower().str.strip() == suburb.lower().strip()]

        if dataframe.empty:
            print(f"\nThere is no information for'{suburb}'.")
            return
        
        summary = dataframe[['bedrooms','bathrooms','parking_spaces']].describe().loc[['mean','std','50%','min','max']]

        print(summary)


    # 3.5. Average Land Size   
    def avg_land_size(self, dataframe, suburb):
        """
        This method calculates and returns the average land size in 𝑚2 of properties in the suburb.

        Parameters
        ----------
        dataframe
        suburb : str

        Returns
        -------
        average land size in 𝑚2
        
        """ 
        if suburb == "all":
            dataframe = dataframe
        else:
            dataframe = dataframe[dataframe['suburb'].str.lower().str.strip()==suburb.lower().strip()]

        if dataframe.empty:
            return None
        
        dataframe = dataframe[dataframe['land_size']>0]
        # Convert hectares to m^2 for the land size
        dataframe.loc[dataframe['land_size_unit']=='ha','land_size'] = dataframe[dataframe['land_size_unit']=='ha']['land_size']*10000

        average_size = dataframe['land_size'].mean()

        return average_size
 

    # 3.8. Identifying a Property of a Specific Price in a Suburb
    def locate_price(self, target_price, data, target_suburb):
        """
        This method is to find out if a specific target price value is in the list of prices from a specific suburb in.

        Parameters
        ----------
        target_price : float
        data : dataframe
        target_suburb: str

        Returns
        -------
        Bool
        
        """ 
        filtered_data = data[data['suburb'].str.lower().str.strip() == target_suburb.lower().strip()]

        prices = filtered_data['price'].tolist()

        # Sort the prices using insertion sort
        for i in range(1, len(prices)):
            key = prices[i]
            j = i -1
            while j >=0 and key > prices[j]:
                prices[j+1] = prices[j]
                j -= 1
            prices[j+1] = key

        # Binary search to locate the target price
        left = 0
        right = len(prices) -1

        while left <= right :
            mid = (left + right) // 2
            if prices[mid] == target_price:
                return True
            elif prices[mid] > target_price:
                left = mid +1
            else:
                right = mid -1

        return False