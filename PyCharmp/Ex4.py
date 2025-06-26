import collections

from attr.validators import max_len


def sparse_vector_dot_product(v1:collections.defaultdict, v2:collections.defaultdict):
    ml = max(max(v1.keys(), default=0), max(v2.keys(), default=0)) + 1
    dot_product = sum(v1[i] * v2[i] for i in range(ml))
    return dot_product

v1 = collections.defaultdict(float, {"a": 5, "b":7})
v2 = collections.defaultdict(float, {"a": 2, "b":4, "c":3})

print(sparse_vector_dot_product(v1, v2))
