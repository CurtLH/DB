#!/usr/bin/env python

import psycopg2
import logging


# enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def connect_to_db(database='postgres', user='postgres', 
                  password='apassword', host='localhost'):

    """
    Connect to Postgres DB and return cursor
 
    Parameters
    ----------
    database : string (default='postgres')

    user : string (default='postgres')

    password : string (default='apassword')

    host : string (default='localhost')
    
    Returns
    -------
    cur : psycopg2 curson
    """

    # connect to the database
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                password="apassword",
                                host="localhost")
        conn.autocommit = True
        cur = conn.cursor()
        logger.info("Successfully connected to the database")

    except:
        logger.warning("Cannot connect to database")
        exit
