#importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb

#reading the file
df=pd.read_csv("911.csv")

#getting the info on the file
df.info()

#printing the first 5 entries in the file
print(df.head())

#printing the top 5 occurring zip codes
print(df["zip"].value_counts().head(5))

#printing the top 5 occurring townships
print(df["twp"].value_counts().head(5))

#printing the number of unique titles
print(df["title"].nunique())

#creating a new column in the datafram for the reason of the call
df["reason"]=df["title"].apply(lambda title: title.split(":")[0])

#printing the number of instances for the reasons
print(df["reason"].value_counts())

#plotting a count plot for the reasons
sb.countplot(x="reason",data=df)
mp.show()

#getting the datatype for the time stamp column
print(type(df.loc[0,"timeStamp"]))

#converting the time stamp column to a datetime format
df["timeStamp"]=pd.to_datetime(df["timeStamp"])

#creating new columns for the hour, month and day
df["hour"]=df["timeStamp"].apply(lambda time: time.hour)
df["month"]=df["timeStamp"].apply(lambda time: time.month)
df["day"]=df["timeStamp"].apply(lambda time: time.dayofweek)

#converting the day number to its respective word
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df["day"]=list(map(lambda x: dmap[x],df["day"]))

#plotting a countplot for the days seperated by the reason
sb.countplot(x="day",data=df,hue="reason")
mp.show()

#plotting a countplot for the month seperated by the reason
sb.countplot(x="month",data=df,hue="reason")
mp.show()

#creates a dataframe that groups by month and returns the count for each column
byMonth=df.groupby("month").count()
print(byMonth.head())

#plotting a line plot for the number of calls per month
byMonth['twp'].plot.line()
mp.show()

#plotting a linear fit plot between number of calls per month
byMonth.reset_index(inplace=True)
sb.lmplot(x="month",y="twp",data=byMonth)
mp.show()

#creates a new column with the date
df["date"]=df["timeStamp"].apply(lambda time: time.date())

#creates a dataframe that groups by date and returns the count for each column
byDate=df.groupby("date").count()

#plotting a line plot for the number of calls per date
byDate['twp'].plot.line()
mp.show()

#creates a new dataframe grouped by the date and returns the count of only the reason column by either traffic, fire or ems and then plots a line plot of it
byDateTraffic=df[df['reason']=='Traffic'].groupby("date").count()
byDateTraffic['twp'].plot.line()
mp.show()
byDateFire=df[df['reason']=='Fire'].groupby("date").count()
byDateFire['twp'].plot.line()
mp.show()
byDateEMS=df[df['reason']=='EMS'].groupby("date").count()
byDateEMS['twp'].plot.line()
mp.show()

#creates a correlation grouped by day and hour with the count per column
hm1=df.groupby(["day","hour"]).count()["twp"].unstack()

#plotting a heat map
sb.heatmap(hm1)
mp.show()

#plotting a cluster map
sb.clustermap(hm1)
mp.show()

#creates a correlation grouped by day and mounth with the count per column
hm2=df.groupby(["day","month"]).count()["twp"].unstack()

#plotting a heat map
sb.heatmap(hm2)
mp.show()

#plotting a cluster map
sb.clustermap(hm2)
mp.show()

