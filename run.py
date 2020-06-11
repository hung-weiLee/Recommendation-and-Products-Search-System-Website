from amazon_website import app
from amazon_website.models import *
from flask_apscheduler import APScheduler

if __name__ == '__main__':
    scheduler = APScheduler()


    # interval examples
    @scheduler.task('interval', id='do_job_1', seconds=30)
    def job1():
        import redis
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
        r.set('Book', Product.query.filter_by(group="Book").count())  # key是"foo" value是"bar" 将键值对存入redis缓存
        r.set('Music', Product.query.filter_by(group="Music").count())
        r.set('DVD', Product.query.filter_by(group="DVD").count())
        r.set('Video', Product.query.filter_by(group="Video").count())
        r.set('Toy', Product.query.filter_by(group="Toy").count())
        r.set('Video Games', Product.query.filter_by(group="Video Games").count())
        r.set('Software', Product.query.filter_by(group="Software").count())
        r.set('CE', Product.query.filter_by(group="CE").count())
        r.set('Sports', Product.query.filter_by(group="Sports").count())
        print('Update Count Job Done')


    @scheduler.task('interval', id='do_job_2', seconds=30)
    def job2():
        import redis
        r = redis.Redis(host='localhost', port=6379,
                        decode_responses=True)  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
        r.set('0', Samples.query.filter_by(score=0).count())  # key是"foo" value是"bar" 将键值对存入redis缓存
        r.set('1', Samples.query.filter_by(score=1).count())
        r.set('2', Samples.query.filter_by(score=2).count())
        r.set('3', Samples.query.filter_by(score=3).count())
        r.set('4', Samples.query.filter_by(score=4).count())
        r.set('5', Samples.query.filter_by(score=5).count())
        r.set('6', Samples.query.filter_by(score=6).count())
        r.set('7', Samples.query.filter_by(score=7).count())
        r.set('8', Samples.query.filter_by(score=8).count())
        r.set('9', Samples.query.filter_by(score=9).count())
        print('Update Count Job_2 Done')

    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
