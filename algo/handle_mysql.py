import pymysql


class HandleMysql:
    def __init__(self):
        """
        连接数据库
        """
        self.conn = pymysql.connect(host='192.168.3.7',
                                    user='laoxu',
                                    password= 'goodbaby',
                                    db='study',
                                    port=3306,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None,is_more=False):
        """获取查询数据"""
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            """多条数据，调用fetchall"""
            sqlvalue = self.cursor.fetchall()
        else:
            """单条数据，调用fetchone"""
            sqlvalue = self.cursor.fetchone()
        return sqlvalue

    def get_tablenames(self, sql):
        self.cursor.execute(sql)
        tables = self.cursor.fetchall()
        for table in tables:
            print(table)


    def create_table(self):
        return




if __name__=="__main__":
    homesql=HandleMysql()
    '''
    score_list = homesql.run('select * from stu_score',is_more=True)
    for i in score_list:
        print(i)
    '''
    sql_new="SELECT table_name,ORDINAL_POSITION, COLUMN_NAME," \
        "COLUMN_TYPE,IS_NULLABLE,COLUMN_COMMENT FROM information_schema. COLUMNS " \
        "WHERE TABLE_SCHEMA = 'study'"
    print(homesql.get_tablenames(sql_new))


