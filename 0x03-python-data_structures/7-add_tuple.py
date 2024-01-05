#!/usr/bin/python3
# def add_tuple(tuple_a=(), tuple_b=()):
#     if len(tuple_a) < 2:
#         a = tuple_a[0] + tuple_b[0]
#         b = tuple_b[1]
#     elif len(tuple_b) < 2 and len(tuple_b) > 0:
#         a = tuple_a[0] + tuple_b[0]
#         b = tuple_a[1]
#     elif len(tuple_b) == 0:
#         a = tuple_a[0]
#         b = tuple_a[1]
#     else:
#         a = tuple_a[0] + tuple_b[0]
#         b = tuple_a[1] + tuple_b[1]

#     return (a, b)


def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (a1 + b1, a2 + b2)
