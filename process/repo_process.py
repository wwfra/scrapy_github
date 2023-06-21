# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/19
"""
import json

# repo_fork数据处理
with open("../spiders/repo_fork.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    # 处理star
    star = data[i]["repo_2_star"]
    if 'k' in star:
        star = int(float(star[:-1]) * 1000)
        data[i]["repo_2_star"] = star
    else:
        star = int(star)
        data[i]["repo_2_star"] = star
    # 处理watch
    watch = data[i]["repo_3_watch"]
    if 'k' in watch:
        watch = int(float(watch[:-1]) * 1000)
        data[i]["repo_3_watch"] = watch
    else:
        watch = int(watch)
        data[i]["repo_3_watch"] = watch
    # 处理fork
    fork = data[i]["repo_4_fork"]
    if 'k' in fork:
        fork = int(float(fork[:-1]) * 1000)
        data[i]["repo_4_fork"] = fork
sorted_data = sorted(data, key=lambda x: int(x["repo_4_fork"]), reverse=True)
with open("../visualization/repo_fork.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)

# repo_star数据处理
with open("../spiders/repo_star.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    # 处理star
    star = data[i]["repo_2_star"]
    if 'k' in star:
        star = int(float(star[:-1]) * 1000)
        data[i]["repo_2_star"] = star
    # 处理watch
    watch = data[i]["repo_3_watch"]
    if 'k' in watch:
        watch = int(float(watch[:-1]) * 1000)
        data[i]["repo_3_watch"] = watch
    else:
        watch = int(watch)
        data[i]["repo_3_watch"] = watch
    # 处理fork
    fork = data[i]["repo_4_fork"]
    if 'k' in fork:
        fork = int(float(fork[:-1]) * 1000)
        data[i]["repo_4_fork"] = fork
    else:
        fork = int(fork)
        data[i]["repo_3_watch"] = fork
sorted_data = sorted(data, key=lambda x: int(x["repo_2_star"]), reverse=True)
with open("../visualization/repo_star.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)
