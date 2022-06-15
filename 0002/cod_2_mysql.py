import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123123123', port=3306, database='mysql')
cursor = conn.cursor()


with open('/Users/wangyu/Desktop/cod.txt', 'r') as cod_file:

    for i in cod_file:
        sql2 = f"insert into mycods values ('{str(i)}')"
        cursor.execute(sql2)


cursor.close()
conn.commit()
conn.close()