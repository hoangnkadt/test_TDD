from peewee import *

# Connect to a Postgres database.
pg_db = PostgresqlDatabase('TDD-test', user='postgres', password='123',host='localhost', port=5432)

class PermutatedLeadStatusHistory(Model):
  id = CharField(primary_key=True, index=True)
  lead_id = ForeignKeyField()
  leadCreatedAt = TimestampField()
  startTime = DateTimeField(index=True)
  endTime = DateTimeField(index=True)
  statusBefore = CharField(null=True) #Need to fix missing statusBefore in app db
  statusAfter = CharField()
  user_id = ForeignKeyField()
  owner_id = ForeignKeyField()
  endTime_id = ForeignKeyField()
  user_history_id = ForeignKeyField()
  class Meta:
    database = pg_db
    table_name = 'PermutatedLeadStatusHistory'

pg_db.connect()
pg_db.create_tables([PermutatedLeadStatusHistory])