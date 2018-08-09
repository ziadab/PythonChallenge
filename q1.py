print('Put your list number \nExemple: 1 2 3 64 98 4  5 7 5 47 ... be sure to make space between each number ')
l = input('>>> ')
l = list((l.split(' ')))

for item in l:
    print(item + '^2 =',str(int(item) * int(item)))

