import os

class Config:
    pass

class ProdConfig(Config):
    pass
   

class DevConfig(Config):
    SECRET_KEY = 'This_is_my_secret'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
