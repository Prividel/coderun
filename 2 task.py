from math import *
from sklearn.ensemble import RandomForestRegressor

x = []
y = []
for line in open('data.csv'):
    x_, y_ = map(float, line.strip().split(','))
    x.append(x_)
    y.append(y_)

features = []
for xx in x:
    curFeatures = [
        sin(xx) ** 2,  # a^2
        log(xx) ** 2,  # b^2
        sin(xx) * log(xx),  # 2ab
        xx ** 2  # c
    ]
    features.append(curFeatures)

rf_model = RandomForestRegressor(max_depth=100)
rf_model.fit(features, y)
importance = rf_model.feature_importances_
a = sqrt(importance[0])
b = sqrt(importance[1])
c = importance[3]

print('{:.2f} {:.2f} {:.2f}'.format(a, b, c))
