from sys import version_info

if version_info[0] == 3:
    PY3 = True
    from . import diff # first method for local import
    # from .diff import sub # second method for local import
elif version_info[0] == 2:
    PY3 = False
else:
    raise EnvironmentError("sys.version_info refers to a version of "
        "Python neither 2 nor 3. This is not permitted. "
        "sys.version_info = {}".format(version_info))

def add(a,b):
    """
    returns sum of two input numbers
    """
    print('submul = {}'.format(diff.submul(a,b)) ) # first method
    # print('diff = {}'.format(sub(a,b)) ) # second method
    return a+b

def addmul(a,b):
    """
    returns prod of two input numbers
    """
    return a*b+a*b
