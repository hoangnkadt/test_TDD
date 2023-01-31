import sys
sys.path.append("./src")
sys.path.append("./configs")
from importDataPostgres import importData
from exportData import exportData

def get_query():
  nameLink = 'lead'
  nameTable = 'TDD-FACT-lead.csv'
  nameTableDatabase = 'lead'
  query = """ 
          select *
          from public.lead
          """
  return query, nameLink, nameTable, nameTableDatabase