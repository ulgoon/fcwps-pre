class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print(line)


ppap = Song(["I have a pen", "I have an apple", "uh!", "apple pen!"])
ppap.sing_a_song()
