import numpy as np
import pandas as pd

data = pd.read_excel('dataset.xlsx')

string_columns = data.select_dtypes(include=['object']).columns
data = data.drop(string_columns, axis=1)

data.to_excel('dataset_clean.xlsx')

def z_score_outliers(df, threshold=3):
	z_scores = np.abs((df - df.mean()) / df.std())

	outliers = df[(z_scores > threshold).any(axis=1)]

	print(outliers)

	outliers.to_excel('outliers_zscore.xlsx')
 

def quartile_outliers(df, threshold=1.5):
	Q1 = df.quantile(0.25)
	Q3 = df.quantile(0.75)

	IQR = Q3 - Q1

	cutoff = threshold * IQR

	lower = Q1 - cutoff
	upper = Q3 + cutoff
	outliers = df[(df < lower) | (df > upper)].dropna(how='all')

	print(outliers)

	outliers.to_excel('outliers_quartile.xlsx')


z_score_outliers(data)
quartile_outliers(data)
