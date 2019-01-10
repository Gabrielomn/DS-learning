import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as seaborn
train = pandas.read_csv('input/train.csv')
test = pandas.read_csv('input/test.csv')

def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pandas.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind = 'bar', stacked = True, figsize = (10,5))

bar_chart('Sex')