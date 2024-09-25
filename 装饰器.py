import time

def decorator(func):#用于测量函数运行时间的装饰器
    def wrapper(*args,**kwargs):#! *args表示位置参数，**kwargs表示关键字参数
        start_time=time.time()
        print(f'{func.__name__} is running.')
        
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f'{func.__name__} execution time :{end_time-start_time}s')
        return result
    return wrapper
@decorator
def square(x):
    return x*x
#装饰器的使用
#第一种
decorated_square=decorator(square)
decorated_square(10)
#第二种

square(10)
def timer(threshold):
    def decorator(func):
        def wrapper(*args,**kwargs):
            start_time=time.time()
            result=func(*args,**kwargs)
            end_time=time.time()
            if end_time-start_time>threshold:
                print(f'{func.__name__} took longer than {threshold}s')
            return result
        return wrapper
    return decorator
@timer(0.2)
def sleep():
    time.sleep(0.4)
sleep()