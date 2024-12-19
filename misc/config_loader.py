import json

def load_config(file_path='data/ini.json'):
    with open(file_path, 'r') as file:
        return json.load(file)
    

def save_config(config, filename="data/ini.json"):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)


def add_value_to_config(key, value, filename="data/ini.json"):
    config = load_config(filename)
    
    if key in config:
        if isinstance(config[key], list):
            config[key].append(value)
        else:
            config[key] = value
    else:
        config[key] = value
    
    save_config(config, filename)


def remove_value_from_config(key, value, filename="data/ini.json"):
    config = load_config(filename)
    
    if key in config:
        if isinstance(config[key], list):
            if value in config[key]:
                config[key].remove(value)
        else:
            del config[key]
    
    save_config(config, filename)


config = load_config()
