# coding:utf-8
# Author:窝里横
from pprint import pprint

import pymysql
import os
from common.readfile import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "api_demoProject.conf")
data = data.load_ini(data_file_path)["MYSQL"]
# print(data)


DB_CONF = {
    "host": data["HOST"],
    "port": int(data["PORT"]),
    "user": data["USER"],
    "password": data["PASSWORD"],
    "db": data["DB"]
}

class MysqlDb():

    def __init__(self, db_conf=None, cursors=pymysql.cursors.DictCursor):
        # 通过字典拆包传递配置信息，建立数据库连接
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=cursors)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


db = MysqlDb(DB_CONF)

if __name__ == '__main__':
    # sql = 'select * from mmall_user'
    res = db.select_db("select * from mmall_user")
    pprint(res)
