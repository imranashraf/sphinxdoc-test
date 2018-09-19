from sys import version_info

if version_info[0] == 3:
    PY3 = True
    from . import sum # first method for local import
    # from .sum import add # second method for local import
elif version_info[0] == 2:
    PY3 = False
else:
    raise EnvironmentError("sys.version_info refers to a version of "
        "Python neither 2 nor 3. This is not permitted. "
        "sys.version_info = {}".format(version_info))

def sub(a,b):
    """
    returns sum of two input numbers
    """
    print('addmul = {}'.format(sum.addmul(a,b)) ) # first method
    # print('sum = {}'.format(add(a,b)) ) # second method
    return a-b

def submul(a,b):
    """
    returns prod of two input numbers
    """
    return a*b-a*b
