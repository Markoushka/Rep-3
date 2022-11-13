# try:
#    assert 2+2 == 5, "wrong result"
# except AssertionError as error:
#     print("Heppend some error ", error)

# Unit test - нужны для того что бы проверить основной код на стабильную работу в разных ситуациях

def add(*args, **kwargs):    # *args - специальный параметр который может обезпечить передачу множества аргументов функции
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result += arg
        else:
            try:
                result += float(arg)
                continue
            except (ValueError, TypeError):
                pass
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result += arg
        else:
            try:
                result += float(arg)
                continue
            except (ValueError, TypeError):
                pass
    return result

def minus(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result -= arg
        else:
            try:
                result -= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result -= arg
        else:
            try:
                result -= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    return result

def multiply(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result *= arg
        else:
            try:
                result *= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result *= arg
        else:
            try:
                result *= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    return result

def devide(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result /= arg
        else:
            try:
                result /= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == bool or type(arg) == float:
            result /= arg
        else:
            try:
                result /= float(arg)
                continue
            except (ValueError, TypeError):
                pass
    return result



