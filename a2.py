import pymysql

mysql_config={
				"ip":"127.0.0.1",
			  	"port":"3306",
			  	"database":"test",
			  	"password":"test"
			  	}

def insertUIDToMysql(uids):
	connection=pymysql.connect(**mysql_config)
	with connection.cursor() as cursor:
		for uid in uids:
			sql="insert into uid (uid) values %s"
			cursor.execute(sql,(uid))
			connection.commit()
	connection.close()

