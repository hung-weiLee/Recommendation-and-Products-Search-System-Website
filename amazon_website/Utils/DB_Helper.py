import pymysql
from sqlalchemy import create_engine

class MysqlHelper(object):

    def __init__(self,host,username,password,database,port):
        #初始化数据库信息并创建数据库连接
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset='utf8')
        print("数据库连接成功！")

    def insertDB(self,sql,param=None):
        ''' 插入数据库操作 '''
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            res = self.cursor.execute(sql,param)
              # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            self.db.commit()
            return res
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def deleteDB(self,sql,param=None):
        ''' 操作数据库数据删除 '''
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            res = self.cursor.execute(sql,param) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
            return res
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def clearTable(self,tableName):
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            res = self.cursor.execute("truncate TABLE "+tableName)
            # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
            return res
        except:
            pass
        finally:
            self.cursor.close()

    def updateDb(self,sql,param=None):
        ''' 更新数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            #self.cursor.execute(sql)
            res = self.cursor.execute(sql,param) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
            return res
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDb(self,sql,param=None):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql,param) # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            res = self.cursor.fetchall()
            return res
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()


    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()
        print("数据库连接关闭！")

mysqlHelper = MysqlHelper("ec2-34-221-148-154.us-west-2.compute.amazonaws.com","root","Bigdata@415","amazon",3306)