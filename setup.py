import io
import json
import os
from setuptools import setup


with open(os.path.join("dash_player", "package.json")) as f:
    package = json.load(f)

package_name = package["name"].replace("@plotly/", "").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    packages=[package_name],
    include_package_data=True,
    license=package["license"],
    long_description=io.open("README.md", encoding="utf-8").read(),
    install_requires=[],
)
