#!/usr/bin/python3

import csv


trener = ['', '','','','', '\\khis', '\\morev', '\\elis', '\\razor', '\\razzzzor',  '\\tre',  '\\gleb']
kur = ['\\olya','\\olya','\\olya','\\olya','\\olya', '\\olya', '\\olya', '\\olya', '\\sharich', '\\sharich',  '\\sharich',  '\\sharich']


with open('list.csv','r') as f:
    awards = csv.reader(f, delimiter=',')
    for row in awards:
        print('\dip{%s}{%s}{%s}{%s}{%s}' % (row[0], row[1], row[2], kur[int(row[0])], trener[int(row[0])]))


# \dip{5}{1}{Иван Иванов}{\olya}{\khis}

# \newcommand{\pok}{\fio{Н.\,В. Походня}\par методист кафедры математики}
# \newcommand{\olya}{\fio{О.\,С. Морозова}\par координатор олимпиадного \par движения} 
# \newcommand{\khis}{\fio{И.\,Ш. Хисамбеев}\par тренер параллели 5 классов}
# \newcommand{\morev}{\fio{К.\,В. Морев}\par тренер параллели 6 классов}
# \newcommand{\elis}{\fio{А.\,С. Елисеев}\par тренер параллели 7 классов}
# \newcommand{\sharich}{\fio{В.\,З. Шарич}\par заведующий кафедрой математики}
# \newcommand{\razor}{\fio{И.\,Н. Барышев}\par тренер параллели 8 классов}
# \newcommand{\razzzzor}{\fio{И.\,Н. Барышев}\par тренер параллели 9 классов}
# \newcommand{\tre}{\fio{В.\,Д. Трещев}\par тренер параллели 10 классов}
# \newcommand{\gleb}{\fio{Г.\,А. Погудин}\par тренер параллели 11 классов}
# \newcommand{\yurpal}{\fio{Ю.\,П. Николаев}\par заместитель директора\par по науке}
