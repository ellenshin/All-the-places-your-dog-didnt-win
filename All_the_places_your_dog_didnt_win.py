rank = int(input('Placement of your dog: '))

list = []

for i in range(0, 101):
    if i != rank:
        if i < 20 and i > 10:
            list.append(str(i) + 'th')
        else:
            if i % 10 == 1:
                list.append(str(i) + 'st')
            elif i % 10 == 2:
                list.append(str(i) + 'nd')
            elif i % 10 == 3:
                list.append(str(i) + 'rd')
            else:
                list.append(str(i) + 'th')

ans = ''
for i in list:
    ans = ans + i + ', '

print(ans)