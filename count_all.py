def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    a=0
    b=0
    for i in txt:
        if i.isdigit():
            a+=1
        else:
            b+=1
    f={}
    f['LETTERS']=a
    f["DIGITS"]=b
    return f
print(count_all("Hello 777"))
#${ "LETTERS":  10, "DIGITS": 0 }