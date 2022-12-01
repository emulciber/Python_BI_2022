import sys
import numpy as np


# def sequential_map(*funs):
#     values = funs[-1]
#     for fun in funs[:-1]:
#         values = map(fun, values)
#     return list(values)


def sequential_map(*funs):
    values = funs[-1]
    all_fun = func_chain(*funs[:-1])
    answer = map(all_fun, values)
    return list(answer)


def consensus_filter(*funs):
    values = funs[-1]
    for fun in funs[:-1]:
        values = filter(fun, values)
    return list(values)


def conditional_reduce(*funs):
    values = funs[-1]
    values = list(filter(funs[0], values))
    answer = values[0]
    for value in values[1:]:
        answer = funs[1](value, answer)
    return answer


def func_chain(*funs):
    def inner_func(x):
        ans = x
        for fun in funs:
            ans = fun(ans)
        return ans
    return inner_func


def multiple_partial(*funs, **kwargs):

    def partial(fun, **kwargs):
        def inner_fun(x):
            return fun(x, **kwargs)
        return inner_fun

    partial_funs = []
    for fun in funs:
        partial_funs.append(partial(fun, **kwargs))

    return partial_funs


def print(*args, **kwargs):
    
    out_string = ''

    separator = kwargs['sep'] if 'sep' in kwargs.keys() else ' '
    ending = kwargs['end'] if 'end' in kwargs.keys() else '\n'

    for arg in args:
        out_string += str(arg) + separator

    out_string += ending

    if 'file' in kwargs.keys():
        kwargs['file'].write(out_string)
    else:
        sys.stdout.write(out_string)

