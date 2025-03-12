import pandas as pd
from ydata_profiling import ProfileReport

# step 1:Data Exploration with Pandas
#1.Load the Dataset
file='diabetes.csv'
data=pd.read_csv(file)
df=pd.DataFrame(data)
print(df.head())

#2.General Information:
print(df.info())
missing_values=df.isnull().sum()
print(f'\nmissing values in each columns:\n{missing_values[missing_values!=0]}')
zeros=(df=='0').sum()
print(f'\nzero values in each columns:\n{zeros}')
#missing values and zeros in each columns:
zerosandmissing_values = pd.DataFrame({'missing_values': missing_values,'zeros': zeros})

print("\nSummary of missing values and zeros:\n",zerosandmissing_values)

#Descriptive Analysis
print(df.describe())

for column in df.columns:
    print(f"{column}: min = {df[column].min()}, max = {df[column].max()}")
#Step 2: Data Exploration with ydata-profiling
#Generate a Profiling Report:
profile = ProfileReport(df, title='Diabetes Data Profiling Report', explorative = True)
profile.to_file("Diabetes_Report.html")



