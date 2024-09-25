import time
class Timer:#上下文管理对象类
    def __init__(self):
        self.elapsed=0
    def __enter__(self):
        self.start_time=time.perf_counter()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.stop_time=time.perf_counter()
        self.elsapsed=self.stop_time-self.start_time

with Timer() as timer:#!在执行这行代码时调用__enter__函数
    nums=[]
    for n in range(1000):
        nums.append(n**2)
    #当离开这个with语句时执行__exit__语句    
print(timer.elapsed)