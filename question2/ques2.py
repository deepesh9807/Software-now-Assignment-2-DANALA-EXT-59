import pandas as pd
import glob # import glob to find files and pattern
import os # import os to work file paths

folder_path = "question2/temperatures" # Folder containing CSV files

all_files = glob.glob(os.path.join(folder_path, "*.csv")) # List of all CSV files

df_list = [] # List to hold all data frames

for file in all_files:
    df = pd.read_csv(file) # Read each CSV file
    df_list.append(df) # Add data frame to list

data = pd.concat(df_list, ignore_index=True) # Combine all data frames

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    data[month] = pd.to_numeric(data[month], errors='coerce') # Convert month columns to num

# +++++++++ 1.Seasonal Average +++++++++ #
# Define Australian seasons
seasons = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}           

seasonal_avg = {}
for season, months_list in seasons.items():
    seasonal_avg[season] = data[months_list].stack().mean(skipna=True)

with open("question2/average_temp.txt", "w") as f:
    for season, avg in seasonal_avg.items():
        f.write(f"{season}: {avg:.2f}°C\n")

# +++++++++ 2. Temperature Range +++++++++ #
data['MaxTemp'] = data[months].max(axis=1, skipna=True) # Calculate max temp
data['MinTemp'] = data[months].min(axis=1, skipna=True) # Calculate min temp
data['TempRange'] = data['MaxTemp'] - data['MinTemp'] # Calculate temp range

max_range = data['TempRange'].max()
largest_range_stations = data[data['TempRange'] == max_range] # largest range stations

with open("question2/largest_temp_range_station.txt", "w") as f:
    for _, row in largest_range_stations.iterrows():
        f.write(f"Station {row['STATION_NAME']}: Range {row['TempRange']:.2f}°C (Max: {row['MaxTemp']:.2f}°C, Min: {row['MinTemp']:.2f}°C)\n")

# +++++++++ 3. Temperature Stability +++++++++ #
data['StdDev'] = data[months].std(axis=1, skipna=True) # Calculate SD for each station

min_std = data['StdDev'].min()
max_std = data['StdDev'].max()

most_stable = data[data['StdDev'] == min_std] # Stations with MIN SD
most_variable = data[data['StdDev'] == max_std] # Stations with MAX SD

with open("question2/temperature_stability_stations.txt", "w") as f:
    for _, row in most_stable.iterrows():
        f.write(f"Most Stable: Station {row['STATION_NAME']}: StdDev {row['StdDev']:.2f}°C\n")
    for _, row in most_variable.iterrows():
        f.write(f"Most Variable: Station {row['STATION_NAME']}: StdDev {row['StdDev']:.2f}°C\n")