import json

with open("posts.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    posts = data["posts"]

for post in posts:
    title = post['title']
    print(f"Pealkiri: {title}")

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

average = reactions_sum / len(post)

print("Keskmine reaktsioonide arv:", average)