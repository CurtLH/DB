from setuptools import setup

requirements = [
    # package requirements go here
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
        'console_scripts': [
            'db=db.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='DB',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
