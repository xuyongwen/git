import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd = 'root', db = 'goods')
print conn
cur = conn.cursor()
print cur
cur.execute("select * from t_admin")
ret = cur.fetchall()
print ret
for x in ret:
	print x 
cur.close()
conn.close() 