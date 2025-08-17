class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-wide info whenever a new song is created
        self.add_song_to_count()
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)
        Song.add_to_artist_count(self.artist)
        Song.add_to_genre_count(self.genre)

    # Increment total song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Add unique artists
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Add unique genres
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Create/update artist histogram
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    # Create/update genre histogram
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


# ----- Example usage -----
#song1 = Song("99 Problems", "Jay-Z", "Rap")
#song2 = Song("Halo", "Beyonce", "Pop")
#song3 = Song("God's Plan", "Drake", "Rap")

print("Total songs:", Song.count)             # 3
print("Artists:", Song.artists)               # ["Jay-Z", "Beyonce", "Drake"]
print("Genres:", Song.genres)                 # ["Rap", "Pop"]
print("Artist count:", Song.artist_count)     # {"Jay-Z": 1, "Beyonce": 1, "Drake": 1}
print("Genre count:", Song.genre_count)       # {"Rap": 2, "Pop": 1}

# ----- Local Tests -----
def run_tests():
    # Create songs
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("God's Plan", "Drake", "Rap")
    song4 = Song("Crazy in Love", "Beyonce", "Pop")

    # Test instance attributes
    assert song1.name == "99 Problems"
    assert song2.artist == "Beyonce"
    assert song3.genre == "Rap"

    # Test class count
    assert Song.count == 4

    # Test unique artists
    assert set(Song.artists) == {"Jay-Z", "Beyonce", "Drake"}

    # Test unique genres
    assert set(Song.genres) == {"Rap", "Pop"}

    # Test artist count histogram
    assert Song.artist_count == {"Jay-Z": 1, "Beyonce": 2, "Drake": 1}

    # Test genre count histogram
    assert Song.genre_count == {"Rap": 2, "Pop": 2}

    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    run_tests()
