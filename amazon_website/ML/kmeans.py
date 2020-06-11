import matplotlib._cm_listed
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pickle
import pandas
from amazon_website.models import *


# from amazon_website.models import *
# samples = Samples.query.all()
# f = open('x', 'wb')
# pickle.dump(samples, f)
# f.close()
# f = open('x', 'rb')
# x = pickle.load(f)
# # #x = x[:50]
# xx = []
# for i in x:
#     vec = str(i.vector).split(',')
#     vec = list(vec)
#     for index, item in enumerate(vec):
#         vec[index] = int(item)
#     temp = []
#     temp.append(vec[0])
#     temp.append(vec[5])
#     xx.append(temp)
# # #
# # #
# xx = np.asarray(xx)
#
#
# f = open('x.2d', 'wb')
# pickle.dump(xx, f)
# f.close()




from sklearn import preprocessing

f = open('x.2d', 'rb')
x = pickle.load(f)
f.close()
x_train = preprocessing.scale(x)

#x_train, x_test = train_test_split(x, test_size=0.3, random_state=42)
#print(len(x_train),' ',len(x_test))

from sklearn.cluster import KMeans

# model = KMeans(n_clusters=10).fit(x_train)
# f = open('model', 'wb')
# pickle.dump(model, f)
# f.close()
f = open('model', 'rb')
model = pickle.load(f)
f.close()
y = model.predict(x_train)
print(len(y))

# plt.xlabel('group')
# plt.ylabel('avg_rating')
#
# plt.scatter(x_train[:, 0], x_train[:, 1], c=model,cmap="tab20")
# plt.colorbar()
# plt.show()
