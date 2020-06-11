import datetime

from amazon_website.models import *
from amazon_website import db

f = open("../../../amazon-meta.txt")

context = []


def process_text(context):
    if not context:
        return
    else:
        try:

            new_context = []
            for item in context:
                item = item.strip()
                part = item.split(':', 1)
                for index, i in enumerate(part):
                    part[index] = i.strip()
                new_context.append(part)
            p = Product(Id=new_context[0][1],
                        title=new_context[2][1],
                        group=new_context[3][1],
                        salesrank=new_context[4][1],
                        ASIN=new_context[1][1])
            db.session.add(p)
            # db.session.commit()
            similar = new_context[5][1]
            if similar[0] != '0':
                similar = similar.split('  ')
                del similar[0]
                for item in similar:
                    s = Similar(product_Id=new_context[0][1], ASIN=item)
                    db.session.add(s)
                    # db.session.commit()
            categories = int(new_context[6][1])
            for index in range(7, 6 + categories + 1):
                c = Category(name=new_context[index], product_Id=new_context[0][1])
                db.session.add(c)
                # db.session.commit()
            reviews = new_context[6 + categories + 1][1]
            reviews = reviews.split(':', 3)
            for index, item in enumerate(reviews):
                reviews[index] = item.strip()

            review = []
            for item in reviews:
                review += item.split(' ')

            total = review[1]
            downloads = review[4]
            rating = review[8]

            r = Review(product_Id=new_context[0][1],
                       total=int(total),
                       downloaded=int(downloads),
                       avg_rating=float(rating)
                       )
            db.session.add(r)
            # db.session.commit()

            for i in range(6 + categories + 2, 6 + categories + 2 + int(total)):

                item = new_context[i]
                res = []
                for j in item:
                    res += j.split(' ')
                res = [i for i in res if i != '']
                i_ = Item(product_Id=new_context[0][1],
                          create_time=datetime.datetime.strptime(res[0], '%Y-%m-%d'),
                          cutomer_Id=res[2],
                          rating=res[4],
                          votes=res[6],
                          helpful=res[8]
                          )
                db.session.add(i_)
                # db.session.commit()

            db.session.commit()
            print(new_context[0][1])
        except:
            db.session.remove()
            print("data error!")


while (1):

    flag = False
    line = f.readline()
    if line in ['\n', '\r', '\n\r']:
        process_text(context)
        context.clear()
    elif line:
        context.append(line)

    else:
        print('Done!')
        break
