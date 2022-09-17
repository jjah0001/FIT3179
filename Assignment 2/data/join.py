import pandas as pd
proficiency = pd.read_csv('~/Documents/Uni/FIT3179/CSV_Files/EnglishProficiency.csv')
print(proficiency)
country = pd.read_csv('~/Documents/Uni/FIT3179/CSV_Files/world_country_and_usa_states_latitude_and_longitude_values.csv', on_bad_lines='skip')
print(country)
proficiency.columns = ['Country', 'Score', 'Band', 'Colony']
country.columns = ['Lat', 'Long', 'Country']
print(len(proficiency))
print(len(country))

data = pd.merge(proficiency, country, on='Country')
data.to_csv('Proficiency_with_long_lat')