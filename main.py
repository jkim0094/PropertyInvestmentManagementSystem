"""
Name: Jee Eun KIM
ID : 34207147
Generate Date : 10th Oct 2023
Last Updated Date: 22th Oct 2023
Description: This python script is for Executing and Testing
"""
from SimpleDataAnalyser import SimpleDataAnalyser
from DataVisualiser import DataVisualiser
from Investor import Investor

if __name__ == "__main__":
    investor_app = Investor()
    file_path = "property_information.csv"
    try:
        # Try loading the default file
        investor_app.data_analyser.dataframe = investor_app.data_analyser.extract_property_info(file_path)
        print("Data successfully loaded!")
    except Exception as e:
        # If there's an error, prompt the user for a new file path
        print(f"Error:{e}")
        file_path = input("Please enter the correct path to the property data file: ")
        try:
            investor_app.data_analyser.dataframe = investor_app.data_analyser.extract_property_info(file_path)  
            print("Data successfully loaded!")
        except Exception as e:
            # Exit the program if data loading fails a second time
            print(f"Error:{e}. Unable to load the data. Exiting the program.")
            exit()
    # If data is loaded successfully, run the main application   
    investor_app.run()


   
# 3.2. test   
# t = SimpleDataAnalyser()
# t2 = t.extract_property_info("property_information.csv")
# print(len(t2))
# this should be 118771


# 3.3. test
# t = SimpleDataAnalyser()
# t2 = t.extract_property_info("property_information.csv")
# t3 = t.currency_exchage(t2,1)
# print(t3)
#this should be [965000. 405000. 881000. ...     nan     nan     nan]


# 3.4. test
# t = SimpleDataAnalyser()
# t2 = t.extract_property_info("property_information.csv")
# t4 = t.suburb_summary(t2,"mitcham")
# this should be
#        bedrooms  bathrooms  parking_spaces
# mean   3.127349   1.631886        1.564809
# std    1.585075   1.111867        1.102015
# 50%    3.000000   1.000000        1.000000
# min    1.000000   1.000000        0.000000
# max   30.000000  20.000000       31.000000


#3.5. test
# t = SimpleDataAnalyser()
# t2 = t.extract_property_info("property_information.csv")
# t5 = t.avg_land_size(t2,"mitcham")
# print(t5)
# this should be 595.0235791451387


#3.6. test
# t = DataVisualiser()
# t2 = t.extract_property_info("property_information.csv")
# t6 = t.prop_val_distribution(t2, "mitcham", "KRW")
# The histogram has been saved as mitcham_properties_value_distribution_KRW.png.


#3.7. test
# t = DataVisualiser()
# t2 = t.extract_property_info("property_information.csv")
# t7 = t.sales_trend(t2)
# The histogram has been saved as sales_trend.png.


#3.8. test
# t = SimpleDataAnalyser()
# t2 = t.extract_property_info("property_information.csv")
# t8 = t.locate_price(1177000, t2, "mitcham")
# print(t8)
# this should be True