def get_lead_export_data():
  nameLink = 'lead'
  nameTable = 'TDD-FACT-lead.csv'
  query = """ 
          SELECT *
          FROM public.lead
          where id IN (select lead_id			 
          FROM (SELECT lead_id, count(*) as count_status FROM public."PermutatedLeadStatusHistory"
          where "statusAfter" IN ('L5A','L5B','L5C') and "user_history_id" is not NULL
          GROUP BY lead_id
          ORDER BY count_status
          LIMIT 15) tb1)
          """
  return query, nameLink, nameTable

def get_lead_import_data():
  nameLink = 'lead'
  nameTable = 'TDD-FACT-lead.csv'
  nameTableDatabase = 'lead'
  return nameLink, nameTable, nameTableDatabase