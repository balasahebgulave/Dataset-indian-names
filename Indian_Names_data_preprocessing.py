import pandas as pd

# Indian-Male-Names.csv and Indian-Female-Names.csv contains raw csv of Indian names.

male_names = pd.read_csv('Indian-Male-Names.csv')
# male_names contains data available in Indian-Male-Names.csv which contain only unprocessed male names.

female_names = pd.read_csv('Indian-Female-Names.csv')
# female_names contains data available in Indian-Female-Names.csv which contain only unprocessed female names.

namelist = []

for names in female_names['name']:
# processing on names acailable in data.
    first_name = str(names).strip().split(' ')[0]

    namelist.append(first_name)

for names in male_names['name']:
# processing on names acailable in data.

    first_name = str(names).strip().split(' ')[0]

    namelist.append(first_name)

processed_name_list = []

s = 'abcdefghijklmnopqrstuvwxyz'
# s contains all alphabates a-z.

for i in namelist:
# processing on names acailable in namelist which contains all male and female names .

    i = i.split('@')[0]

    i = i.split('.')[-1]

    i = i.split('-')[-1]

    i = i.strip('`').strip()

    if len(i) > 2:

        for j in i:

            if j in s:
                processed_name_list.append(i)
 

unique_names = set(processed_name_list)
# unique_names contains unique names and removes repeated names.

processed_name_list = sorted(list(unique_names))
# processed_name_list contains list of all names in sorted format.

data = pd.DataFrame(processed_name_list, columns=['Name'])
# data contains dataframe of processed_name_list.

data.to_csv('Indian_Names.csv')
# final output create Indian_Names.csv


