import os

BUILD_NUMBER = os.environ.get('BUILD_NUMBER')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
DATABASE_URL = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1) if os.environ.get('DATABASE_URL') else None
REBASE_URL = os.environ.get('REBASE_URL')
