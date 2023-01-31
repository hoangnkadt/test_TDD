def get_config_export():
  db_config = {
    'uri': 'mongodb://localhost:27017',
    'crm_db': 'techkids-edu-crm',
    'crm_db_credentials': None,
    'mySQL': {
      'db_name': 'crm-bi-database',
      'user': 'postgres',
      'password': '123',
      'host': 'localhost',
      'port': 5432
    }
  }
  return db_config

def get_config_import():
  db_config = {
    'uri': 'mongodb://localhost:27017',
    'crm_db': 'techkids-edu-crm',
    'crm_db_credentials': None,
    'mySQL': {
      'db_name': 'TDD-test',
      'user': 'postgres',
      'password': '123',
      'host': 'localhost',
      'port': 5432
    }
  }
  return db_config