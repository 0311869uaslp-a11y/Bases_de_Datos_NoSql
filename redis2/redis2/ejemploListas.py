import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
print(r.lrange("milista",0,-1))
arr=r.lrange("fibo",0,-1)
print(arr[3].decode())