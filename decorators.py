# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

'''def print_result(test):
    def wrapper(*arg):
        rtn = test(*arg)
        print(test.__name__)
        if type(rtn) == list:

            for x in rtn:
                print(x)
        elif type(rtn) == dict:

            for k, v in rtn.items():
                print(k, '=', v)
        else:
            print(rtn)
        return rtn

                # test(*arg)

    return wrapper'''

def print_result(func):
    def new_func(*args):
        res = func(*args)
        print(func.__name__)
        if type(res) == list:
            [print(x) for x in res]
        elif type(res) == dict:
            [print(key,'=',value) for key,value in res.items()]
        else:
            print(res)
        return(res)
    return new_func
