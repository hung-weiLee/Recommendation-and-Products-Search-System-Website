from flask import render_template, url_for, redirect, request
from amazon_website import app
from amazon_website import db
from amazon_website.models import *
from pyecharts import options as opts
from pyecharts.charts import *
from sqlalchemy import extract, and_
from datetime import datetime, timedelta


@app.route('/')
def root():
    return redirect(url_for('search_page'))


@app.route('/info/', methods=['POST', 'GET'])
def info_page():
    group = request.args.get("group")
    key = request.args.get("key")
    page = int(request.args.get("page"))
    avg_rate = int(request.args.get("avg_rate"))
    if key == '':
        if group == 'All':

            paginate = Product.query \
                .join(Review) \
                .filter(Review.avg_rating >= avg_rate) \
                .paginate(page, 20, error_out=False)
        else:

            paginate = Product.query \
                .join(Review) \
                .filter(Product.group == group) \
                .filter(Review.avg_rating >= avg_rate) \
                .paginate(page, 20, error_out=False)
    else:
        if group == 'All':

            paginate = Product.query \
                .join(Review) \
                .filter(Product.title.like('%' + key + '%')) \
                .filter(Review.avg_rating >= avg_rate) \
                .paginate(page, 20, error_out=False)
        else:

            paginate = Product.query \
                .join(Review). \
                filter(Product.title.like('%' + key + '%')) \
                .filter(Product.group == group) \
                .filter(Review.avg_rating >= avg_rate) \
                .paginate(page, 20, error_out=False)

    products = paginate.items

    return render_template('information.html', paginate=paginate, products=products, group=group,
                           key=key, page=page, avg_rate=avg_rate)


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    data = request.args.to_dict()
    # form = SearchForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('info_page'), code=307)
    return render_template('search.html', title='Search', result_json=data)


@app.route('/detail', methods=['GET'])
def show_detail():
    product_id = request.args['product_id']

    product = Product.query.filter_by(Id=product_id).first()

    similars, similar_products = [], []

    for similar in product.similar:
        similars.append(
            Product.query.filter_by(ASIN=similar.ASIN).first()
        )

    for similar in similars:
        if similar:
            similar_products.append(similar)

    return render_template('detail.html', product=product, similar_products=similar_products)


def pie_base():
    import redis

    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    num1 = r.get('Book')
    num2 = r.get('Music')
    num3 = r.get('DVD')
    num4 = r.get('Video')
    num5 = r.get('Toy')
    num6 = r.get('Video Games')
    num7 = r.get('Software')
    num8 = r.get('CE')
    num9 = r.get('Sports')
    c = (
        Pie().add("", [("Book", num1), ("Music", num2), ("DVD", num3), ("Video", num4), ("Toy", num5),
                       ("Video Games", num6), ("Software", num7), ("CE", num8), ("Sports", num9)])
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def pie_base2():
    import redis

    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    num1 = r.get('0')
    num2 = r.get('1')
    num3 = r.get('2')
    num4 = r.get('3')
    num5 = r.get('4')
    num6 = r.get('5')
    num7 = r.get('6')
    num8 = r.get('7')
    num9 = r.get('8')
    num10 = r.get('9')
    c = (
        Pie().add("", [("0", num1), ("1", num2), ("2", num3), ("3", num4), ("4", num5),
                       ("5", num6), ("6", num7), ("7", num8), ("8", num9), ("9", num10)])
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def bar_base3():
    num1 = Review.query.filter_by(avg_rating=1).count()
    num2 = Review.query.filter_by(avg_rating=2).count()
    num3 = Review.query.filter_by(avg_rating=3).count()
    num4 = Review.query.filter_by(avg_rating=4).count()
    num5 = Review.query.filter_by(avg_rating=5).count()

    c = (
        Bar().add_xaxis(["5", "4", "3", "2", "1"])
            .add_yaxis('', [num5, num4, num3, num2, num1])
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c


def line_base4():
    import time
    print('check11')
    # data1 = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = '1999'")
    # num1 = data1.fetchall()
    # data2 = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = '2000'")
    # num2 = data2.fetchall()
    # data3 = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = '2001'")
    # num3 = data3.fetchall()
    # data4 = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = '2002'")
    # num4 = data4.fetchall()
    # year = 2000
    # s = "'" + str(year) + "'"
    # data5 = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = "+ s)
    # num5 = data5.fetchall()

    y_list = []
    x_list = []

    for year in range(1999, 2006):
        print('year:',year)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        y = "'" + str(year) + "'"
        data = db.session.execute("SELECT COUNT(product_Id) FROM items WHERE DATE_FORMAT(create_time,'%Y') = " + y)
        num = data.fetchall()
        x_list.append(str(year))
        y_list.append(num[0][0])
    c = (
        Line()
            .add_xaxis(x_list)
            .add_yaxis('', y_list)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c


@app.route("/pieChart")
def get_pie_chart():
    print("success !!!")
    c = pie_base()
    return c.dump_options()


@app.route("/pieChart2")
def get_pie_chart2():
    print("success !!!")
    c = pie_base2()
    return c.dump_options()


@app.route("/barChart1")
def get_bar_chart():
    print("success 123123123123!!!")
    c = bar_base3()
    return c.dump_options()


@app.route("/lineChart")
def get_line_chart():
    print("success 1111!!")
    c = line_base4()
    return c.dump_options()
