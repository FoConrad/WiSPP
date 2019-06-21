a = 2+3 * 5
print('2+3 * 5 = {} (normal python is {}, expected {})'.format(a, 25, 17))

# Note the 1 and 20 takes precedence
if a  >  1 and 20: 
    print('More than 20!')
else:
    print('< 1 and True, or something...')
