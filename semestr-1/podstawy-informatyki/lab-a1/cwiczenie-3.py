tab = []

for i in range(1, 10):
    print('Podaj liczbe:')
    tab.append(input())

print("len(tab) = ", len(tab))
for a in range(1, 10, 1):
    print(tab[9 - a])
