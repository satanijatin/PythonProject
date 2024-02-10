def tuple_extend(tuple1, tuple2):
    return tuple1 + tuple2


tuple1 = (1, 2, 3)
tuple2 = (4,)
extended_tuple = tuple_extend(tuple1, tuple2)
print("Extended Tuple:", extended_tuple)
