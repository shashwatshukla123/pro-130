import pandas as pd

df = pd.read_csv("final.csv")
# Listing all columns
print(df.head(5))

#Deleting the file
del df["Luminosity"]

print(list(df))
df.to_csv('main.csv') 