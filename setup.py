from setuptools import setup, find_packages

setup(
    name="lokotech-django-site",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "asgiref==3.8.1",
        "dj-database-url==3.1.2",
        "Django==6.0.3",
        "gunicorn==26.0.0",
        "psycopg2-binary==2.9.12",
        "python-decouple==3.8",
        "whitenoise==6.12.0",
    ],
)
