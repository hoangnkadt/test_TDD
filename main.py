from src.importDataPostgres import importData
from input.permutatedStatus.main import get_query
from src.exportData import exportData
from configs.config import get_config
def run():
  config = get_config()
  query, nameLink, nameTable, nameTableDatabase = get_query()
  exportData(config,query,nameTable,nameLink)
  importData(nameLink,nameTable,nameTableDatabase)
if __name__ == '__main__':
  run()