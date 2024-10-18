def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  
print_params(b=25) 
print_params(c=[1, 2, 3]) 


values_list = [1, True, 'String']
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = [5.11, 'String']

print_params(*values_list)  
print_params(**values_dict) 
print_params( 42, *values_list_2)  
