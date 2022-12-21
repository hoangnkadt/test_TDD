from peewee import *

# Connect to a Postgres database.
pg_db = PostgresqlDatabase('TDD-test', user='postgres', password='123',host='localhost', port=5432)

class PermutatedLeadStatusHistory (Model):
  id = CharField(primary_key=True, index=True)
  lead_id = CharField()
  startTime = DateTimeField(index=True)
  endTime = DateTimeField(index=True)
  statusBefore = CharField(null=True)
  statusAfter = CharField()
  user_id = CharField()
  class Meta:
    database = pg_db
    db_table = 'PermutatedLeadStatusHistory'

pg_db.connect()
pg_db.create_tables([PermutatedLeadStatusHistory])