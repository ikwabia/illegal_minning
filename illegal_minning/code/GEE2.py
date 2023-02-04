#import pandas as pd
##importing the csv file generated with the analysis in gcp
df=pd.read_csv(r"C:/Users/Windows10/Desktop/cloud_computing/cc.csv")
df
##describing the data
df.describe()
##plotting the graph of the statistics
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
plt.figure(figsize=(12,6))
date=df['DATE']
ashanti=df['ASHANTI']
western=df['WESTERN']
greater=df['GREATER']
plt.plot(date,ashanti,label='ASHANTI REGION',linewidth=2,marker='o')
plt.plot(date,western,label='WESTERN REGION',linewidth=2,marker='*')
plt.plot(date,greater,label='GREATER ACCRA REGION',linewidth=2,marker='x')
plt.title('YEARLY VEGETATION FLOW')
plt.ylabel('ACRES OF LAND')
plt.xlabel('YEARS')
plt.legend()

##average acres of Land of vegetation through analysis period
average_A = df['ASHANTI'].mean()
average_G = df['GREATER'].mean()
average_W = df['WESTERN'].mean()
print(average_A)
print(average_G)
print(average_W)

##analysing period 2018&2022
compare_data= df[(df.DATE ==2018)!=(df.DATE==2022)]
compare_data
compare_data.std()

##bargraph of 2018&2022
compare_data.plot(x='DATE',kind='bar',figsize=(12,6))
plt.ylabel('ACRES OF LAND')
plt.xlabel('YEARS')
plt.title('COMPARING DATA OF 2018 & 2022')
