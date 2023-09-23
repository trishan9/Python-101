class InstaGram:
    def __init__(self, insta_user_name, full_name):
        self.insta_user_name = insta_user_name
        self.full_name = full_name
        self.followers = 0
        self.following = 0
    

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = InstaGram("trishan_wagle", "Trishan Wagle")
user2 = InstaGram("smarika9", "Smarika")
print(user1.insta_user_name, user1.full_name)

user1.follow(user2)
print(user1.followers, user1.following)
print(user2.followers, user2.following)