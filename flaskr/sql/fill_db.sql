INSERT INTO genres (title)
VALUES
    ('rock'),
    ('classic'),
    ('pop');

INSERT INTO tracks (title, artist, length, genre_id)
VALUES
    ('rock_song_1', 'rock_artist_1', 100, 1),
    ('rock_song_2', 'rock_artist_2', 90, 1),
    ('rock_song_3', 'rock_artist_3', 130, 1),
    ('rock_song_4', 'rock_artist_4', 180, 1),
    ('rock_song_5', 'rock_artist_4', 115, 1),
    ('classic_song_1', 'classic_artist_1', 200, 2),
    ('classic_song_2', 'classic_artist_1', 240, 2),
    ('classic_song_3', 'classic_artist_1', 90, 2),
    ('classic_song_4', 'classic_artist_2', 100, 2),
    ('classic_song_5', 'classic_artist_2', 165, 2),
    ('classic_song_6', 'classic_artist_3', 180, 2),
    ('pop_song_1', 'pop_artist_1', 180, 3),
    ('pop_song_2', 'pop_artist_1', 120, 3),
    ('pop_song_3', 'pop_artist_1', 150, 3),
    ('pop_song_4', 'pop_artist_1', 100, 3),
    ('pop_song_5', 'pop_artist_2', 180, 3),
    ('pop_song_6', 'pop_artist_2', 120, 3),
    ('pop_song_7', 'pop_artist_2', 90, 3),
    ('pop_song_8', 'pop_artist_2', 155, 3),
    ('pop_song_9', 'pop_artist_3', 110, 3),
    ('pop_song_10', 'pop_artist_3', 85, 3);
