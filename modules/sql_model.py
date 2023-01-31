from peewee import *

# Connect to a Postgres database.
pg_db = PostgresqlDatabase('TDD-test', user='postgres', password='123',host='localhost', port=5432)

class PermutatedLeadStatusHistory(Model):
  id = CharField(primary_key=True, index=True)
  lead_id = CharField()
  leadCreatedAt = TimestampField()
  startTime = DateTimeField(index=True)
  endTime = DateTimeField(index=True)
  statusBefore = CharField(null=True) #Need to fix missing statusBefore in app db
  statusAfter = CharField()
  user_id = CharField()
  owner_id = CharField()
  endTime_id = IntegerField()
  user_history_id = IntegerField()
  class Meta:
    database = pg_db
    table_name = 'PermutatedLeadStatusHistory'


class lead(Model):
  id = CharField(primary_key=True, index=True)
  createdAt = TimestampField(null=True)
  lastModifiedAt = TimestampField(null=True)
  contact_id = CharField()
  user_id = CharField()
  statusName = CharField(null=True)
  content_id = CharField()
  isDeleted = BooleanField(null=True)
  channel = CharField(null=True)
  source = CharField(null=True)
  medium = CharField(null=True)
  campaign = CharField(null=True)
  businessDomain_id = CharField()
  businessUnit_id = CharField()
  class Meta:
    database = pg_db
    table_name = 'lead'


def get_mySQL_db():
  return pg_db

pg_db.connect()
pg_db.create_tables([lead])
pg_db.create_tables([PermutatedLeadStatusHistory])