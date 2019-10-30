def decorator(func):
   def wrapper():
       print("Please write something:")
       func()
       print("It's test")
   return wrapper
def decorator2(func2):
   def wrapper2():
       print(str(input()))
       func2()
       print("444444444444")
   return wrapper2
@decorator
@decorator2
def print_text():
   print("Hi Sergey if you read it!")
print_text();

# что то пошло не так..
# второй заход..
# третий..
# четвертый...