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
    description=("A Dash component for playing a variety of URLs."),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/plotly/dash-player",
    install_requires=["dash>=1.6.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Dash",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
