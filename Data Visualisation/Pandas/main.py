#importing the packages
import pandas as pd
import matplotlib.pyplot as plt

#reading the file
df3 = pd.read_csv('df3')

#creating a scatter plot between a and b
df3.plot.scatter(x="a",y="b",figsize=(12,4),c="red",s=8)
plt.show()

#creating a histogram with a
df3["a"].plot.hist()
plt.show()

#creating a histogram with column a and a different style
plt.style.use('ggplot')
df3["a"].plot.hist(bins=30)
plt.show()

#creating a boxplot with a and b
df3.boxplot(column=["a","b"])
plt.show()

#creating a kde plot with d
df3['d'].plot.kde()
plt.show()

#creating a kde plot with d with line attributes
df3["d"].plot.kde(linewidth=3,linestyle="--")
plt.show()

#creating an area plot for the first 30 entries
df3.iloc[0:31].plot.area()
plt.show()

#creating an area plot for the first 30 entries and placing the legend outside
df3.iloc[0:31].plot.area(label="test1")
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='center left')
plt.show()
