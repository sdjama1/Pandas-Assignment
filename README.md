Using pd.read_csv(), with .squeeze("columns") to load a single column as a series
To make the combined data we use pd.merge and match the datasets by using sample_id and species
To calculate the correlation between each variable, we select the relevant columns (sepal_length, petal_length, etc.) and put those in a variable
The .corr() funuction does the computing and math for us for the selected variables.
for the Average values we can specify the columns from combined_data and use the .mean() function which calculates for each variable across all samples
Same goes for .median() and .std()

