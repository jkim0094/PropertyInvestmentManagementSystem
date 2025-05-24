"""
Name: Jee Eun KIM
ID : 34207147
Generate Date : 10th Oct 2023
Last Updated Date: 22th Oct 2023
Description: This python script is for Investor class including display_menu, run functions
"""

from SimpleDataAnalyser import SimpleDataAnalyser
from DataVisualiser import DataVisualiser

class Investor:
    def __init__(self):
        self.data_analyser = SimpleDataAnalyser()
        self.data_visualiser = DataVisualiser()

    def display_menu(self):
        while True:
            print("\n========== Investor App Menu ==========")
            print("1. Suburb Property Summary")
            print("2. Average Land Size")
            print("3. Property Value Distribution")
            print("4. Sales Trend")
            print("5. Locate Property By Price")
            print("0. Exit")
            choice = input("Enter your choice(0 ~ 5): ")

            # Check if the choice is numeric and in the range 0-5
            if choice.isdigit() and 0 <= int(choice) <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number 0 ~ 5.")

    
    def run(self):
        while True:
            choice = self.display_menu()
            if choice == "0":
                print("Exit the program")
                break
            elif choice == "1": 
                print("========== 1. Suburb Property Summary ==========")
                suburb = input("Enter suburb(or 'all'): ")
                self.data_analyser.suburb_summary(self.data_analyser.dataframe, suburb)
            elif choice == "2":
                print("========== 2. Average Land Size ==========")
                suburb = input("Enter suburb(or 'all'): ")
                size = self.data_analyser.avg_land_size(self.data_analyser.dataframe, suburb)
                print(f"Average land size in {suburb}: {size}m^2")

            elif choice == "3":
                print("========== 3. Property Value Distribution ==========")
                suburb = input("Enter suburb(or 'all'): ")
                currency = input("Enter the target currency (AUD, USD, INR, etc.): ").upper()
                self.data_visualiser.prop_val_distribution(self.data_analyser.dataframe, suburb, currency)

            elif choice == "4":
                print("========== 4. Sales Trend ==========")
                self.data_visualiser.sales_trend(self.data_analyser.dataframe)

            elif choice == "5":
                print("========== 5. Locate Property By Price ==========")
                target_suburb = input("Enter suburb: ")
                while True:
                    try:
                        target_price = float(input("Enter price: "))
                        break
                    except ValueError:
                        print("Please enter a valid numeric price.")

                found = self.data_analyser.locate_price(target_price, self.data_analyser.dataframe, target_suburb)
                if found:
                    print(f"{target_price} property is available in {target_suburb}")
                else:
                    print(f"No property is available at {target_price} in {target_suburb}.")
    
    