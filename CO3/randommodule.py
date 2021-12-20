#rondom module
print(".............")
import random
l1=["apple","bnanana","orange"]
print("sample",random.sample(l1,k=2))
print("choice",random.choice(l1))
print("choices:",random.choices(l1,k=2))
random.shuffle(l1)