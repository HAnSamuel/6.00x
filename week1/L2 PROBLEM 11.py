varA=7
varB=5
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')


# if (type(varA) or type(varB)) == str works totally different
# if the type of varA is int and varB is str, it means if (int or str) == str
# the result of int or str is int
