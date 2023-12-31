# ----------------------------------------------------------- #
# DATE: 2023.07.16                                            #
# AUTHOR: Maxim Datskiy                                       #
# GitHub: https://github.com/immmax                           #
# Stepik: https://stepik.org/users/525951056/profile          #
# ----------------------------------------------------------- #
# Добрый, добрый Python - обучающий курс от Сергея Балакирева #
# ----------------------------------------------------------- #
# Модуль 2 - Мои первые шаги в Python                         #
# Урок 2.4 - Функции print и input                            #
# ----------------------------------------------------------- #
#           https://stepik.org/lesson/567023                  #
# ----------------------------------------------------------- #
#           Шаг 5/13                                          #
# ----------------------------------------------------------- #

# Подвиг 4. Допишите программу, в которой вводятся два слова
#           (в переменные s1 и s2) в одну строчку через пробел, 
#           и отображаются в консоли в формате:
#               Word 1: s1 | Word 2: s2

# ----------------------------------------------------------- #

# ввод данных
s1, s2 = map(str.strip, input().split())

# здесь продолжите программу
print(f'Word 1: {s1} | Word 2: {s2}')