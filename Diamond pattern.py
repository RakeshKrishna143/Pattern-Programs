'''
Engineer's Revolution
Example :
n = 5
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        * 
'''
n = 7
for i in range(1,2*n):
    for j in range(1,2*n):
        if i+j>=n+1 and j-i<=n-1 and i-j<=n-1 and i+j<=3*n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
