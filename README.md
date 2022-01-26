# Flask User Authentication

## Features :
- Register (with unique username & hashed password)
- Login
- Welcome (allowed to access when logged in)
- Logout

## Install the requirements
```batch
pip install -r requirements.txt
```

## Additional Files
- genTable.py --> Used for generating tables

## Generate the tables

- First start the python shell
```batch
python
```

- Then import db from genTable
```batch
from genTable import db
```

- Then create the table
```batch
db.create_all()
```

- Then exit the shell
```batch
exit()
```

## Database Used
- Postgresql

## Useful sources
- [Flask 2.0x Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Postgres Commands (postgresqltutorial.com)](https://www.postgresqltutorial.com/psql-commands/)
- [Postgres Commands (geeksforgeeks.org)](https://www.geeksforgeeks.org/postgresql-psql-commands/)
- [Flask 2.x Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Live preview of this project at:
- [https://flask-user-registration.herokuapp.com/](https://flask-user-registration.herokuapp.com/)

## Markdown Cheatsheet:
- [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Thanks for viewing this project