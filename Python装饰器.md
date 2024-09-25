# Python装饰器

**装饰器：将函数作为参数传递给函数，其本质上是一个函数，接收函数作为参数，并在自己内部根据传入函数定义一个新函数，并且扩展一些新的功能，装饰器将新函数返回**

==举例==

```python
import time

def decorator(func):#用于测量函数运行时间的装饰器
    def wrapper(*args,**kwargs):
        start_time=time.time()
        print(f'{func.__name__} is running.')
        
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f'{func.__name__} execution time :{end_time-start_time}s')
        return result
    return wrapper
def square(x):
    return x*x
#装饰器的使用
#第一种
decorated_square=decorator(square)
decorated_square(10)
#第二种
@decorator
square(10)
```

**装饰器生成器**

```python
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
```

==使用装饰器的原因==

- 提高代码复用，避免重复冗余代码
- 可以保证函数的逻辑清晰
- 通过装饰器，我们可以扩展别人的函数