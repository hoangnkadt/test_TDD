import sys,psycopg2

conn = psycopg2.connect(host='localhost', database='TDD-test',user='postgres', password='123')
cur = conn.cursor()

query = """ 
          select * from "PermutatedLeadStatusHistory"
        
        """

outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

with open("testExportData.csv", "w") as f:
    cur.copy_expert(outputquery, f)