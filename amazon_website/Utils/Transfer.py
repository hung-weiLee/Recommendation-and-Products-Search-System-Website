import pickle

from amazon_website.models import *
from amazon_website import db

#DO NOT run this code
# my_dic ={'Book':0,
#          'Music':1,
#          'DVD':2,
#          'Video':3,
#          'Toy':4,
#          'Video Games':5,
#          'Software':6,
#          'CE':7,
#          'Sports':8}
# res = Product.query.join(Category).join(Review).all()
# print('data loaded')
# for index, item in enumerate(res):
#     p_id = item.Id
#     vec = str(my_dic[item.group])+','+ str(item.salesrank)
#     vec += ','+str(len(item.categories))
#     vec += ','+str(item.reviews[0].total) + ','+str(item.reviews[0].downloaded)+','+str(item.reviews[0].avg_rating)
#     s = Samples(product_Id=p_id,vector=vec)
#     db.session.add(s)
#     print(index + 1, '/', len(res))
#
# db.session.commit()

# from sklearn import preprocessing
#
# f = open('../ML/x.2d', 'rb')
# x = pickle.load(f)
# f.close()
# x_train = preprocessing.scale(x)

#x_train, x_test = train_test_split(x, test_size=0.3, random_state=42)
#print(len(x_train),' ',len(x_test))

from sklearn.cluster import KMeans

# model = KMeans(n_clusters=10).fit(x_train)
# f = open('model', 'wb')
# pickle.dump(model, f)
# f.close()
# f = open('../ML/model', 'rb')
# model = pickle.load(f)
# f.close()
# y = model.predict(x_train)
# print(len(y))
#
#
# res = Samples.query.all()
# for index, item in enumerate(res):
#     if index%1000 == 0:
#         print(index)
#     item.score = int(y[index])
#     db.session.add(item)
# db.session.commit()
