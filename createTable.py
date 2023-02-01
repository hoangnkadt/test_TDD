from modules.sql_model import *
from src.importDataPostgres import importData
from input.permutatedStatus.main import get_permutatedStatus_data
from input.lead.main import get_lead_data
from src.exportData import exportData
from configs.config import get_config_export,get_config_import

def run_table(table, config_export, config_import):
    query_functions = {
        "permutatedStatus": get_permutatedStatus_data,
        "lead": get_lead_data,
    }
  
    query_function = query_functions.get(table)
    query, nameLink, nameTable, nameTableDatabase = query_function()
    exportData(config_export, query, nameTable, nameLink)
    importData(config_import, nameLink, nameTable, nameTableDatabase)

def run_tables(tables):
    config_export = get_config_export()
    config_import = get_config_import()

    for table in tables:
        run_table(table, config_export, config_import)

if __name__ == '__main__':
    run_tables(["permutatedStatus", "lead"])