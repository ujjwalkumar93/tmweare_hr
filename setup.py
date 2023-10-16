from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tmweare_hr/__init__.py
from tmweare_hr import __version__ as version

setup(
	name="tmweare_hr",
	version=version,
	description="Hr Related custom fields and Scripts",
	author="ranbir",
	author_email="ranbir@tmweare.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
