from functools import reduce

f=lambda a,b:a+b   # defining anonymous (Lambda) function for addition

result = f(5,6)
print(result)

#Filter, MAP, Reduce function with lambda expression

num = [2,3,6,9,12,56,77,55]

filter = list(filter(lambda n: n%2==0, num))
print(filter)

map = list(map(lambda n: n*2, filter))
print(map)

reduce = reduce(lambda a,b:a+b, map)  #reduce fun is not available default. we need to import it from functools.
print(reduce)
