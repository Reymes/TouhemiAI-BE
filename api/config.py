class Config:
    ...


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    ...


class TestConfig(Config):
    ...
