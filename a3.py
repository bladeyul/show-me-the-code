from redis import StrictRedis

redis_config={
				"host":"localhost",
				"port":6379,
				"db":0,
			}

def redis_uid(uids):
	r_db=StrictRedis(**redis_config)
	if r_db.exists('uids'):
		r_db.delete('uids')
	for uid in uids:
		r_db.rpush("uids",uid)
	r_db.close()

