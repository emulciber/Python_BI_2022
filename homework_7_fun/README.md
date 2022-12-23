# Homework 7: Functional programming

File ```functional.py``` contains next functions:
* __sequential_map(*functions, container)__ - takes several functions and a container with values and returns sequential execution of this functions to values in container.
* __consensus_filter(*functions, container)__ - takes several functions (with bool return) and a container with values and returns only values with True in all functions.
* __conditional_reduce(function, function, container)__ - a first function takes one argument and returns True or False, then a second function takes two arguments and do _reduce_ analogue on True values from the first function.
* __func_chain(*functions)__ - returns a chain from sequential execution of functions.
* __multiple_partial(*functions, **kwargs)__ - a _partial_ function analogue that takes several functions and returns several "partial" functions.
* __print(*args, sep=sep, end=end, file=file)__ - the analogue of "print" function.
