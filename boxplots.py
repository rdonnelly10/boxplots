import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

#print(healthcare.head())
#print(healthcare['DRG Definition'].unique())

#getting all diagnoses for chest pain
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
#print(chest_pain.head())

#getting all diagnoses for chest paini in the state of Alabama
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']
print(alabama_chest_pain.head())

costs = alabama_chest_pain[' Average Covered Charges '].values

#creating the boxplot
#plt.boxplot(costs)
#plt.show()

#getting every state
states = chest_pain['Provider State'].unique()

#now make a dataset for each state
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

#plotting 50 boxplots
plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels = states)
plt.show()