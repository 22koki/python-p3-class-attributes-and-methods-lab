class Song:
    # Class attribute to keep track of the number of songs
    count = 0

    # Class attribute to store unique genres
    genres = set()

    # Class attribute to store unique artists
    artists = set()

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs and update genres and artists
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

        # Add to genre count after updating genres
        Song.add_to_genre_count()

    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs
        cls.count += 1

    def add_to_genres(self):
        # Add the genre of the current song to the genres set
        Song.genres.add(self.genre)

    def add_to_artists(self):
        # Add the artist of the current song to the artists set
        Song.artists.add(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        # Reset genre_count dictionary before updating
        cls.genre_count = {}

        # Combine genres set from all instances
        all_genres = [song.genre for song in cls.__dict__.values() if isinstance(song, Song)]

        # Populate the genre_count dictionary
        for genre in all_genres:
            # Count the occurrences of each genre in the genres set
            count = all_genres.count(genre)

            # Assign the count to the genre in the dictionary
            cls.genre_count[genre] = count

    @classmethod
    def add_to_artist_count(cls):
        # Reset artist_count dictionary before updating
        cls.artist_count = {}

        # Combine artists set from all instances
        all_artists = set([song.artist for song in cls.__dict__.values() if isinstance(song, Song)])

        # Populate the artist_count dictionary
        for artist in all_artists:
            # Count the occurrences of each artist in the artists set
            count = sum(1 for song in cls.__dict__.values() if isinstance(song, Song) and artist == song.artist)

            # Assign the count to the artist in the dictionary
            cls.artist_count[artist] = count
