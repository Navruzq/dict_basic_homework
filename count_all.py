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
        elif i.isalpha():
            b+=1
  
    return {'LETTERS':b,"DIGITS":a}
print(count_all("Hello 777"))
