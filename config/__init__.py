from .dev import DevConfig
from .testconf import TestConfig

try:
    from .prod import ProdConfig
except ImportError:
    AppConfig = DevConfig
else:
    AppConfig = ProdConfig


__all__ = [
    'AppConfig',
    'TestConfig',
]
