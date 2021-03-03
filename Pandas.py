import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print (df.head())
df.set_index('PassengerId',inplace=True)
