
videoСardsNumber = int(input('Введите количество видеокарт: '))

videoСards = []
newVideoCardsList = []
maxItem = 0

for item in range(videoСardsNumber):

    videoСards.append(int(input(f'Видеокарта {item + 1}: ')))

if videoСards[item] > maxItem:
    maxItem = videoСards[item]

for item in range(videoСardsNumber):
    if videoСards[item] != maxItem:
        newVideoCardsList.append(videoСards[item])

print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoСardsNumber):
    print(videoСards[item], end=' ')
print(']')

print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
    print(newVideoCardsList[item], end=' ')
print(']')