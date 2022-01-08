with open('day5.txt','r') as f:
    a = []
    for line in f.readlines():
        a.append(line.rstrip().replace(' -> ', ',').split(','))

c = []
h = []
for p in a:
    for e in range(len(p)):
        p[e] = int(p[e])
    
    if p[0] == p[2]:
        c.append(p)
    elif p[1] == p[3]:
        c.append(p)
    else:
        h.append(p)

g = [[0 for x in range(1000)] for x in range(1000)]

for d in c:
    s=1
    if(d[0]>d[2]):
        s = -1
    if(d[1]>d[3]):
        s = -1

    if(d[0]==d[2]):
        for y in range(d[1],d[3]+s,s):
            g[d[0]][y] += 1
    elif(d[1]==d[3]):
        for x in range(d[0],d[2]+s,s):
            g[x][d[1]] += 1

for d in h:
    dx = dy = 1
    x2 = d[2]
    y2 = d[3]
    x = x1 = d[0]
    y = y1 = d[1]
    if x1>x2:
        dx = -1
        x2 -= 1
    else:
        x2+=1
    if y1>y2:
        dy = -1
        y2 -= 1
    else:
        y2 += 1
    #print(d)
    while True:     
        g[x][y] += 1
        #print("({},{})".format(x,y))
        x += dx
        y += dy

        if(x == x2):
            break
        if(y == y2):
            break

t = 0
for f in g:
    for j in f:
        if j > 1:
            t+=1
