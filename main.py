import redis

class RedisCacheService:
    def __init__(self, host, port, db, prefix):
        self.redis_client = redis.Redis(host=host, port=port, db=db)
        self.prefix = prefix

    def set(self, key, value, ttl):
        key = f"{self.prefix}:{key}"
        self.redis_client.setex(key, ttl, value)

    def get(self, key):
        key = f"{self.prefix}:{key}"
        return self.redis_client.get(key)

    def delete(self, key):
        key = f"{self.prefix}:{key}"
        self.redis_client.delete(key)

    def exists(self, key):
        key = f"{self.prefix}:{key}"
        return self.redis_client.exists(key)

    def ttl(self, key):
        key = f"{self.prefix}:{key}"
        return self.redis_client.ttl(key)

# Misol foydalanish
cache_service = RedisCacheService('localhost', 6379, 0, 'my_prefix')
cache_service.set('user:1', 'John Doe', 3600)  # 1 soatga saqlanadi
print(cache_service.get('user:1'))  # John Doe
cache_service.delete('user:1')
print(cache_service.exists('user:1'))  # False
print(cache_service.ttl('user:1'))  # -2 (soatga saqlangan bo'lsa, -2 qaytadi)
