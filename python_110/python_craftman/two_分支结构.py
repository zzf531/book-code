"""
德摩根定律
通俗的说，德摩根定律就是 not A or not B 等价于 not (A and B)
"""
a, b, c = 1, 2, 3
if not a > 4 or not b > 1:
    print('真的')

if not (a > 4 and b > 1):
    print('真的')


"""
2.自定义对象的"布尔真假"
python 的所有对象都有自己的“布尔真假”：
布尔值为假的对象：None, 0, False, [], (), {}, set(), frozenset(), ... ...
布尔值为真的对象：非 0 的数值、True，非空的序列、元组，普通的用户类实例, object()
>>> bool(object())
True

重点来了，虽然所有用户类实例的布尔值都是真。但是 Python 提供了改变这个行为的办法：
自定义类的 __bool__ 魔法方法 （在 Python 2.X 版本中为 __nonzero__）。
当类定义了 __bool__ 方法后，它的返回值将会被当作类实例的布尔值。
另外，__bool__ 不是影响实例布尔真假的唯一方法。如果类没有定义 __bool__ 方法，
Python 还会尝试调用 __len__ 方法*（也就是对任何序列对象调用 len 函数）*，
通过结果是否为 0 判断实例真假。
"""

class UserCollection(object):

    def __init__(self, users):
        self._users = users

users = UserCollection(['zzf',12])

if len(users._users) > 0:
    print(len(users._users))
    print("There's some users in collection!")

"""
上面的代码里，判断 UserCollection 是否有内容时用到了 users._users 的长度。其实，通过为 UserCollection 添加 __len__ 魔法方法，上面的分支可以变得更简单：
通过定义魔法方法 __len__ 和 __bool__ ，我们可以让类自己控制想要表现出的布尔真假值，让代码变得更 pythonic。
"""
class UserCollection2(object):
    def __init__(self, users):
        self._users = users
    def __len__(self):
        return len(self._users)

users = UserCollection2(['zzf',12])

if users:
    print('集合中有一些用户')


"""
all() 和 any() 两个函数非常适合在条件判断中使用。这两个函数接受一个可迭代对象，
返回一个布尔值，其中：
all(seq)：仅当 seq 中所有对象都为布尔真时返回 True，否则返回 False
any(seq)：只要 seq 中任何一个对象为布尔真就返回 True，否则返回 False
"""


'''
4. 使用 try/while/for 中 else 分支
'''
def do_stuff():
    first_thing_successed = False
    try:
        first_thing_successed = True
    except Exception as e:
        print('调用发生错误')
        return

    if first_thing_successed:
        return 'do_the_second_thing()'

def do_stuff2():
    try:
        a =123
    except Exception as e:
        print("Error while calling do_some_thing")
        return
    else:
        return a
