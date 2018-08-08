from django.test import TestCase

# Create your tests here.
nums = range(2,20)
for i in nums:
    nums = filter(lambda x:x==i or x % i,nums)
print(nums)
for i in nums:
    print(i)