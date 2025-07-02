import requests
import pandas as pd
import matplotlib.pyplot as plt
 OpenWeatherMap
api_key = "aee476b8119fd55e4a0e9bbfd2e9fc4e";
city = "Delhi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Extract and visualize
main = data['main']
df = pd.DataFrame(main.items(), columns=['Metric', 'Value'])

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['Metric'], df['Value'], color='skyblue')
plt.title(f"Weather Data for {city}")
plt.ylabel("Values")
plt.show()