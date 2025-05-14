#questao 01
def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return v[i] + f(v, i - 1) 
 
l = [5,4,6,8,1,2] 
print(f(l, len(l) - 1)) 

#questao 2
def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return max(v[i], f(v, i - 1)) 
 
l = [5,4,6,8,1,2] 
print(f(l, len(l) - 1)) 

#questao 3
def func(n): 
    if n <= 1: 
        return 1 
    else: 
        return n * func(n - 1) 
 
print(func(4)) 

#questao 4
def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return min(v[i], f(v, i - 1)) 
 
l = [5,4,6,8,10,12] 
print(f(l, len(l) - 1)) 