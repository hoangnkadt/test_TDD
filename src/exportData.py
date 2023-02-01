import os
import psycopg2

def exportData(config,query,nameTable,nameLink):
  conn = psycopg2.connect(host=config['mySQL']['host'], database=config['mySQL']['db_name'],user=config['mySQL']['user'], password=config['mySQL']['password'])
  cur = conn.cursor()
  outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER ".format(query)
  file_path = os.path.join(os.getcwd(), 'input', nameLink , nameTable)
  with open(file_path, "w",  encoding="utf-8") as f:
      cur.copy_expert(outputquery, f)