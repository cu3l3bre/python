import redis  # pip install redis

# db = 0..15
r0 = redis.Redis(host='127.0.0.1', port=6379, db = 0, charset="utf-8", decode_responses=True)
r1 = redis.Redis(host='127.0.0.1', port=6379, db = 1, charset="utf-8", decode_responses=True)
r15 = redis.Redis(host='127.0.0.1', port=6379, db = 15, charset="utf-8", decode_responses=True)

print("Typ von r0: ",type(r0))


d0 = {"Croatia": "Zagreb", "Bahamas": "Nassau"}
print("Typ von d0: ", type(d0))

#r0.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
r0.mset(d0)
r0.mset({"Germany": "Berlin", "France": "Paris"})

r1.mset({"Italy": "Rome", "England": "London"})

r15.mset({"Daniel": "32"})


print(r0.get("Croatia"), r1.get("Italy") , r0.get("England"))
print(r15.get("Daniel"))

r0.bgsave()