#pip install redis
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.set('foo', 'bar')
r.mset({'a':'100',"b":3.45,"c":"hola juan"})
print(r.mget('a','b'))
print(r.get('a'),r.get('b'))