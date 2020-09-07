#importing package
import pandas as pd

#reading the file
ecom=pd.read_csv("Ecommerce Purchases")

#printing the first 5 entries from the file
print(ecom.head())

#printing the information about the file
print(ecom.info(()))

#printing the average of the purchase price column 
print(ecom["Purchase Price"].mean())

#printing the biggest number of the purchase price column
print(ecom["Purchase Price"].max())

#printing the smallest number of the purchase price column
print(ecom["Purchase Price"].min())

#printing the number of instances where the language is english
print(ecom[ecom["Language"]=="en"].count())

#printing the number of instances where the job is lawyer
print(ecom[ecom["Job"]=="Lawyer"].count())

#printing the number of AM's and PM's in the entries 
print(ecom["AM or PM"].value_counts())

#printing the top 5 jobs
print(ecom["Job"].value_counts().head(5))

#printing the purchase price where the lot is 90 WT
print(ecom[ecom["Lot"]=="90 WT"]["Purchase Price"])

#printing the email where the credit card number is 4926535242672853
print(ecom[ecom["Credit Card"]==4926535242672853]["Email"])

#printing the number of instances where the CC provider is american express and the purchase price is over 95
print(ecom[(ecom["CC Provider"]=="American Express")&(ecom["Purchase Price"]>95)].count())

#printing the number of times the expiry date is 2025
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))

#printing the top 5 email services used
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))



