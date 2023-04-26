class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Devop$2021+'
    MYSQL_DB = 'parquesbolivaruno'


config = {
    'development': DevelopmentConfig
}
