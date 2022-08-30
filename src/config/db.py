"""
    Database configuration
"""
import os


DATABASE_CONFIG = {
    "host": os.environ.get('DATABASE_HOST', 'localhost'),
    "port": int(os.environ.get('DATABASE_PORT', '5432'),),
    "username":  os.environ.get('DATABASE_USER', 'oipie'),
    "password":  os.environ.get('DATABASE_PASSWORD', 'password'),
    "database_name": os.environ.get('DATABASE_NAME', 'oipie'),
}
print('DATABASE_URL'.replace('postgres', 'postgresql'))
DATABASE_URL_CONECTION = os.environ.get(
    'DATABASE_URL'.replace('postgres', 'postgresql'),
    "postgresql://{host}:{port}/{database_name}?user={username}&password={password}"
    .format(**DATABASE_CONFIG))
