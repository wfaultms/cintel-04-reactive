'''
Purpose: Use Python to create local datasets for review.

Once they exist, you don't need to run these, but the examples may be
useful for creating your own datasets.

You can uncomment the code and add it to your app.py file. 
After the dataset is created, comment out the code again.

You can also run this file by itself to create datasets.

mtcars.csv - from R mtcars dataset 
https://shinylive.io/py/examples/#read-local-csv

penguins - from Seaborn penguins dataset

flights - from Seaborn flights dataset

Note: A local csv copy allows review from within VS Code.
'''

import pandas as pd
import seaborn as sns
from bokeh.sampledata.les_mis import data as les_mis_data
from bokeh.sampledata.movies_data import data as movies_data


# penguins = sns.load_dataset("penguins")
# penguins.to_excel("penguins.xlsx")
#penguins.to_csv("penguins.csv")


# flights = sns.load_dataset("flights")
# flights.to_excel("flights.xlsx")
# flights.to_csv("flights.csv")

les_mis = pd.DataFrame(les_mis_data['links'])
les_mis.to_excel("les_mis.xlsx")
les_mis.to_csv("les_mis.csv")



