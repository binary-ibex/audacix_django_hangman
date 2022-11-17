# audacix_django_hangman


### system specification use for the development:

- os: ubuntu 20.04 LST
- python: 3.8.10
- ram: 20 GB
- processor: intel i5 7th gen


### How to run the project 

- Install packages 

```
pip3 install -r requirements.txt 

```
- Run inital migrations 

```
python3 manage.py migrate
```

- Load data 

```
python3 manage.py loaddata fixtures.yaml

```

- Run development server
```
python3 manage.py runserver 8000

```

#### Optionsl

Run test 

```
python3 manage.py test

```