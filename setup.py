from setuptools import setup

requirements = [
  "psycopg2"
]

setup(
    name='DB',
    version='0.1.0',
    description="Database Connector",
    author="Curtis Hampton",
    author_email='CurtLHampton@gmail.com',
    url='https://github.com/CurtLH/DB',
    packages=['db'],
    entry_points={
    },
    install_requires=requirements,
    keywords='DB',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
