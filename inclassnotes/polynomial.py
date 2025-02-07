class Polynomial(object):
    def __init__(self, coef, name = "harry"):
        self.coef = coef
        self.name =  name
        
    def degree(self):
        return( len(self.coef) -1)
    
    def evaluate(self, x):
        return sum()
    


a =[4,0-1,1]
b = [1,0,-1]
p = Polynomial(a)
q = Polynomial(b, name="Harry")

print(f"{p.coef =}")
print(f"{q.coef =}")

print(f"{p.degree =}")
print(f"{q.degree =}")

print(f"{p.name =}")
print(f"{q.name =}")

