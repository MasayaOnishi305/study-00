import csv
import requests

name1 = 'ぜんいつ'
name2 = 'ねずこ'

if name2 != 'むざん':
    print(name2 + 'と'+ name1 + 'は仲間です')
else:
    print(str(name2) +'と'+ name1 + 'は仲間ではありません')

names = ["たんじろう","ぎゆう","ねずこ","むざん"]
names.append('ぜんいつ')

def print_character_name():
    for character_name in names:
        print(character_name)

print_character_name()

def check_names(name):
    if name in names:
        print(name+'は含まれます')
    else:
        print(name+'は含まれません')

check_names('ぎゆう')