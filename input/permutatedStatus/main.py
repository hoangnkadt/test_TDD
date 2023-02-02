def get_permutatedStatus_import_data():
  nameLink = 'permutatedStatus'
  nameTable = 'TDD-FACT-permutatedStatus.csv'
  nameTableDatabase = 'PermutatedLeadStatusHistory'
  return nameLink, nameTable, nameTableDatabase

def get_permutatedStatus_export_data():
  nameLink = 'permutatedStatus'
  nameTable = 'TDD-FACT-permutatedStatus.csv'
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
  return query, nameLink, nameTable