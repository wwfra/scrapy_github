# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/19
"""
import json

# org_fol数据处理
with open("../spiders/org_fol.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    fork = data[i]["org_4_follower"]
    if 'k' in fork:
        fork = int(float(fork[:-1]) * 1000)
        data[i]["org_4_follower"] = fork

sorted_data = sorted(data, key=lambda x: int(x["org_4_follower"]), reverse=True)

with open("../visualization/org_fol.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)

# org_repo数据处理
with open("../spiders/org_repo.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    fork = data[i]["org_3_repo"]
    if 'k' in fork:
        fork = int(float(fork[:-1]) * 1000)
        data[i]["org_3_repo"] = fork

sorted_data = sorted(data, key=lambda x: int(x["org_3_repo"]), reverse=True)

with open("../visualization/org_repo.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)
