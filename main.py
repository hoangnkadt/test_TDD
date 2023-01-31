from src.importDataPostgres import importData
from input.permutatedStatus.main import get_query
from src.exportData import exportData
from configs.config import get_config_export,get_config_import
def run():
  config_export = get_config_export()
  config_import = get_config_import()
  query, nameLink, nameTable, nameTableDatabase = get_query()
  exportData(config_export,query,nameTable,nameLink)
  importData(config_import,nameLink,nameTable,nameTableDatabase)
if __name__ == '__main__':
  run()