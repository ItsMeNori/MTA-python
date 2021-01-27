import time as t

start = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
end = t.clock()
print(str(end-start) +" seconds")