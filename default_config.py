DEBUG = False  # set to False in production mode
# Additional files to watch to restart the development server
RELOAD_ON_FILES = ["webserver/static/build/rev-manifest.json"]

SECRET_KEY = "CHANGE_ME"


# DATABASES

# Primary database
SQLALCHEMY_DATABASE_URI = "postgresql://acousticbrainz@/acousticbrainz"

# This connection string will be used for testing
SQLALCHEMY_TEST_URI = "postgresql://ab_test@/ab_test"

# The name of a postgres user who has superuser privileges. Your local user should
# be able to connect to the database with this user.
PG_SUPER_USER = "postgres"
# The port that postgres is running on
PG_PORT = "5432"

# MUSICBRAINZ

MUSICBRAINZ_USERAGENT = "acousticbrainz-server"
MUSICBRAINZ_HOSTNAME = None

# OAuth
MUSICBRAINZ_CLIENT_ID = "CHANGE_ME"
MUSICBRAINZ_CLIENT_SECRET = "CHANGE_ME"

# CACHE

MEMCACHED_SERVERS = ["127.0.0.1:11211"]
MEMCACHED_NAMESPACE = "AB"

# LOGGING

LOG_FILE_ENABLED = False
LOG_FILE = "./acousticbrainz.log"

LOG_EMAIL_ENABLED = False
LOG_EMAIL_TOPIC = "AcousticBrainz Webserver Failure"
LOG_EMAIL_RECIPIENTS = []  # List of email addresses (strings)

LOG_SENTRY_ENABLED = False
SENTRY_DSN = ""


# MISCELLANEOUS

# Mail server
# These variables need to be defined if you enabled log emails.
SMTP_SERVER = "localhost"
SMTP_PORT = 25
MAIL_FROM_DOMAIN = "acousticbrainz.org"

FILE_STORAGE_DIR = "./files"

#Feature Flags
FEATURE_EVAL_LOCATION = False
