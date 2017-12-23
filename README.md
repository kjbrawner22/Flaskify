# Flaskify
Command Line Interface for common Flask operations

1. Installation
	- `git clone https://github.com/kjbrawner22/Flaskify.git`
	- `cd Flaskify`
	- `pip3 install -e .` (e flag signals development mode).
		- Note: after every change to the source code, you must run this command again.
		- Note: I have not tried this with python2. Please let me know if it works or if it needs some changes.
	#### ---OR---
	- [Go to releases page](https://github.com/kjbrawner22/Flaskify/releases/tag/0.1.dev1)
	- Download latest .whl file
	- Locate file in cmd or terminal
	- Run `pip3 install ` with wheel name appended.
2. Usage
	- `flaskify generate project`
		- This generates a project structure for an easily-scalable Flask app.
		- prompts you for the project name.
	- `flaskify generate route`
		- This adds a route to the routes.py file, and generates corresponding html/css files.
		- prompts you for route name and html/css name (w/o extensions).
	- `flaskify run`
		- combines the `export FLASK_APP=run.py` and `flask run` into 1 step.
3. Contribution
	- Always Welcome! If you can make this tool better, fix my code, add documentation, or have ideas for new features, please submit a pull request.
4. Plans for the Future
	- Set up a config system to allow for custom naming and tracking of project-generated files.
	- Add more generation options such as Forms, Mail setup, etc.

### Thanks for using/contributing to Flaskify :)
