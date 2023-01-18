from src.importDataPostgres import importData
from src.exportData import exportData

query = """ 
    SELECT "PermutatedLeadStatusHistory".*
    FROM public."PermutatedLeadStatusHistory"
    RIGHT join (
      SELECT lead_id, count(*) as count_status FROM public."PermutatedLeadStatusHistory"
      GROUP BY lead_id
      ORDER BY count_status DESC
      LIMIT 3) as tb1
    ON "PermutatedLeadStatusHistory".lead_id = tb1.lead_id
        """
exportData(query,'TDD-FACT-permutatedStatus.csv')
importData('TDD-FACT-permutatedStatus.csv','PermutatedLeadStatusHistory')