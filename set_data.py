import pandas as pd

"""
    #1 reading the data
    #2 mapping text into numbers
    #3 converting dates to timestamp format
    #4 filling empy values with the average of corresponding column
    #5 scaling the data
"""

# read data from csv file
data_frame = pd.read_csv("realtor-dataset-100k1.csv")

# mapping text
data_frame['status'].replace({'ready_to_build': 1, 'for_sale': 2}, inplace=True)
# data_frame['street'] = data_frame['street'].str.replace('\\d+', '')

# remove duplicates
data_frame.drop_duplicates(keep='last')

# fill NAN with average
data_frame.fillna(data_frame.mean())

data_frame.to_csv("new_data_frame1.csv")

# data_frame['sold_date'] = pd.to_datetime(data_frame['sold_date'])
# data_frame['sold_date'].str.replace("/", "").astype(int)
