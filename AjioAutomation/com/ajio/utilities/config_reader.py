import os
import configparser

class ConfigReader:
    _prop = None

    @staticmethod
    def get_property(key: str) -> str:
        if ConfigReader._prop is None:
            ConfigReader._prop = configparser.ConfigParser()
            config_path = os.path.join("src", "test", "resources", "config", "config.properties")
            try:
                ConfigReader._prop.read(config_path)
            except Exception as e:
                print(f"❌ Error loading config: {e}")

        return ConfigReader._prop.get("DEFAULT", key, fallback=None)