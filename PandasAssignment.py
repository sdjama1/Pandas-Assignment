import pandas as pd


sepal_data = pd.read_csv("E:\editing v2\HW\Sepal_Data.csv").squeeze("columns")
petal_data = pd.read_csv("E:\editing v2\HW\Petal_Data.csv").squeeze("columns")


#print(sepal_data.columns)
#print(petal_data.columns)


combined_data = pd.merge(sepal_data, petal_data, on=['sample_id', 'species'])

#print(combined_data.head())

numeric_data = combined_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]


correlation_matrix = numeric_data.corr()


#print("Not inluding 1 to 1 correlations (sepal length vs sepal length etc)","\n", correlation_matrix)

average_values = combined_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
median_values = combined_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].median()
deviation_values = combined_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].std()






print("Median Values", "\n", median_values)
print("Average Values", "\n", average_values)
print("Standard Deviation Values", "\n", deviation_values)




'''
grouped_data = combined_data.groupby('species').agg(['mean', 'median', 'std'])

print(grouped_data)
'''