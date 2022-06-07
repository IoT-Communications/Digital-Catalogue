from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in digital_catalogue/__init__.py
from digital_catalogue import __version__ as version

setup(
	name="digital_catalogue",
	version=version,
	description="Digital Catalogue System",
	author="IoT Communications (Pty) Ltd",
	author_email="info@iotcomms.co.bw",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
