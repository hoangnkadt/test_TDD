from input.permutatedStatus.main import get_permutatedStatus_export_data
from input.lead.main import get_lead_export_data
from src.exportData import exportData
from configs.config import get_config_export
import os

def run_table(one_table, config_export):
    query_functions = {
        "permutatedStatus": get_permutatedStatus_export_data,
        "lead": get_lead_export_data,
    }
  
    query_function = query_functions.get(one_table)
    query, nameLink, nameTable = query_function()
    exportData(config_export, query, nameTable, nameLink)

def run_tables(tables):
    config_export = get_config_export()
    for table in tables:
        run_table(table, config_export)

if __name__ == '__main__':
    table = os.getenv('TABLE')
    list_table = table.split(',')
    if list_table[0].lower() == 'all':
        run_tables(["permutatedStatus", "lead"])
    else:
        run_tables(list_table)