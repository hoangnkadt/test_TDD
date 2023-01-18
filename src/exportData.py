import psycopg2

def exportData(query,nameTable):
  conn = psycopg2.connect(host='localhost', database='TDD-test',user='postgres', password='123')
  cur = conn.cursor()

  query = """ 
            select * from "PermutatedLeadStatusHistory" ORDER BY "id" limit 10
          
          """

  outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

  with open(nameTable, "w") as f:
      cur.copy_expert(outputquery, f)