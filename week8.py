#data collection
import pandas as pd

# Load the data
df = pd.read_csv("owid-covid-data.csv")

# Display the shape and first few rows
print(df.shape)
df.head()

#data exploration

# View column names
df.columns

# Check for missing values
df.isnull().sum()

# Basic info
df.info()

# Summary statistics
df.describe()

#data cleaning
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter selected countries
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Drop rows with critical missing values
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Fill remaining missing values (if needed)
df.fillna(0, inplace=True)

#total cases over time
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()
#death rate comparison
df['death_rate'] = df['total_deaths'] / df['total_cases']

#cumulative vacations over time
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_vaccinations'], label=country)
plt.title("Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.show()

#Choropleth Map
import plotly.express as px

latest_data = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest_data,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Global COVID-19 Case Distribution")
fig.show()
