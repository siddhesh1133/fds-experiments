cri=['a','b','c','d','e','f']
bad=['a','b','c','h','i','j']
fot=['a','h','e','d','k','l']
a=[]
b=[]
c=[]
d=[]
e=[]
g=[]
def fun():
    for i in cri:
        for j in bad:
            if (i==j):
                a.append(i)
    print("students who play both cricket and badminton=",a)
    for i in cri:
        f=0
        for j in bad:
            if(i==j):
                f=1
        if (f==0):
            b.append(i)
    for i in bad:
        f=0
        for j in cri:
            if(i==j):
                f=1
        if (f==0):
            b.append(i)
    print("students who play either cricket or badminton but not both=",b)
    for i in cri:
        for j in fot:
            c.append(i)
    for i in bad:
        for j in fot:
            c.append(i)
    for i in fot:
        f=0
        for j in c:
            if(i==j):
                f=1
        if(f==0):
            d.extend(i)
    print("student who nether play cricket nor batminton=",d)
    for i in cri:
        for j in fot:
            if (i==j):
                e.append(i)
    for i in e:
        f=0
        for j in bad:
            if (i==j):
                f=1
        if(f==0):
            g.extend(i)
    print("students who play cricket and football but  not badminton=",g)
fun()


















        
