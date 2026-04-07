import requests

<<<<<<< HEAD
with open("posts.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    posts = data["posts"]
=======
URL = "https://dummyjson.com/posts"
r = requests.get(URL)
data = r.json()
posts = data["posts"]

max_post = posts[0]
views_sum = 0
reactions_sum = 0
>>>>>>> eb4c1ec53b7396920d32243e679bd658e331e1c5

for post in posts:
    title = post['title']
    print(f"Pealkiri: {title}")

    likes = post["reactions"]["likes"]
    dislikes = post["reactions"]["dislikes"]
    kokku = likes + dislikes

    max_likes = max_post["reactions"]["likes"] + max_post["reactions"]["dislikes"]

    if kokku > max_likes:
        max_post = post

    views_sum += post["views"]
    reactions_sum += kokku

average = reactions_sum / len(post)

print("Kõige rohkem reaktsioone:", max_post["title"])
print("Vaatamisi kokku:", views_sum)
print("Keskmine reaktsioonide arv:", average)