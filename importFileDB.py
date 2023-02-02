from modules.sql_model import *
from src.importDataPostgres import importData
from input.permutatedStatus.main import get_permutatedStatus_import_data
from input.lead.main import get_lead_import_data
from configs.config import get_config_import
import os

def run_table(one_table, config_import):
    query_functions = {
        "permutatedStatus": get_permutatedStatus_import_data,
        "lead": get_lead_import_data,
    }
    query_function = query_functions.get(one_table)
    nameLink, nameTable, nameTableDatabase = query_function()
    importData(config_import, nameLink, nameTable, nameTableDatabase)

def run_tables(tables):
    config_import = get_config_import()

    for table in tables:
        run_table(table, config_import)

if __name__ == '__main__':
    table = os.getenv('TABLE')
    list_table = table.split(',')
    if list_table[0].lower() == 'all':
        run_tables(["permutatedStatus", "lead"])
    else:
        run_tables(list_table)