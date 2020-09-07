#importing package
import pandas as pd

#reading the file
sal=pd.read_csv("Salaries.csv")

#printing the first 5 entries 
print(sal.head())

#printing the information of the csv
print(sal.info())

#printing the average of the base pay column 
print((sal["BasePay"].mean()))

#printing the biggest over time pay
print(sal["OvertimePay"].max())

#printing the job title of the employee called joseph driscoll
print(sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"])

#printing the total pay benefits of the employee called joseph driscoll
print(sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"])

#printing the information of the employee with the biggest total pay benefits
print(sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()])

#printing the information of the employee with the smallest total pay benefits
print(sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()])

#printing the average base pay per year
print(sal.groupby('Year').mean()['BasePay'])

#printing the number of unique job titles
print(sal["JobTitle"].nunique())

#printing the top 5 number of job titles
print(sal['JobTitle'].value_counts().head(5))

#printing the number of job title that only has one occourence in 2013
print(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

#printing the number of job titles that have the word chief in them
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
print(sum(sal['JobTitle'].apply(chief_string)))
