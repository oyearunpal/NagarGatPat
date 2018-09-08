# NagarGatPat

[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

NagarGatPat is a free open source web based project where you can add details of swaymsevaks of your Nagar. It is design for Nagar's daily usage.

## Feautres

1. You can add all details of swaymsevaks like, basti,shakha,emailID,Sangh Shiksha varg.
2. Data can be filter based on Swaymsevak type(Bal,Tarun,Vyvasayi),basti,shakha etc.
3. Also you can see graph of swaymsevak belongs to different shakha, basti etc.
4. Lots of filter and sorting available there.
5. It also shows birthday coming in 15days.

## Documentation


-
## Installation

1) Install python 2.7 [https://www.python.org/downloads/release/python-2713/]
2) Install postgresql
3) Install pip [https://pip.pypa.io/en/stable/installing/]
3) ```pip install -r requirements.txt```

Download project 

# Commands to setup the project
1)Set up database configuration in Online_Retail>settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'name_of_db',
        'USER': 'user_of_db',
        'PASSWORD': 'pass_of_db',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```

2)Commands to set up project and run the development server
```
  python manage.py makemigrations
  python manage.py migrate
  //Create superuser
  python manage.py createsuperuser
  //run server
  python manage.py runserver
```

## TODO

1. Move from python 2.7 to python 3.0. And django 1.9 to 2.0.
2. Import / Export in csv/xlsx format.


## Immediate TODO
1. Pick nagar/basti names from file .
2. Remove Jholivachnalaya.

## Contribute

Any developers who wants to contribute please feel free to do your contribution.

## Code of Conduct

 - 

## Connect with Developer

Arun Pal


## License



