# ============================================================
# Exercise 3: Who is the song producer?
# Instructions:
# Create a Song class with a method to print lyrics line by line.
#
# Step 1: Create a Song class.
#         - __init__ takes lyrics (a list) as parameter.
#         - sing_me_a_song() prints each lyric on a new line.
# ============================================================

class Song:
    def __init__(self, lyrics):
        """
        Initialize a Song object.
        Parameters: lyrics (list): list of song lyric lines
        """
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Print each lyric line by line."""
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a lady who's sure",
                 "all that glitters is gold",
                 "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()
