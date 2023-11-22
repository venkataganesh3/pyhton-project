#working of while loop
x=1
while x<=10:
    print(x)
    x+=1


x=10
while x>=0:
    print(x)
    x-=1
        
x=1
while x<11:
    print(x,end=' ')
    x+=1


x=1
while x<11:
    if x==6:
        break
    print(x)
    x+=1

x=0
while x<10:
    x+=1
    if x==6:
        continue
    print(x, end=' ')


x=0
while x<10:
    x+=1
    print(x,end=' ')
else:
    print('\ntask finished!')


x=0
while x<10:
    x+=1
    if x==5:
       continue
    print(x)

else:
    print('\ntask finished')


for x in range(10):
    print(x, end=' ')
else:
    print('\ntask finished!')


for x in  range[1,2,3,4,5,6]:
    print(x,end=' ')
else:
    print('\ntask finished!')


  

n=int(input('enter number:'))
if n%2==0:
    print('even')
else:
    print('odd')




sum=0
for i in range(0,10):
    if i%2==0:
        sum+=i
print(sum)



    
    
    
