
def get_sq(w, h):
    return w * h

def func_show(f):
    def inner(*args):
        res = f(*args)
        print (f"Площадь прямоуголтника: {res}")
        return res
    return inner

# @func_show
def get_sq(w, h):
    return w * h

if __name__ == '__main__':
    print(f'get_sq(12, 12) = {get_sq(12, 12)}')
