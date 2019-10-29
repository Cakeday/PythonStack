import random
def randInt(max=100,min=0):
    if min>max or max<0 or min<0:
        return 'dork'
        
    num = random.random() * (max-min) + min
    return round(num)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=-15, max=7))