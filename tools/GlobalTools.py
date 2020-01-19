import copy

def deep_copy(obj):
    '''# 深copy数据 ,
    传入的对象 LIST 其他需要转换'''
    return copy.deepcopy(obj)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False