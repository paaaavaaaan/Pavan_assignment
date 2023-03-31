def decorator_timer(func):
    from time import time
    def wrapper(a,b):
        t1 = time()
        result = func(a,b)
        end = time()-t1
        return result, end
    return wrapper
@decorator_timer
def my_add(a, b):
    res = a ** b
    return res
result,exec_time = my_add(400000 , 500000)
print(exec_time) 
