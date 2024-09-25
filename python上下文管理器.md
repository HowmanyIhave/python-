# Python上下文管理器

##  什么是上下文管理器

- 一个上下文管理器就是一个对象

- 定义了运行时的上下文

- 使用with语句来执行

	- ```python
		with context as ctx:
		    #使用这个上下文对象
		    #执行代码
		#自动关闭    
		```

	- 使用open打开的对象是一个上下文管理器对象

		- ```python
			import time
			class Timer:#上下文管理对象类
			    def __init__(self):
			        self.elapsed=0
			    def __enter__(self):
			        self.start_time=time.perf_counter()
			        return self#返回的是一个Timer()类的对象
			    def __exit__(self,exc_type,exc_val,exc_tb):
			        self.stop_time=time.perf_counter()
			        self.elsapsed=self.stop_time-self.start_time
			
			with Timer() as timer:#在执行这行代码时调用__enter__函数，Timer()生成一个Timer对象调用__enter__对象返回一个Timer类给timer
			    nums=[]
			    for n in range(1000):
			        nums.append(n**2)
			    #当离开这个with语句时执行__exit__语句    
			print(timer.elapsed)
			```

		- 可重用性高