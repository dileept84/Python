#Decoraters: by using decoraters we can add extra features to existing function

def div(a,b):
    print(a/b)

def deco_div(func):      #special decorater function

    def inner(a,b):
        if a<b:
            a,b = b, a
            return func(a,b)
    return inner
div = deco_div(div)
div(2,4)