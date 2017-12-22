from setuptools import setup

setup(
	name='flaskify',
	version='0.1',
	py_modules=['flaskify'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		flaskify=flaskify:cli
	''',
)