import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "userConfig.json"

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = json.load(file)
    params = config.get("params", {})
    xng_params = config.get("xng_params", {})
    return params, xng_params

def update_config(new_params=None, new_xng_params=None):
    global params, xng_params

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = json.load(file)

    if new_params:
        config["params"].update(new_params)
    if new_xng_params:
        config["xng_params"].update(new_xng_params)

    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

    params, xng_params = load_config()

params, xng_params = load_config()