class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []

    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)

    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)

    def display_location(self):
        print("The location of the reel is:", self.location)

    def display_likes(self):
        print("The likes of the reel are:", self.likes)

    def display_comments(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("Comments on the reel:")
            for comment in self.comments:
                print("-", comment)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def delete_last_comment(self):
        if len(self.comments) == 0:
            print("No comments to delete")
        else:
            self.comments.pop()


reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Anusha",
    "Bangalore"
)

reel1.liked()
reel1.add_comment("Nice reel!")
reel1.add_comment("Loved it")

reel2 = Instagram(
    "finance minister conference",
    "conference with friends",
    "Rahul",
    "Delhi"
)

reel2.liked()

reel1.display_likes()
reel2.display_likes()

reel1.display_comments()
reel1.delete_last_comment()
reel1.display_comments()

print(id(reel1))
print(id(reel2))