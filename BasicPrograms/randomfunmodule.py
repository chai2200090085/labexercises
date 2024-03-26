# import random
# # n=random.randbytes(4)
# # print(n)
# # print(random.randrange(1,3))
# mylist=[1,6,7,4,9]
# jan=(4,7,3,"chabz","hasbzdxj")
# feb={2,7,1,9,"dhsjh","fdsasd"}
#
# print(random.choice(mylist))
# print(random.choice(jan))
# # print(random.choice(feb))
# random.shuffle(mylist)
# print(mylist)
import string
import random
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran)
print(ran1)
# print(ran)

