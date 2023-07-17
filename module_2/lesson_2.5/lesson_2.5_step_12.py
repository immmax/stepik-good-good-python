# ----------------------------------------------------------- #
# DATE: 2023.07.16                                            #
# AUTHOR: Maxim Datskiy                                       #
# GitHub: https://github.com/immmax                           #
# Stepik: https://stepik.org/users/525951056/profile          #
# ----------------------------------------------------------- #
# Добрый, добрый Python - обучающий курс от Сергея Балакирева #
# ----------------------------------------------------------- #
# Модуль 2 - Мои первые шаги в Python                         #
# Урок 2.4 - Логический тип Bool. Операторы сравнения         #
# ----------------------------------------------------------- #
#           https://stepik.org/lesson/567024                  #
# ----------------------------------------------------------- #
#           Шаг 12/12                                         #
# ----------------------------------------------------------- #

# Подвиг 11. Вводится вещественное число. Нужно проверить, что оно
#            попадает или в диапазон [0; 2] или в диапазон [10; 20] (включительно).
#            На экран вывести True, если попадает и False - в противном случае.
#            Задача делается без использования условного оператора.

# ----------------------------------------------------------- #

number = float(input())
print(0 <= number <= 2 or 10 <= number <= 20)