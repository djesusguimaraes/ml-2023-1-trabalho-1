import numpy as np
import pandas as pd

def clean_data():
	data = pd.read_excel('dataset.xlsx')

	print(f'Original Shape: \t{data.shape}\n')

	data = data.dropna(axis=1, how='all')

	print(f'Not NaN Columns Shape: \t{data.shape}\n')

	data = data.dropna(thresh=10)

	print(f'Not NaN Shape: \t{data.shape}\n')

	string_columns = data.select_dtypes(include=['object']).columns

	print(f'Object Columns count: {len(string_columns)}\n')

	for column in string_columns:
		data[column] = data[column].astype('category').cat.codes

	data.to_excel('dataset_clean.xlsx')
 
	return data

def z_score_outliers(df, threshold=3):
	z_scores = np.abs((df - df.mean()) / df.std())

	outliers = df[(z_scores > threshold).any(axis=1)]

	print(outliers)

	outliers.to_excel('outliers_zscore.xlsx')


z_score_outliers(clean_data())
