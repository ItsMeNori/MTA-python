#how do for loops work?
#remove break to run the code.
for j in range(9):
    break
    for i in range(9):
        a = i+1
        b = (i+1)*(j+1)
        print(a,"*",(j+1),"=",b)
        
i = 0
while i<10:
    print(" "*(10-i),"* "*i)
    i+=1
    
i = 10
while i>0:
    print(" "*(10-i),"* "*i)
    i-=1