import json
from pathlib import Path
from abc import ABC, abstractmethod

class IConfigService(ABC):
    @abstractmethod
    def update_config(self, new_config: dict):
        pass

class ConfigService:
    CONFIG_PATH = Path("app/common/userConfig.json")

    def update_config(self, new_config: dict):

        if not self.CONFIG_PATH.exists():
            raise FileNotFoundError(f"Configuration file not found at {self.CONFIG_PATH}")

        with self.CONFIG_PATH.open("r") as file:
            current_config = json.load(file)

        def deep_merge(original, updates):

            for key, value in updates.items():
                if value is None:
                    continue
                if isinstance(value, dict) and key in original and isinstance(original[key], dict):
                    deep_merge(original[key], value)
                else:
                    original[key] = value

        deep_merge(current_config, new_config)

        with self.CONFIG_PATH.open("w") as file:
            json.dump(current_config, file, indent=4)
