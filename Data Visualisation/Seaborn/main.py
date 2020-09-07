#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#setting the plotting style
sns.set_style('whitegrid')

#importing the data
titanic = sns.load_dataset('titanic')

#creating a joint plot between fare and age
sns.jointplot("fare","age",titanic)
plt.show()

#creating a histogram plot with fare
sns.distplot(titanic["fare"],kde=False,bins=25)
plt.show()

#creating a box plot between class and age
sns.boxplot(x="class", y="age",data=titanic)
plt.show()

#creating a swarm plot between class and age
sns.swarmplot(x="class", y="age",data=titanic)
plt.show()

#creating a count plot with sex
sns.countplot(x="sex",data=titanic)
plt.show()

#creating a correlation and then a heatmap on the dataframe
tc=titanic.corr()
sns.heatmap(tc,cmap="coolwarm")
plt.show()

#creating a grid of histograms with age differentiated by sex
g=sns.FacetGrid(titanic,col="sex")
g.map(sns.distplot,"age",kde=False)
plt.show()