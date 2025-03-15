import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/QuGenAI/Practice/master/data/iris.csv')
df.head()
df.tail()
# Compare this snippet from github/command.py:  # git clone
# git clone
df.describe()
df.info()