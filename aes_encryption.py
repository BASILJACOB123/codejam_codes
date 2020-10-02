plain_text=[]
cipher_text=[]
inp=[]
w=[]
l=[]
sbox=[[['6','3'],['7','C'],['7','7'],['7','B'],['F','2'],['6','B'],['6','F'],['C','5'],['3','0'],['0','1'],['6','7'],['2','B'],['F','E'],['D','7'],['A','B'],['7','6']],
[['C','A'],['8','2'],['C','9'],['7','D'],['F','A'],['5','9'],['4','7'],['F','0'],['A','D'],['D','4'],['A','2'],['A','F'],['9','C'],['A','4'],['7','2'],['C','0']],
[['B','7'],['F','D'],['9','3'],['2','6'],['3','6'],['3','F'],['F','7'],['C','C'],['3','4'],['A','5'],['E','5'],['F','1'],['7','1'],['D','8'],['3','1'],['1','5']],
[['0','4'],['C','7'],['2','3'],['C','3'],['1','8'],['9','6'],['0','5'],['9','A'],['0','7'],['1','2'],['8','0'],['E','2'],['E','B'],['2','7'],['B','2'],['7','5']],
[['0','9'],['8','3'],['2','C'],['1','A'],['1','B'],['6','E'],['5','A'],['A','0'],['5','2'],['3','B'],['D','6'],['B','3'],['2','9'],['E','3'],['2','F'],['8','4']],
[['5','3'],['D','1'],['0','0'],['E','D'],['2','0'],['F','C'],['B','1'],['5','B'],['6','A'],['C','B'],['B','E'],['3','9'],['4','A'],['4','C'],['5','8'],['C','F']],
[['D','0'],['E','F'],['A','A'],['F','B'],['4','3'],['4','D'],['3','3'],['8','5'],['4','5'],['F','9'],['0','2'],['7','F'],['5','0'],['3','C'],['9','F'],['A','8']],
[['5','1'],['A','3'],['4','0'],['8','F'],['9','2'],['9','D'],['3','8'],['F','5'],['B','C'],['B','6'],['D','A'],['2','1'],['1','0'],['F','F'],['F','3'],['D','2']],
[['C','D'],['0','C'],['1','3'],['E','C'],['5','F'],['9','7'],['4','4'],['1','7'],['C','4'],['A','7'],['7','E'],['3','D'],['6','4'],['5','D'],['1','9'],['7','3']],
[['6','0'],['8','1'],['4','F'],['D','C'],['2','2'],['2','A'],['9','0'],['8','8'],['4','6'],['E','E'],['B','8'],['1','4'],['D','E'],['5','E'],['0','B'],['D','B']],
[['E','0'],['3','2'],['3','A'],['0','A'],['4','9'],['0','6'],['2','4'],['5','C'],['C','2'],['D','3'],['A','C'],['6','2'],['9','1'],['9','5'],['E','4'],['7','9']],
[['E','7'],['C','8'],['3','7'],['6','D'],['8','D'],['D','5'],['4','E'],['A','9'],['6','C'],['5','6'],['F','4'],['E','A'],['6','5'],['7','A'],['A','E'],['0','8']],
[['B','A'],['7','8'],['2','5'],['2','E'],['1','C'],['A','6'],['B','4'],['C','6'],['E','8'],['D','D'],['7','4'],['1','F'],['4','B'],['B','D'],['8','B'],['8','A']],
[['7','0'],['3','E'],['B','5'],['6','6'],['4','8'],['0','3'],['F','6'],['0','E'],['6','1'],['3','5'],['5','7'],['B','9'],['8','6'],['C','1'],['1','D'],['9','E']],
[['E','1'],['F','8'],['9','8'],['1','1'],['6','9'],['D','9'],['8','E'],['9','4'],['9','B'],['1','E'],['8','7'],['E','9'],['C','E'],['5','5'],['2','8'],['D','F']],
[['8','C'],['A','1'],['8','9'],['0','D'],['B','F'],['E','6'],['4','2'],['6','8'],['4','1'],['9','9'],['2','D'],['0','F'],['B','0'],['5','4'],['B','B'],['1','6']]]

invsbox=[[['5','2'],['0','9'],['6','A'],['D','5'],['3','0'],['3','6'],['A','5'],['3','8'],['B','F'],['4','0'],['A','3'],['9','E'],['8','1'],['F','3'],['D','7'],['F','B']],
[['7','C'],['E','3'],['3','9'],['8','2'],['9','B'],['2','F'],['F','F'],['8','7'],['3','4'],['8','E'],['4','3'],['4','4'],['C','4'],['D','E'],['E','9'],['C','B']],
[['5','4'],['7','B'],['9','4'],['3','2'],['A','6'],['C','2'],['2','3'],['3','D'],['E','E'],['4','C'],['9','5'],['0','B'],['4','2'],['F','A'],['C','3'],['4','E']],
[['0','8'],['2','E'],['A','1'],['6','6'],['2','8'],['D','9'],['2','4'],['B','2'],['7','6'],['5','B'],['A','2'],['4','9'],['6','D'],['8','B'],['D','1'],['2','5']],
[['7','2'],['F','8'],['F','6'],['6','4'],['8','6'],['6','8'],['9','8'],['1','6'],['D','4'],['A','4'],['5','C'],['C','C'],['5','D'],['6','5'],['B','6'],['9','2']],
[['6','C'],['7','0'],['4','8'],['5','0'],['F','D'],['E','D'],['B','9'],['D','A'],['5','E'],['1','5'],['4','6'],['5','7'],['A','7'],['8','D'],['9','D'],['8','4']],
[['9','0'],['D','8'],['A','B'],['0','0'],['8','C'],['B','C'],['D','3'],['0','A'],['F','7'],['E','4'],['5','8'],['0','5'],['B','8'],['B','3'],['4','5'],['0','6']],
[['D','0'],['2','C'],['1','E'],['8','F'],['C','A'],['3','F'],['0','F'],['0','2'],['C','1'],['A','F'],['B','D'],['0','3'],['0','1'],['1','3'],['8','A'],['6','B']],
[['3','A'],['9','1'],['1','1'],['4','1'],['4','F'],['6','7'],['D','C'],['E','A'],['9','7'],['F','2'],['C','F'],['C','E'],['F','0'],['B','4'],['E','6'],['7','3']],
[['9','6'],['A','C'],['7','4'],['2','2'],['E','7'],['A','D'],['3','5'],['8','5'],['E','2'],['F','9'],['3','7'],['E','8'],['1','C'],['7','5'],['D','F'],['6','E']],
[['4','7'],['F','1'],['1','A'],['7','1'],['1','D'],['2','9'],['C','5'],['8','9'],['6','F'],['B','7'],['6','2'],['0','E'],['A','A'],['1','8'],['B','E'],['1','B']],
[['F','C'],['5','6'],['3','E'],['4','B'],['C','6'],['D','2'],['7','9'],['2','0'],['9','A'],['D','B'],['C','0'],['F','E'],['7','8'],['C','D'],['5','A'],['F','4']],
[['1','F'],['D','D'],['A','8'],['3','3'],['8','8'],['0','7'],['C','7'],['3','1'],['B','1'],['1','2'],['1','0'],['5','9'],['2','7'],['8','0'],['E','C'],['5','F']],
[['6','0'],['5','1'],['7','F'],['A','9'],['1','9'],['B','5'],['4','A'],['0','D'],['2','D'],['E','5'],['7','A'],['9','F'],['9','3'],['C','9'],['9','C'],['E','F']],
[['A','0'],['E','0'],['3','B'],['4','D'],['A','E'],['2','A'],['F','5'],['B','0'],['C','8'],['E','B'],['B','B'],['3','C'],['8','3'],['5','3'],['9','9'],['6','1']],
[['1','7'],['2','B'],['0','4'],['7','E'],['B','A'],['7','7'],['D','6'],['2','6'],['E','1'],['6','9'],['1','4'],['6','3'],['5','5'],['2','1'],['0','C'],['7','D']]]

dic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

mix=[[2,3,1,1],
[1,2,3,1],
[1,1,2,3],
[3,1,1,2]]

invmix=[[['0','E'],['0','B'],['0','D'],['0','9']],
[['0','9'],['0','E'],['0','B'],['0','D']],
[['0','D'],['0','9'],['0','E'],['0','B']],
[['0','B'],['0','D'],['0','9'],['0','E']]]
hexx={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
rcon=[['0','0','0','0','0','0','0','1'],['0','0','0','0','0','0','1','0'],['0','0','0','0','0','1','0','0'],['0','0','0','0','1','0','0','0'],['0','0','0','1','0','0','0','0'],['0','0','1','0','0','0','0','0'],['0','1','0','0','0','0','0','0'],['1','0','0','0','0','0','0','0'],['0','0','0','1','1','0','1','1'],['0','0','1','1','0','1','1','0']]
#User Defined Functions:
def hex2bin(val):
    var=""
    var+=hexx[val]
    return var

def bin2hex(val):
    var1=""
    var2=""
    var1=str(val[0])+str(val[1])+str(val[2])+str(val[3])
    for key,value in hexx.items():
        if var1==value:
            var2+=key
    return var2

def dec2hex(val):
    for key,value in dic.items():
        if val==value:
            return key

def leftshift(val):
    temp=val[0]
    for i in range(1,4):
        val[i-1]=val[i]
    val[3]=temp

def gfunction(val,n):
    #Step a
    leftshift(val)
    x=[]
    #Step b
    for i in range(0,4):
        xx=[]
        xx.append(sbox[dic[val[i][0]]][dic[val[i][1]]][0])
        xx.append(sbox[dic[val[i][0]]][dic[val[i][1]]][1])
        x.append(xx)
    #Step c
    var=[]
    temp3=[]
    temp1=rcon[n-1]
    temp2=hexx[x[0][0]]+hexx[x[0][1]]
    for i in range(0,8):
        temp3.append(str(int(temp1[i])^int(temp2[i])))
    x[0][0]=bin2hex(temp3[0:4])
    x[0][1]=bin2hex(temp3[4:8])
    return x

def xorfunction(val1,val2):
    var=[]
    for i in range(0,4):
        var1=[]
        for j in range(0,2):
            var2=[]
            val1[i][j]=hex2bin(val1[i][j])
            val2[i][j]=hex2bin(val2[i][j])
            for k in range(0,4):
                var2.append(str(int(val1[i][j][k])^int(val2[i][j][k])))
            val1[i][j]=bin2hex(val1[i][j])
            val2[i][j]=bin2hex(val2[i][j])
            var2=str(bin2hex(var2))
            var1.append(var2)
        var.append(var1)
    return var

def xorfunction2(val1,val2):
    var1=[]
    val1=list(val1)
    val2=list(val2)
    for j in range(0,2):
        var2=[]
        val1[j]=hex2bin(val1[j])
        val2[j]=hex2bin(val2[j])
        for k in range(0,4):
            var2.append(str(int(val1[j][k])^int(val2[j][k])))
        val1[j]=bin2hex(val1[j])
        val2[j]=bin2hex(val2[j])
        var2=str(bin2hex(var2))
        var1.append(var2)
    return var1

def twofunction(val):
    t2=[0,0,0,1,1,0,1,1]
    temp1=hexx[val[0]]
    temp2=hexx[val[1]]
    temp=list(temp1+temp2)
    t1=temp[0]
    for i in range(1,8):
        temp[i-1]=temp[i]
    temp[7]='0'
    if(t1=='1'):
        for i in range(0,8):
            temp[i]=str(int(temp[i])^t2[i])
    ll=bin2hex(temp[0:4])
    rr=bin2hex(temp[4:8])
    temp=ll+rr
    return temp

def threefunction(val):
    temp1=list(val)
    temp1=twofunction(temp1)
    temp1=xorfunction2(temp1,val)
    return temp1

def efunction(val):
    return twofunction(xorfunction2(val,twofunction(xorfunction2(val,twofunction(val)))))

def bfunction(val):
    return xorfunction2(twofunction(xorfunction2(val,twofunction(twofunction(val)))),val)

def dfunction(val):
    return xorfunction2(twofunction(twofunction(xorfunction2(val,twofunction(val)))),val)

def ninefunction(val):
    return xorfunction2(val,twofunction(twofunction(twofunction(val))))
    
#Input Statements:
inp=input("Enter the key(32-bit hexadecimal): ")
#Joining two characters:
for i in range(0,32,2):
    var=[]
    var.append(inp[i])
    var.append(inp[i+1])
    l.append(var)
#Word Generation:
for i in range(0,16,4):
    var=[]
    var.append(l[i])
    var.append(l[i+1])
    var.append(l[i+2])
    var.append(l[i+3])
    w.append(var)
#Loop for key generation:
for i in range(0,10):
    new=[]
    for j in range(0,4):
        new.append(w[4*(i+1)-1][j])
    w.append(xorfunction(w[4*(i+1)-4],gfunction(new,i+1)))
    w.append(xorfunction(w[4*(i+1)],w[4*(i+1)-3]))
    w.append(xorfunction(w[4*(i+1)+1],w[4*(i+1)-2]))
    w.append(xorfunction(w[4*(i+1)+2],w[4*(i+1)-1]))
print("The Keys are:")
keyout=[]
for i in range(0,44,4):
    var=[]
    var.append(w[i])
    var.append(w[i+1])
    var.append(w[i+2])
    var.append(w[i+3])
    keyout.append(var)
for i in range(0,11):
    print("ROUND #",i)
    for j in range(0,4):
        for k in range(0,4):
            for m in range(0,2):
                print(keyout[i][j][k][m],end="")
    print("\n")
for k in range(0,11):
    keyout[k]=[[keyout[k][j][i] for j in range(len(keyout[k]))] for i in range(len(keyout[k][0]))]
#Encryption:
plain_text=input("Enter the plain_text text (128-bit binary or 16-bit hexadecimal): \n")
#Round 0:
#Joining two characters:
l=[]
for i in range(0,32,2):
    var=[]
    var.append(plain_text[i])
    var.append(plain_text[i+1])
    l.append(var)
#Word Generation:
w=[]
for i in range(0,16,4):
    var=[]
    var.append(l[i])
    var.append(l[i+1])
    var.append(l[i+2])
    var.append(l[i+3])
    w.append(var)
#Transpose function
w=[[w[j][i] for j in range(len(w))] for i in range(len(w[0]))]
print("\nInput:\n")
for j in range(0,4):
    for k in range(0,4):
        for m in range(0,2):
            print(w[j][k][m],end="")
        print(end=" ")
print("\n")
round0=[]
for j in range(0,4):
    var1=[]
    for k in range(0,4):
        var2=[]
        for m in range(0,2):
            var2.append(dec2hex(dic[keyout[0][j][k][m]]^dic[w[j][k][m]]))
        var1.append(var2)
    round0.append(var1)
print("After round 0: \n")
for j in range(0,4):
    for k in range(0,4):
        for m in range(0,2):
            print(round0[j][k][m],end="")
        print(end=" ")
print("\n")
#Loop for rounds 1-10:
for i in range(1,11):
    print("Round #",i,": \n")
    #Subs Bytes:
    asub=[]
    for j in range(0,4):
        var1=[]
        for k in range(0,4):
            var1.append(sbox[dic[round0[j][k][0]]][dic[round0[j][k][1]]])
        asub.append(var1)
    print("\nAfter Subs.Bytes: \n")
    for j in range(0,4):
        for k in range(0,4):
            for m in range(0,2):
                print(asub[j][k][m],end="")
            print(end=" ")
    print("\n")
    #Shift Rows:
    for j in range(1,4):
        right=asub[j][j::]
        left=asub[j][:j:]
        asub[j]=right+left
    print("\nAfter Shift Rows: \n")
    for j in range(0,4):
        for k in range(0,4):
            for m in range(0,2):
                print(asub[j][k][m],end="")
            print(end=" ")
    print("\n")
    amix=[]
    if(i!=10):
    #Mix columns:
        for j in range(0,4):
            var2=[]
            for k in range(0,4):
                var1=[]
                for h in range(0,4):
                    if(mix[j][h]==1):
                        var1.append(asub[h][k])
                    elif(mix[j][h]==2):
                        var1.append(list(twofunction(asub[h][k])))
                    else:
                        var1.append(list(threefunction(asub[h][k])))
                for h in range(1,4):
                    var1[0]=xorfunction2(var1[0],var1[h])
                    if(h==3):
                        var2.append(var1[0])
            amix.append(var2)
        print("After Mix Columns: ")
        for j in range(0,4):
            for k in range(0,4):
                for m in range(0,2):
                    print(amix[j][k][m],end="")
                print(end=" ")
        print("\n")
    #Add round key:
    if(i==10):
        amix=asub
    roundn=[]
    for j in range(0,4):
        var1=[]
        for k in range(0,4):
            var2=[]
            for m in range(0,2):
                var2.append(dec2hex(dic[keyout[i][j][k][m]]^dic[amix[j][k][m]]))
            var1.append(var2)
        roundn.append(var1)
    print("\nOutput of Round #",i,": \n")
    for j in range(0,4):
        for k in range(0,4):
            for m in range(0,2):
                print(roundn[j][k][m],end="")
            print(end=" ")
    print("\n")
    round0=roundn
cipher_text=[[round0[j][i] for j in range(len(round0))] for i in range(len(round0[0]))]
print("The cipher_text: ")
for j in range(0,4):
    for k in range(0,4):
        for m in range(0,2):
            print(cipher_text[j][k][m],end="")
        print(end=" ")
