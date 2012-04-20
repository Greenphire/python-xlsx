'''
Convert excel column names to integers and vice-versa
'''

from string import ascii_uppercase

def xlcol2num(x):
    '''
    >>> xlcol2num('A')
    1
    >>> xlcol2num('AA')
    27
    >>> xlcol2num('KN')
    300
    >>> xlcol2num('DKJ')
    3000
    >>> xlcol2num('GJH')
    5000
    '''
    if list(x) != [c for c in x if c in ascii_uppercase]:
        raise ValueError('Invalid excel column')
    return reduce(lambda s, a: s * 26 + ord(a) - ord('A') + 1, x, 0)

def num2xlcol(n):
    '''
    >>> num2xlcol(1)
    u'A'
    >>> num2xlcol(27)
    u'AA'
    >>> num2xlcol(300)
    u'KN'
    >>> num2xlcol(3000)
    u'DKJ'
    >>> num2xlcol(5000)
    u'GJH'
    '''
    if type(n) != int:
        raise ValueError('index must be an integer')
    if n < 1:
        raise ValueError('Index is too small')
    result = ""
    while True:
        if n > 26:
            n, r = divmod(n - 1, 26)
            result = chr(r + ord('A')) + result
        else:
            return unicode(chr(n + ord('A') - 1) + result)
