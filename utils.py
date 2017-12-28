from os import path
from json import load,dump

def load_config():
	cfg_path = "flaskify_config.json"
	if path.isfile(cfg_path):
		with open(cfg_path, "r") as file:
			return load(file)
	else:
		data = {
			"FLASK_APP" : "run.py",
			"VENV_PATH" : "venv",
			"ROUTES"    : "app/routes.py"
		}
		with open(cfg_path, "w+") as file:
			dump(data, file)
		return data