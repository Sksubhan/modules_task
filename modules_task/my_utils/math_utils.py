def is_prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
            break
    return 'prime' if c==0 else 'Not a prime'
