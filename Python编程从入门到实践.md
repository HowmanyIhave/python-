# Python编程从入门到实践

==本书学习从第八章开始==

==从本书开始作笔记方式开始改变，将不再对文章内容进行详细摘录，而是进行精简笔记，记录书籍页码，对文章内容进行补充或强调==

### 1. 128页 函数内修改或禁止修改传入参数

> - 在函数中传入列表作为参数，该列表直接在函数中被修改
>
> 	```python
> 	lis=[1,2,3]
> 	def solution(lis):
> 	    pass
> 	solution(lis) #将列表直接传入函数，该列表能被修改
> 	```
>
> - 向函数中传入列表副本，来解决参数在函数中被修改的问题
>
> 	```python
> 	lis=[1,2,3]
> 	def solution(lis):
> 	    pass
> 	solution(lis[:]) #将列表副本传入函数，该列表能避免被修改
> 	```

### 2. 175页 使用异常处理避免崩溃

> - ```python
> 	print('请输入两个数字进行除法操作！')
> 	print("输入'q'退出程序")
> 	while True:
> 	    first_number=input("第一个数字：")
> 	    if first_number=='q':
> 	        break
> 	    second_number=input("第二个数字：")
> 	    if second_number=='q':
> 	        break
> 	    try:
> 	        answer=int(first_number)/int(second_number)
> 	    except ZeroDivisionError:
> 	        print('0不能作除数') #或使用pass语句使程序静默失败
> 	    else:
> 	        print(answer)
> 	```
>
> - 使用else模块，如果try模块中的代码成功执行，将执行else模块中的语句

### 3. 180多页 对python的测试代码进行笔记

