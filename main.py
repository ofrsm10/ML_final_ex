import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from set_data import data_frame

X = data_frame[['acre_lot', 'house_size', 'bed', 'bath', 'zip_code']]

scale = StandardScaler()
scaledX = scale.fit_transform(X)


if __name__ == '__main__':
    y = data_frame['price']
    regr = linear_model.LinearRegression()
    regr.fit(scaledX, y)
    scaled = scale.transform([[2300, 1.3]])

    predicted_price = regr.predict([scaled[0]])
    print(predicted_price)
