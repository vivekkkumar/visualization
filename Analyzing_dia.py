__author__ = 'vmuthukr'


import pandas as pd
import matplotlib.pyplot as plt


data = pd.ExcelFile("/Users/vmuthukr/Documents/Data sets/diabetesNFHS3.xls")

# to remove unwanted rows print data.parse(skiprows=2)

data_obese =  data.parse()

#Renaming columns:


data_obese.rename(columns={u'India/States/UTs': u'States'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of women in age group 15-49 per 100-000 reported Diabetes-Total': u'women in age group 15-49 per 100-000 Total'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of women in age group 15-49 per 100-000 reported Diabetes-Rural': u'women in age group 15-49 per 100-000 Rural'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of women in age group 15-49 per 100-000 reported Diabetes-Urban': u'women in age group 15-49 per 100-000 Urban'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of men in age group 15-49 per 100-000 reported Diabetes-Total': u'men in age group 15-49 per 100-000 Total'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of men in age group 15-49 per 100-000 reported Diabetes-Rural': u'men in age group 15-49 per 100-000 Rural'}, inplace=True)
data_obese.rename(columns={u'NFHS III(2005-06)-Number of men in age group 15-49 per 100-000 reported Diabetes-Urban': u'men in age group 15-49 per 100-000 Urban'}, inplace=True)

#data_obese.plot()
#plt.show()


data_obese_no_cat = data_obese.drop('Categories', axis=1)
data_obese_no_cat = data_obese.drop('women in age group 15-49 per 100-000 Total', axis=1)
data_obese_no_cat = data_obese.drop('men in age group 15-49 per 100-000 Total', axis=1)

data_obese_no_cat.set_index('States', inplace=True)


list = ['Andhra Pradesh', 'Kerala', 'Tamil Nadu', 'Karnataka']

#removing_total.loc[list]

new_data = data_obese_no_cat.loc[list]

new_data.plot(kind='bar');
#data_obese_no_cat.plot(alpha=0.5)


plt.show()










