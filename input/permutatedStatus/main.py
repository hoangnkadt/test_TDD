import sys
sys.path.append("./src")
from importDataPostgres import importData
from exportData import exportData
def run():
  nameLink = 'permutatedStatus'
  nameTable = 'TDD-FACT-permutatedStatus.csv'
  nameTableDatabase = 'PermutatedLeadStatusHistory'
  query = """ 
          SELECT "PermutatedLeadStatusHistory".*
          FROM public."PermutatedLeadStatusHistory"
          JOIN (
            SELECT lead_id, count(*) as count_status FROM public."PermutatedLeadStatusHistory"
            where "statusAfter" IN ('L5A','L5B','L5C') and "user_history_id" is not NULL
            GROUP BY lead_id
            ORDER BY count_status
            LIMIT 15) as tb1
          ON "PermutatedLeadStatusHistory".lead_id = tb1.lead_id
          """
  exportData(query,nameTable,nameLink)
  importData(nameLink,nameTable,nameTableDatabase)
if __name__ == '__main__':
  run()