import pymysql    # 导入操作数据库的库


class MySQL:
    """数据库操作"""
    def __init__(self):
        # 数据库连接信息
        self.config = {
            "host" : "test.lemonban.com",
            "port" : 3306,
            "user" :  "test",
            "password": "test",
            "db":  "future"
        }

    # 连接数据库
    def connect_db(self):
        db = pymysql.connect(**self.config)
        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        return cursor

    def select(self,sql):
        cursor = self.connect_db()
        # 查询语句
        # 使用execute() 执行sql查询
        cursor.execute(sql)

        # 使用fetchone() 获取单条数据
        data = cursor.fetchone()
        cursor.close()
        return data

    # 关闭数据库,这里不好写，使用上下文管理器算了
    def close(self):
        pass




if __name__ == '__main__':
    sql = "select * from member where regName = 'Sherlock'"
    print(MySQL().select(sql))