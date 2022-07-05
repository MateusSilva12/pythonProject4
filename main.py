import random
def bubblesorte(x):
    final=len(x)
    while final>0:
        i=0
        while i<final-1:
            if x[i]>x[i+1]:
                temp=x[i]
                x[i]=x[i+1]
                x[i+1]=temp


            i +=1
        final-=1
v=[9,2,3,3,4]

bubblesorte(v)
print(v)


