import pandas as pd

country = pd.read_csv('~/Documents/Uni/FIT3179/Git/Assignment2/data/JoinedData4.csv', on_bad_lines='skip')
country.columns = ['Country', 'Score', 'Band', 'Colony','Lat', 'Long', 'Country Code', 'Rank', 'Number of Tourists']
business = pd.read_csv('~/Documents/Uni/FIT3179/Git/Assignment2/data/%TourismToGDP.csv', on_bad_lines='skip')
business.columns = ['Country', 'Tourism Contribution to GDP (%)']


data = pd.merge(country, business, on='Country')
data.to_csv('JoinedData5.csv')