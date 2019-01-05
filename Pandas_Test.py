# coding=utf-8

import pandas as pd
import numpy

user_age = pd.Series(data = [18, 30, 25, 40])
#print(user_age)

user_age.index.name = "name"

#print(user_age)

user_age.name = "user_age_info"
#print(user_age)

name = pd.Index(['Tom', 'Bob', ])

#构建索引
name = pd.Index(["Tom", "Bob", "Mary", "Jame"], name = "name")
#构造Series
user_age = pd.Series(data = [18, 30, 25, 40], index = name, name = "user_age_info")


index = pd.Index(data = [1, 2, 3, 4])
data = {'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4]}

frame = pd.DataFrame(index = index, data = data)

frame
