#ex13
#Fibonacci number


def fibo(n):
    num_f=[0]
    if n==0:
        num_f=[]
    elif n==1:
        num_f=[1]
    elif n==2:
        num_f=[1,1]
    elif n>2:
        num_f=[1,1]
        for i in range(n-2):
            new_element=num_f[-1]+num_f[-2]
            num_f.append(new_element)
    return num_f
ask = int(input("How many fibonacci numbers do you want to generate?: "))
result=fibo(ask)
print(result)



