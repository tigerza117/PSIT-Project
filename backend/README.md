# backend

## Project setup

Install dependencies
'''
pip install -r requirements.txt
'''

Setup database
'''
from app_main import db
db.create_all()
'''


### Compiles and hot-reloads for development

'''
py app_main.py | python3 app.py
'''

### Lints and fixes files
'''
autopep8 --in-place --recursive .
'''
