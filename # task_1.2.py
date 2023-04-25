import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
y = my_favorite_songs [0] [1], my_favorite_songs [1] [1], my_favorite_songs [2] [1], my_favorite_songs [3] [1], my_favorite_songs [4] [1], my_favorite_songs [5] [1], my_favorite_songs [6] [1], my_favorite_songs [7] [1], my_favorite_songs [8] [1]

sampling = sum(random.choices(y, k=3))
print("Три песни звучат {} минут".format(sampling))
# как перевести рандомную цифру в время с помощью datetime мой мозг не может воспроизвести

# В y вы сделали кортеж. Этого было не обязательно. Можно было перебрать через цикл

time = 0
for song in random.sample(my_favorite_songs, 3):
    time += song[1]

print(f'Пункт C(A): Три песни звучат {round(time, 2)}')

# вот вариант перевода во время
from random import sample
from datetime import timedelta
from math import modf

time = 0
for song in sample(tuple(my_favorite_songs_dict), 3):
    time += my_favorite_songs_dict[song]

print(f'Пункт C(B): Три песни звучат {round(time, 2)}')
