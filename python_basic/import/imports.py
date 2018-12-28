import sys
import random
from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')

# print(sys.path)
print(f"{courses[index]}'s index  = {index}")  # 1

choiced_course = random.choice(courses)
print(choiced_course)

import math

rad = math.radians(90)
print("sin(rad) = " + str(math.sin(rad)))

import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2018))

import os

print(os.getcwd())
print(os.__file__)  # C:\Anaconda3\lib\os.py
print(os.listdir())  # ['intro.py', 'my_module.py', '__pycache__']

print(os.stat('imports.py'))

mtime = os.stat('imports.py').st_mtime
print(datetime.datetime.fromtimestamp(mtime))

print(os.environ.get('OS'))
print(os.path.basename(r'c:\tmp\test.py'))
print(os.path.dirname(r'c:\tmp\test.py'))
print(os.path.split(r'c:\tmp\test.py'))
print(os.path.exists(r'c:\tmp\test.py'))
print(os.path.splitext('c:/tmp/test.py'))
print(dir(os.path))
# os.path.isdir()
# os.path.isfile()
