import pandas as pd

country_data = pd.read_csv("country.csv")

val_a_code = country_data['value_a_code']
val_b_code = country_data['value_b_code']
dom_a_code = country_data['domain_b_code']

#1 ABW - ABW
#print(country_data[country_data['value_a_code'] == val_b_code])

#2 263
#dupl_country = (val_b_code.duplicated())
#print(dupl_country.sum())

#3 928
#unique = (~val_b_code.duplicated())
#print(unique.sum())