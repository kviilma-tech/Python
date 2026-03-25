import requests

URL = "https://dummyjson.com/posts"
r = requests.get(URL)
data = r.json()
posts = data["posts"]

def get_reactions(post):
    return post["reactions"]["likes"] + post["reactions"]["dislikes"]

for post in posts:
    print(post["title"])

max_post = posts[0]

for post in posts:
    if get_reactions(post) > get_reactions(max_post):
        max_post = post

print("Kõige rohkem reaktsioone:", max_post["title"])

views_sum = 0

for post in posts:
    views_sum += post["views"]

print("Vaatamisi kokku:", views_sum)

reactions_sum = 0

for post in posts:
    reactions_sum += get_reactions(post)

average = reactions_sum / len(posts)

print("Keskmine reaktsioonide arv:", average)