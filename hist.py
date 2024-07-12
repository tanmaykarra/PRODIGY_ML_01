# Load the dataset again to ensure all columns are available
data = pd.read_csv(file_path, skiprows=4)

# Melt the data to have 'Year' and 'Population' columns
data_melted = data.melt(id_vars=['Country Name'], value_vars=[str(year) for year in range(1960, 2023+1)], 
                        var_name='Year', value_name='Population')

# Drop rows with missing values in 'Population'
data_melted = data_melted.dropna(subset=['Population'])

# Convert 'Year' and 'Population' columns to appropriate data types
data_melted['Year'] = data_melted['Year'].astype(int)
data_melted['Population'] = data_melted['Population'].astype(float)

# Plotting the histogram for population distribution
plt.figure(figsize=(12, 8))
plt.hist(data_melted['Population'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.title('Distribution of Population from 1960 to 2023')
plt.show()
