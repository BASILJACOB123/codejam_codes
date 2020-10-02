t=int(input())
z=0
for i in range(t):
    p=list(map(int,input().split()))
    r=p[3]
    c=p[4]
    s=list(input())
    l=[[r,c]]
    for i in range(len(s)):
        if(s[i]=='N'):
            if([r-1,c] not in l):
                [r,c]=[r-1,c]
                l.append([r,c])
            else:
                while([r-1,c] in l):
                    [r,c]=[r-1,c]
                [r,c]=[r-1,c]
                l.append([r,c])
                
        elif(s[i]=='S'):
            if([r+1,c] not in l):
                [r,c]=[r+1,c]
                l.append([r,c])
            else:
                while([r+1,c] in l):
                    [r,c]=[r+1,c]
                [r,c]=[r+1,c]
                l.append([r,c])
        elif(s[i]=='E'):
            if([r,c+1] not in l):
                [r,c]=[r,c+1]
                l.append([r,c])
            else:
                while([r,c+1] in l):
                    [r,c]=[r,c+1]
                [r,c]=[r,c+1]
                l.append([r,c])
                
                    
        else:
            if([r,c-1] not in l):
                [r,c]=[r,c-1]
                l.append([r,c])
            else:
                while([r,c-1] in l):
                    [r,c]=[r,c-1]
                [r,c]=[r,c-1]
                l.append([r,c])
    z=z+1
    print('Case #' +str(z) + ': ' + str(r) + ' ' +str(c))


        
