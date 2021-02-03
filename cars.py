import numpy as np
import os.path
import math
import pandas as pd


def clean_up_upper(s):
    ''' For use for user input to convert to uppercase for easy comparison to database'''

    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.upper().strip(punctuation)
    return result


def clean_up_lower(s):
    ''' For use for user input to convert to lowercase for easy comparison to database'''

    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result


def user_input(s):

    inputs = input(s)
    return inputs


def compare(i, j, k):
    ''' For use comparing user input to database '''
    sub_dataframe = j.loc[j[k] == i]
    if len(sub_dataframe > 0):
        return sub_dataframe
    else:
        print("car not in column")

   # j.set_index(i, inplace=True)
 #   if i == j.equals(j[i]):
  #      return all(j.loc[j[i]]) == i
   # for index, row in j.iterrows():
      #  if row['Manufacturer'] == i:
         #   return j

#def new_dataframe(df, column):
    #df1 = df.set_index(column)
    #return df1


""" --------------------------------------"""

input_file = "fuel_and_emissions.csv"
car_dataset = pd.read_csv(input_file, sep=",", usecols=[0, 1, 2, 5, 36, 38], encoding="iso-8859-1")

#print(df_cars.head())

input1 = user_input(print("Please enter the manufacturer of your car"))
#new_dataframe(car_dataset, "Manufacturer")

#df_man = car_dataset[car_dataset.Type == input1]

compare(input1, car_dataset, "Manufacturer")






# Manufacturer = input("Please enter the manufacturer of your car")
# Model = input("Please enter the model of your car")
# Petrol_or_Diesel = input("Is your car petrol or diesel?")
# if Petrol_or_Diesel == "petrol" or "Petrol":
