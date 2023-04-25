my_favorite_songs = ('Waste a Moment', 'Staying\' Alive', 'A Sorta Fairytale', 'Start Me Up', 'New Salvation')
print (my_favorite_songs[0], my_favorite_songs [-1], my_favorite_songs [1], my_favorite_songs[-2])

# Посмотрите внимательнее на условие задачи. Переопределять переменную my_favorite_songs нельзя!
# Нужно воспользоваться методом split для того чтобы перейти от строки к списку

# Решение с помощью метода split() и индексации списков
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
