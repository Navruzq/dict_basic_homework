def first_item():
    """
    Given a dictionary, Return first item value.
    """
    data = {'a': 1, 'b': 2}
    while data:
        k,v=data.popitem()
    return v
print(first_item())

