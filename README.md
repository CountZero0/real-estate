# Site of a real estate agency 

The site is under construction, so only a page with a list of apartments and an admin panel for filling the database is available. 

## Run 

- Download the code 
- Install dependencies with `pip install -r requirements.txt` 
- Create a database file and apply all migrations immediately with `python3 manage.py migrate` 
- Start the server with `python3 manage.py runserver` 

## Environment Variables 

Part of the project settings is taken from the environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`. 

3 variables are available: 
- `DEBUG` — debug mode. Set to True to see debug information in case of an error.
- `SECRET_KEY` - secret key of the project
- `ALLOWED_HOSTS` - see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). 
- `DATABASE` — one-line address to the database, for example: `sqlite:///db.sqlite3`. More information in [documentation](https://github.com/jacobian/dj-database-url) 

    This makes it easy to switch between databases: PostgreSQL, MySQL, SQLite - it doesn't matter, you just need to substitute the right address. 
    
