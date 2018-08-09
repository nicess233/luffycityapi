from django.test import TestCase

# Create your tests here.
import redis
conn = redis.Redis(host="192.168.11.122",port=6379)

conn.set("class_name","11")
print(conn.get("class_name"))