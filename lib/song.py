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

        # Update class-level data
        Song.count += 1

        if artist not in Song.artists:
            Song.artists.append(artist)
        if genre not in Song.genres:
            Song.genres.append(genre)

        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
