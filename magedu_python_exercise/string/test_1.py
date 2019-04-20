sq = ['1', ['2', '2'], '3']
# print('\"'.join(map(str, sq)))
# print(sq)
sq = 'My name is watson'
# print('\n'.join(sq).splitlines())
print(sq.rsplit(None, maxsplit=1)[-1])
