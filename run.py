from app import create_app
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig

config_map = {
    "development" : DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

import os
config_class = os.environ.get("CONFIG_CLASS", "development")

app = create_app(config_map[config_class])

if __name__ == "__main__":
    app.run()
