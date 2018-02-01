from setuptools import setup

setup(
	name='flaskify',
	version='0.2',
	description='Simple Flask project generation',
	author="Kenny Brawner",
	author_email="kjbrawner@crimson.ua.edu",
	py_modules=['flaskify'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		flaskify=flaskify:cli
	''',
)