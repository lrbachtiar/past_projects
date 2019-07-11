import sqlite3
import re

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    """
    conn = sqlite3.connect(db_file)
    return conn

def clean_column_names(column_name):
    new_name = re.sub(r'[^A-Za-z0-9]', '_', column_name).strip()
    cameled = re.sub(r'_{1,}', '_', camel_to_lower_case(new_name))
    final = cameled[:-1] if cameled[-1] == '_' else cameled
    return final


def camel_to_lower_case(name):
    step_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z])([0-9A-Z])', r'\1_\2', step_1).lower()