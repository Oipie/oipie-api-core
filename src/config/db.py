"""
    Database configuration
"""
import os


DATABASE_CONFIG = {
    "host": os.environ.get('HOST', 'localhost'),
    "port": int(os.environ.get('PORT', '5432'),),
    "username":  os.environ.get('DATABASE_USER', 'oipie'),
    "password":  os.environ.get('DATABASE_PASSWORD', 'password'),
    "database_name": os.environ.get('DATABASE_NAME', 'oipie'),
}
