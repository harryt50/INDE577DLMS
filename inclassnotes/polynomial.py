class Polynomial(object):
    def __init__(self, coef):
        self.coef = coef
        
    def degree(self):
        return( len(self.coef) -1)
    


lst =[4,0-1,1]
p = Polynomial(lst)

print(f"{p.coef =}")
