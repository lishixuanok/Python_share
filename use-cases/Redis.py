import redis

# redis documentation
# https://pypi.python.org/pypi/redis
pool = redis.ConnectionPool(host='your host', port=6379, db=1, password='your password')
r = redis.Redis(connection_pool=pool)


def pipline():
    # put data
    data = {'test': True}
    r.set('test', data)

    # get data
    pipe = r.pipeline()
    pipe.get('test')
    res = pipe.execute()
    print(res)

if __name__ == '__main__':
    pipline()
