import pandas as pd

print("Resume Screening System")

df = pd.read_excel("dataset/Resume.xls")

print(df.head())
print(df.columns)
print(df.shape)
