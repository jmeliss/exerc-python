'''#PILHA 
p = Pilha[]
num = 13
while num > 0:
    resto = num % 2
    num - num // 2
    p.push(resto)

while not p.empyt():
    print(p.pop())

#cod de busca 
class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
 
    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self'''

#questao prova
class Pilha(): 
    def __init__(self): 
        self.data = [ ] 
 
    def push(self, x): 
        self.data.append(x) 
 
    def pop(self): 
        if len(self.data) > 0: 
            return self.data.pop(-1) 
 
    def empty(self): 
        return len(self.data) > 0 
 
p = Pilha() 
q = Pilha() 
for i in range(5): 
    if i % 2 == 0: 
        p.push(i) 
    else: 
        q.push(i) 
while p.empty(): 
    q.push(p.pop()) 
while q.empty(): 
    print(q.pop()) 

# outra questao 
class S: 
    def __init__(self): 
        self.v = [ ] 
        self.i = -1 
 
    def push(self, x): 
        self.i += 1 
        self.v.insert(0, x) 
 
    def pop(self): 
        if(not self.empty()): 
            self.i -= 1 
            return self.v.pop() 
 
    def empty(self): 
        return self.i < 0 
 
 
s = S() 
for i in range(10): 
    s.push(i) 
 
while not s.empty(): 
    print(s.pop()) 