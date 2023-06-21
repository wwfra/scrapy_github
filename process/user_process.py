# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/19
"""
import json

# user_fol数据处理
with open("../spiders/user_fol.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    # 处理star
    star = data[i]["user_3_star"]
    if 'k' in star:
        star = int(float(star[:-1]) * 1000)
        data[i]["user_3_star"] = star
    else:
        star = int(star)
        data[i]["user_3_star"] = star
    # 处理repo
    repo = data[i]["user_4_repo"]
    if 'k' in repo:
        repo = int(float(repo[:-1]) * 1000)
        data[i]["user_4_repo"] = repo
    else:
        repo = int(repo)
        data[i]["user_4_repo"] = repo
    # 处理follower
    follower = data[i]["user_5_follower"]
    if 'k' in follower:
        follower = int(float(follower[:-1]) * 1000)
        data[i]["user_5_follower"] = follower
    else:
        follower = int(follower)
        data[i]["user_5_follower"] = follower
    # 处理following
    following = data[i]["user_6_following"]
    if 'k' in following:
        following = int(float(following[:-1]) * 1000)
        data[i]["user_6_following"] = following
    else:
        following = int(following)
        data[i]["user_6_following"] = following

sorted_data = sorted(data, key=lambda x: int(x["user_5_follower"]), reverse=True)

with open("../visualization/user_fol.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)

# user_repo数据处理
with open("../spiders/user_repo.json", encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    follower = data[i]["user_5_follower"]
    if 'k' in follower:
        follower = int(float(follower[:-1]) * 1000)
        data[i]["user_5_follower"] = follower
    else:
        follower = int(follower)
        data[i]["user_5_follower"] = follower

sorted_data = sorted(data, key=lambda x: int(x["user_5_follower"]), reverse=True)

with open("../visualization/user_repo.json", "w", encoding='utf-8') as file:
    json.dump(sorted_data, file)
