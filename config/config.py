import os
import streamlit as st

# DEPRECATED: THIS WAS NECESSARY USING SQLITE3
current_dir = os.getcwd()
DB_FILE = f'{current_dir}/movies_db2.db'

DB_NAME = "defaultdb"

# Safely load database credentials from Streamlit Secrets
try:
    USERNAME = st.secrets["DB_USERNAME"]
    PASSWORD = st.secrets["DB_PASSWORD"]
    HOST = st.secrets["DB_HOST"]
    PORT = st.secrets.get("DB_PORT", 3306)
except (FileNotFoundError, KeyError, Exception):
    # Fallback placeholders for local testing if secrets aren't set
    USERNAME = "root"
    PASSWORD = "password"
    HOST = "localhost"
    PORT = 3306

MOVIES_PER_ROW = 5
DATA_PATH = f"{current_dir}/data/"
MOVIE_DB_URL = "https://www.themoviedb.org/"
NO_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Image-missing.svg/480px-Image-missing.svg.png"


rec_methods = ['Generalized recommendations', 'Content-based recommendations', 'Collaborative recomendations']
rec_description = dict()
rec_description['Generalized recommendations'] = "These recommendations are based on movie popularity"
rec_description['Content-based recommendations'] = "Recommend similar movies based on a particular movie."
rec_description['Collaborative recomendations'] = "Recommends movies based on past ratings and preferences of other 'similar' users. (DEVELOPING)"

