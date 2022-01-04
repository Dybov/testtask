from .dev import DevConfig

try:
    from .prod import ProdConfig
except ImportError:
    AppConfig = DevConfig
else:
    AppConfig = ProdConfig
