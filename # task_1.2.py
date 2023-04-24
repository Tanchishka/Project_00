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