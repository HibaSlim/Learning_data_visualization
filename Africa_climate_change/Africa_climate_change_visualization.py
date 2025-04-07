import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1- Load the dataset
data = pd.read_csv('Africa_climate_changes.csv')
print(data.head())
print(data.describe())
print(data.info())
#2- Clean the data as needed.
# missing values
print('missingvalues:',data.isnull().sum())

print('fill the missing values with the interpolate() methode \nthe precipitation, max temp, min temp are more likely to be affected by the values after or below the missing one')
data['TAVG'] = data['TAVG'].interpolate()
data['PRCP'] = data['PRCP'].interpolate()
data['TMAX'] = data['TMAX'].interpolate()
data['TMIN'] = data['TMIN'].interpolate()
#check if there is no more missing values
print('missingvalues :',data.isnull().sum())
print('there is 2 missing value in PRCP so they are either in the first or last rows of our table \nthe interpolate() estimates missing values based on the values before and after the missing data\nwe will print the headt and the tail of our data:\n')
print(data.head())
print(data.tail())
data['PRCP'] = data['PRCP'].interpolate()
# Convert date column to datetime format if necessary
data['DATE'] = pd.to_datetime(data['DATE'])
data['year'] = data['DATE'].dt.year
data['month']= data['DATE'].dt.month
data['day']= data['DATE'].dt.day
data.drop(columns=['DATE'], inplace=True)

#3-Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
# df for Tunisia and Cameroon
df = data[data['COUNTRY'].isin(['Tunisia', 'Cameroon'])]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='TAVG', hue='COUNTRY')
plt.title('Average Temperature in Tunisia and Cameroon (1980-2023)')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.legend(title='COUNTRY')
plt.grid()
plt.show()


#4-Zoom in to only include data between 1980 and 2005, try to customize the axes labels.
print('there is a screenshot included')

#5-Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure). Describe the obtained results.

senegal_data = data[data['COUNTRY'] == 'Senegal']

senegal1980_2000 = senegal_data[(senegal_data['year'] >= 1980) & (senegal_data['year']<= 2000)]
senegal2000_2023 = senegal_data[(senegal_data['year'] > 2000) & (senegal_data['year']<= 2023)]
#hystogram with plotly
plt.figure(figsize=(10, 6))
plt.hist(senegal1980_2000['TAVG'], bins=20, alpha=0.5, label='1980-2000')
plt.hist(senegal2000_2023['TAVG'], bins=20, alpha=0.5, label='2000-2023')
plt.title('Temperature Distribution in Senegal (1980-2000) and (2000-2023)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
"""

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.histplot(senegal_1980_2000['TAVG'], bins=20, kde=True)
plt.title('Temperature Distribution in Senegal (1980-2000)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(senegal_2000_2023['TAVG'], bins=20, kde=True)
plt.title('Temperature Distribution in Senegal (2000-2023)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()"""

print('the average temperature have almost the same frequency but slightly colder ')
#6-Select the best chart to show the Average temperature per country.
#check TAVG per country
tavg_country = data.groupby('COUNTRY')['TAVG'].mean()

plt.figure(figsize=(10, 6))
tavg_country.plot(kind='bar')
plt.title('average temperature by country')
plt.xlabel('COUNTRY')
plt.legend()
plt.show()
#7-Make your own questions about the dataset and try to answer them using the appropriate visuals.