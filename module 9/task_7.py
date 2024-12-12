



def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        count = 0
        if result < 2:
            count += 1
        for i in range(result - 1, 1, -1):
            if result % i == 0:
                count += 1
                
        if count > 0:
            print('Составное')
        else: 
            print('Простое') 
        return result
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)



    
    

