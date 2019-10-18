def fibo (n,k):
    previous = 1
    current =  1
    
    for item in range(n-2):
        
        previous, current = current, current+ previous*k
        

    return current;

w = open("output.txt","w")
w.write(str(fibo(33,4)))
print(str(fibo(33,4)))