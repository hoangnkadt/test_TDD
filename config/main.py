from importlib import import_module


class Config:
  module = None
  env = None
  tenant = None

  @classmethod
  def init(cls, env, tenant, config_file='config', table=None):
    # Switch env here
    cls.module = import_module(f'configs.etl.{tenant}.{env}.{config_file}')
    cls.env = env
    cls.tenant = tenant
    cls.table = table
