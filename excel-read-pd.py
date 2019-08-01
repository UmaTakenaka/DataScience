#%%
import pandas as pd
filename = "population.xlsx"
sheet_name = "list-sjis.csv"
book = pd.read_excel(filename, sheetname=sheet_name)

book.sort_values(by="法定人口", ascending=False)
print(book)

#%%
