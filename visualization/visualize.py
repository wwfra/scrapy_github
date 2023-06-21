# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/19
"""
"""
参数：
org 组织  :   followers,repos
user用户  :   followers,repos
repo仓库  :   stars,forks

1.双饼图
followers前百中用户/组织饼图
repos前百中用户/组织饼图

2.双折线
followers排行用户折线图
followers排行组织折线图

3.repos排行组织柱状图

仓库stars前十的标星、分支、观看次数
仓库forks前十的标星、分支、观看次数
"""
import json
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams['font.family'] = font.get_name()

# 1.followers前百中用户/组织饼图
# followers前百用户
with open("./user_fol.json", encoding='utf-8') as file:
    user_fol = json.load(file)
# followers前百组织
with open("./org_fol.json", encoding='utf-8') as file:
    org_fol = json.load(file)
# repos前百用户
with open("./user_repo.json", encoding='utf-8') as file:
    user_repo = json.load(file)
# repos前百组织
with open("./org_repo.json", encoding='utf-8') as file:
    org_repo = json.load(file)

value_fol = [len(user_fol), len(org_fol)]
value_repo = [len(user_repo), len(org_repo)]
labels = ['User', 'Organization']
colors = ['#4cafe8', '#ef5656']

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].pie(value_fol, labels=labels, colors=colors, autopct='%1.1f%%', explode=[0, 0.1])
axs[0].set_title('Followers前百比例图')
axs[1].pie(value_repo, labels=labels, colors=colors, autopct='%1.1f%%')
axs[1].set_title('Repos前百比例图')

plt.show()

# 2.followers排行用户/组织双折线图
user_fol_num = []
user_fol_index = []
for i in range(len(user_fol)):
    user_num = user_fol[i]["user_5_follower"]
    user_fol_num.append(user_num)
    user_fol_index.append(i + 1)
org_fol_num = []
org_fol_index = []
for i in range(len(org_fol)):
    org_num = org_fol[i]["org_4_follower"]
    org_fol_num.append(org_num)
    org_fol_index.append(i + 1)

fig, axs = plt.subplots(figsize=(12, 6))
axs.plot(user_fol_index, user_fol_num, label='User')
axs.plot(org_fol_index, org_fol_num, label='Organization')
axs.legend()
plt.xlabel('Index')
plt.ylabel('Followers')
plt.title('Followers前百用户/组织粉丝量对比图')

plt.show()

# 3.repos排行组织柱状图
org_repo_num = []
org_repo_name = []
for i in range(len(org_repo)):
    org_num = org_repo[i]["org_3_repo"]
    org_name = org_repo[i]["org_2_page"]
    org_repo_num.append(org_num)
    org_repo_name.append(org_name[19:])
fig, axs = plt.subplots(figsize=(12, 8))
axs.bar(org_repo_name, org_repo_num)
plt.xticks(rotation=90)
plt.xlabel('Organization')
plt.ylabel('RepoNum')
plt.title('Repos前百组织仓库数柱状图')

plt.show()

# stars前百仓库
with open("./repo_star.json", encoding='utf-8') as file:
    repo_star = json.load(file)
# forks前百仓库
with open("./repo_fork.json", encoding='utf-8') as file:
    repo_fork = json.load(file)

# stars仓库名、星、观看、分支
repo_star_num = []
repo_star_name = []
repo_star_fork = []
repo_star_watch = []
for i in range(20):
    repo_num = repo_star[i]["repo_2_star"]
    repo_name = repo_star[i]["repo_1_name"]
    repo_name = repo_name.split('/')[1]
    repo_s_fork = repo_star[i]["repo_4_fork"]
    repo_watch = repo_star[i]["repo_3_watch"]
    repo_star_num.append(repo_num)
    repo_star_name.append(repo_name)
    repo_star_fork.append(repo_s_fork)
    repo_star_watch.append(repo_watch)

# forks仓库名、星、观看、分支
repo_fork_num = []
repo_fork_name = []
repo_fork_star = []
repo_fork_watch = []
for i in range(20):
    repo_num = repo_fork[i]["repo_4_fork"]
    repo_name = repo_fork[i]["repo_1_name"]
    repo_name = repo_name.split('/')[1]
    repo_f_star = repo_fork[i]["repo_2_star"]
    repo_watch = repo_fork[i]["repo_3_watch"]
    repo_fork_num.append(repo_num)
    repo_fork_name.append(repo_name)
    repo_fork_star.append(repo_f_star)
    repo_fork_watch.append(repo_watch)

fig, axs = plt.subplots(2, 3, figsize=(12, 6))
# stars仓库名、星、观看、分支
axs[0, 0].plot(repo_star_name, repo_star_num)
axs[0, 0].set_xticklabels(repo_star_name, rotation=90, fontsize=6)
# axs[0, 0].set_xticks(repo_star_name[::2])
axs[0, 0].set_title('stars前20仓库收藏量')

axs[0, 1].plot(repo_star_name, repo_star_fork)
axs[0, 1].set_xticklabels(repo_star_name, rotation=90, fontsize=6)
# axs[0, 1].set_xticks(repo_star_name[::2])
axs[0, 1].set_title('stars前20仓库分支数')

axs[0, 2].plot(repo_star_name, repo_star_watch)
axs[0, 2].set_xticklabels(repo_star_name, rotation=90, fontsize=6)
# axs[0, 2].set_xticks(repo_star_name[::2])
axs[0, 2].set_title('stars前20仓库浏览量')

# forks仓库名、星、观看、分支
axs[1, 0].plot(repo_fork_name, repo_fork_star)
axs[1, 0].set_xticklabels(repo_fork_name, rotation=90, fontsize=6)
# axs[1, 0].set_xticks(repo_fork_name[::2])
axs[1, 0].set_title('forks前20仓库收藏量')

axs[1, 1].plot(repo_fork_name, repo_fork_num)
axs[1, 1].set_xticklabels(repo_fork_name, rotation=90, fontsize=6)
# axs[1, 1].set_xticks(repo_fork_name[::2])
axs[1, 1].set_title('forks前20仓库分支数')

axs[1, 2].plot(repo_fork_name, repo_fork_watch)
axs[1, 2].set_xticklabels(repo_fork_name, rotation=90, fontsize=6)
# axs[1, 2].set_xticks(repo_fork_name[::2])
axs[1, 2].set_title('forks前20仓库浏览量')

plt.show()
