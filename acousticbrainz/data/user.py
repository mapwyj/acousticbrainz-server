import psycopg2
from flask import current_app
from flask_login import UserMixin
from werkzeug.exceptions import BadRequest, ServiceUnavailable


def create(musicbrainz_id):
    try:
        connection = psycopg2.connect(current_app.config['PG_CONNECT'])
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "user" (musicbrainz_id) VALUES (%s)',
                       (str(musicbrainz_id),))
        connection.commit()

        # Getting new user's ID
        cursor.execute('SELECT id FROM "user" WHERE musicbrainz_id = %s',
                       (str(musicbrainz_id),))
    except psycopg2.ProgrammingError, e:
        raise BadRequest(str(e))
    except psycopg2.IntegrityError, e:
        raise BadRequest(str(e))
    except psycopg2.OperationalError, e:
        raise ServiceUnavailable(str(e))

    return cursor.fetchone()[0]


def get(id):
    try:
        connection = psycopg2.connect(current_app.config['PG_CONNECT'])
        cursor = connection.cursor()
        cursor.execute('SELECT id, created, musicbrainz_id FROM "user" WHERE id = %s',
                       (str(id),))
    except psycopg2.IntegrityError, e:
        raise BadRequest(str(e))
    except psycopg2.OperationalError, e:
        raise ServiceUnavailable(str(e))

    if cursor.rowcount > 0:
        row = cursor.fetchone()
        return User(
            id=row[0],
            created=row[1],
            musicbrainz_id=row[2],
        )
    else:
        return None


def get_by_mb_id(musicbrainz_id):
    try:
        connection = psycopg2.connect(current_app.config['PG_CONNECT'])
        cursor = connection.cursor()
        cursor.execute('SELECT id, created FROM "user" WHERE musicbrainz_id = %s',
                       (str(musicbrainz_id),))
    except psycopg2.IntegrityError, e:
        raise BadRequest(str(e))
    except psycopg2.OperationalError, e:
        raise ServiceUnavailable(str(e))

    if cursor.rowcount > 0:
        row = cursor.fetchone()
        return User(
            id=row[0],
            created=row[1],
            musicbrainz_id=musicbrainz_id,
        )
    else:
        return None


def get_or_create(musicbrainz_id):
    user = get_by_mb_id(musicbrainz_id)
    if not user:
        create(musicbrainz_id)
        user = get_by_mb_id(musicbrainz_id)
    return user


class User(UserMixin):
    def __init__(self, id, created, musicbrainz_id):
        self.id = id
        self.created = created
        self.musicbrainz_id = musicbrainz_id
