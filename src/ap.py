from instaloader import Instaloader, Profile
from datetime import datetime
import json

USERNAME = "jimmykaneki@gmail.com"
PASSWORD = "Frejlord123"

loader = Instaloader()
loader.login(USERNAME, PASSWORD)

f = open("data/data_influencer.json")
data_influencer = json.load(f)
f.close()

hasil_scrape = []

for i in data_influencer:
	target_profile = i["Username"]

	try:
		profile = Profile.from_username(loader.context, target_profile[1:])

		total_num_likes = 0
		total_num_comments = 0
		total_num_posts = 0

		for post in profile.get_posts():
			total_num_likes += post.likes
			total_num_comments += post.comments
			total_num_posts += 1

		raw = {
			"Username": target_profile,
			"Posts": total_num_posts,
			"Likes": total_num_likes,
			"Comments": total_num_comments
		}
	except:
		raw = {
			"Username": target_profile,
			"Posts": 0,
			"Likes": 0,
			"Comments": 0
		}
	finally:
		raw["Scrapped_at"] = datetime.utcnow().isoformat()
		hasil_scrape.append(raw)
		print(raw)

f=open("data/hasil_scrape.json", "w")
json.dump(hasil_scrape, f, indent=4)
f.close()
