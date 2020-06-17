num_units = int(input())

if num_units < 1:
    print('no army')
elif num_units <= 9:
    print('few')
elif num_units <= 49:
    print('pack')
elif num_units <= 499:
    print('horde')
elif num_units <= 999:
    print('swarm')
else:
    print('legion')
