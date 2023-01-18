import os
import psycopg2

def exportData(query,nameTable):
  conn = psycopg2.connect(host='localhost', database='crm-bi-database',user='postgres', password='123')
  cur = conn.cursor()
  outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
  file_path = os.path.join(os.getcwd(), 'input', nameTable)
  with open(file_path, "w") as f:
      cur.copy_expert(outputquery, f)