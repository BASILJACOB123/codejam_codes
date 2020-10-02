# Driver code 
p = 3292937;
i, j, flag = 0, 0, 0;
for i in range(p,1,-1): 
    if (i == 1 or i == 0 or i==2): 
        continue; 
 
    flag = 1; 
  
    for j in range(2, ((i // 2) + 1), 1): 
        if (i % j == 0): 
            flag = 0; 
            break;
    if (flag == 1):
        if(p%i==0):
            print(i)
        
        

    


