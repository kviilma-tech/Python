import json

with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

for post in posts:
    print(post["title"])

max_post = posts[0]

for post in posts:
    reactions = post["reactions"]["likes"] + post["reactions"]["dislikes"]
    max_reactions = max_post["reactions"]["likes"] + max_post["reactions"]["dislikes"]
    
    if reactions > max_reactions:
        max_post = post

print("Kõige rohkem reaktsioone:", max_post["title"])

views_sum = 0

for post in posts:
    views_sum += post["views"]

print("Vaatamisi kokku:", views_sum)

reactions_sum = 0

for post in posts:
    reactions_sum += post["reactions"]["likes"] + post["reactions"]["dislikes"]

average = reactions_sum / len(posts)

print("Keskmine reaktsioonide arv:", average)