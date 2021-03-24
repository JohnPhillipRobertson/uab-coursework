

class User:

    def __init__(self, password, email):
        self.password = hash(password)
        self.email = email
        self.logged_in = False
        self.videos = set()
        self.liked_videos = set()

    def login(self):
        self.logged_in = True

    def logout(self):
        self.logged_in = False

    def add_video(self, video):
        self.videos.add(video)

    def like(self, video):
        if video not in self.liked_videos:
            self.liked_videos.add(video)
        if video in self.liked_videos:
            self.liked_videos.remove(video)
            # It's standard like behavior to make like unlike if already like
