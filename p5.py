class y:
    cls_attr=0
    def __init__(self,g,v0):
        self.g=g
        self.v0=v0
    def value(self,t):
        return self.v0*t-0.5*self.g*t**2
y.cls_attr=5
property
y=Y(9.8,5)
print(y.value(0.1))