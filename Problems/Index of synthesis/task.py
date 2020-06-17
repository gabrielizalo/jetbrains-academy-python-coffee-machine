index_synthesis = float(input())

if index_synthesis < 2:
    print('Analytic')
elif index_synthesis <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
