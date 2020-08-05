def flip_list(lst):
    return [x[0] if isinstance(x, list) else [x] for x in lst]
