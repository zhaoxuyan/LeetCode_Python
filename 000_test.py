capitals = {'Iowa': 'DesMoines', 'Wisconsin': 'Madison'}
print(capitals['Iowa'])
capitals['Utah'] = 'SaltLakeCity'
print(capitals)
capitals['California'] = 'Sacramento'
print(len(capitals))
for k in capitals:
    print(capitals[k], " is the capital of ", k)
