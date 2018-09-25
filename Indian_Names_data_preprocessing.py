import pandas as pd

male_names = pd.read_csv('Indian-Male-Names.csv')

female_names = pd.read_csv('Indian-Female-Names.csv')

namelist = []

for names in female_names['name']:

    first_name = str(names).strip().split(' ')[0]

    namelist.append(first_name)

for names in male_names['name']:

    first_name = str(names).strip().split(' ')[0]

    namelist.append(first_name)

processed_name_list = []

s = 'abcdefghijklmnopqrstuvwxyz'

for i in namelist:

    i = i.split('@')[0]

    i = i.split('.')[-1]

    i = i.split('-')[-1]

    i = i.strip('`').strip()

    if len(i) > 2:

        for j in i:

            if j in s:
                processed_name_list.append(i)

unique_names = set(processed_name_list)

processed_name_list = sorted(list(unique_names))

data = pd.DataFrame(processed_name_list, columns=['Name'])

data.to_csv('Indian_Names.csv')
