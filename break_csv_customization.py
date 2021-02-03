import pandas as pd

df = pd.read_csv("music.csv")

# for i in df:
#     print(i) # gives you the column name

# df.values gives us multidimenional list where each item(list) in list is the row of the csv (no column name rows)

male_df_values = []
female_df_values = []

for i in df.values:
    if i[1] == 1:  # 1 for male
        male_df_values.append(i)
    else:  # other one is 0 which is female
        female_df_values.append(i)

c = 0
male_dataframe = {}
female_dataframe = {}

for i in df:  # gives the column name
    temp = []

    for j in male_df_values:
        temp.append(j[c])

    male_dataframe[i] = temp

    # dataframe should be like {
    #     "column_name1": [row1_column1_value, row2_column1_value, row3_column1_value ...],
    #     "column_name2": [row1_column2_value, row2_column2_value, row3_column2_value ...],
    #     "column_name3": [row1_column3_value, row2_column3_value, row3_column3_value ...],
    # }

    c += 1  # incrementing for getting the next column value for each rows

# convert it to panda dataframe object
csv_converter = pd.DataFrame(male_dataframe)
# using dataframe you can save it as cv
csv_converter.to_csv("o.csv", index=False)
