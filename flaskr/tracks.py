from flask import (
    Blueprint, render_template, request
)

from flaskr.db import get_db

bp = Blueprint('tracks', __name__, url_prefix='/tracks')


@bp.route('/')
def main_page():
    return render_template('tracks_main_page.html')


@bp.route('/names/')
def names():
    db = get_db()
    unique_artists = db.execute(
        'SELECT DISTINCT artist FROM tracks'
    ).fetchall()
    return render_template('tracks/unique_artists.html', artists=unique_artists)



@bp.route('/tracks/', defaults={'genre': None})
@bp.route('/tracks/<genre>')
def get_genre_count(genre):
    print(genre)
    if genre is None:
        db = get_db()
        tracks_count = db.execute(
            'SELECT COUNT(*) as cnt FROM tracks'
        ).fetchone()

        genres = db.execute(
            'SELECT title FROM genres'
        ).fetchall()

        return render_template('tracks/tracks_count.html',
                               tracks_count=tracks_count['cnt'],
                               genres=genres,
                               genre=None)

    genre_selected = genre

    db = get_db()
    genre_count_tracks = db.execute(
        'SELECT count(*) as cnt '
        'FROM tracks JOIN genres g on g.id = tracks.genre_id '
        'WHERE g.title = ?', (genre_selected,)
    ).fetchone()
    genres = db.execute(
        'SELECT title FROM genres WHERE title <> ?', (genre_selected,)
    ).fetchall()
    return render_template('tracks/tracks_count.html',
                           tracks_count=genre_count_tracks['cnt'],
                           genres=genres,
                           genre=genre_selected)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks = db.execute(
        'SELECT DISTINCT title, length FROM tracks'
    ).fetchall()
    return render_template('tracks/tracks_sec.html', tracks=tracks)


@bp.route('/tracks-sec/statistics')
def tracks_sec_statistics():
    db = get_db()
    tracks_stat = db.execute(
        'SELECT SUM(length) as tr_sum, AVG(length) as tr_avg FROM tracks'
    ).fetchone()

    return render_template('tracks/tracks_statistics.html', tracks_mean=round(tracks_stat['tr_avg'], 2),
                           tracks_sum=tracks_stat['tr_sum'])
