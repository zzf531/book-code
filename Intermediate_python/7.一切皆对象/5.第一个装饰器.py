from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("之前")
        a_func()  # 调用来才返回自己
        print("之后")
    return wrapTheFunction


@a_new_decorator
def a():
    print("装饰器消除恶臭")

a()
ab = a_new_decorator(a)
print(a.__name__)



