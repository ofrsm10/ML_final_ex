import pandas as pd


def concat(a, b, c, d):

    s1 = str(a)
    s2 = str(b)
    s3 = str(c)
    s4 = str(d)
    s = s1 + s2 + s3 + s4
    e = int(s)

    return e


data_frame = pd.read_csv("new_data_frame1.csv")

data_frame['mapped_address'] = ''
data_frame.to_csv("date_frame.csv")
i = 1
j = 1
k = 1
m = 1
states = data_frame['state'].unique()
for state in states:
    cities = data_frame.loc[data_frame['state'] == state]['city'].unique()
    for city in cities:
        streets = data_frame.loc[(data_frame['state'] == state) & (data_frame['city'] == city)]['street'].unique()
        for street in streets:
            addresses = data_frame.loc[
                (data_frame['state'] == state) & (data_frame['city'] == city) &
                (data_frame['street'] == street)]['full_address'].unique()
            for address in addresses:
                temp_df = data_frame.loc[
                    (data_frame['state'] == state) & (data_frame['city'] == city) & (data_frame['street'] == street) &
                    (data_frame['full_address'] == address)]
                print(temp_df)
                mapping_code = concat(i, j, k, m)
                temp_df['mapped_address'] = mapping_code
                m += 1
            k += 1
        j += 1
    i += 1


