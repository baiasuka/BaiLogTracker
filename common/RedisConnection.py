import pickle
import redis
import sys
sys.path.append("../")
import config

class RedisConnection:
    def __init__(self):
        if config:
            self.host = config.REDIS_HOST
            self.port = config.REDIS_PORT
            self.db = config.REDIS_CACHE_DB
            self.pwd = config.REDIS_PASSWORD
            # 键的存活时间
            self.expire = config.REDIS_CACHE_EX
            # self.xx = config.REDIS_CACHE_XX
        pool = redis.ConnectionPool(host=self.host,password=self.pwd, port=self.port, db=self.db)
        self.conn = redis.Redis(connection_pool=pool)

    # 数据储存
    def set(self, key, value, ex=None):
        # 序列化对象，并将结果数据流写入到文件对象中
        value = pickle.dumps(value)
        if ex:
            self.conn.set(key,value,ex=ex)
        else:
            self.conn.set(key,value, ex=self.expire)

    # 数据读取
    def get(self, key):
        value = self.conn.get(key)
        if value:
            # 反序列化对象，将文件数据还原为python对象
            value = pickle.loads(value, encoding='bytes')
            return value
        else:
            return None
