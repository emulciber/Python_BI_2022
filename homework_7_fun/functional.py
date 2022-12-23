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
        answer = x
        for function in funs:
            answer = function(answer)
        return answer
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


def print(*args, sep=' ', end='\n', file=False):
    
    out_string = ''

    for arg in args:
        out_string += str(arg) + sep

    out_string += end

    if file:
        with open(file, 'w') as output_file:
            output_file.write(out_string)
    else:
        sys.stdout.write(out_string)

        