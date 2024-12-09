import os
import re
from setuptools import find_packages, setup

def read_requirements():
    """Read requirements from requirements.txt file"""
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")
    return [req for req in requirements if req and not req.startswith("#")]

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    # Process any images in the README
    images = re.findall(r"!\[.*\]\((.*)\)", long_description)
    for image in images:
        if "http" in image:
            continue
        long_description = long_description.replace(
            image, "https://raw.githubusercontent.com/yourusername/techbase/main/" + image
        )

# Get version from GitHub ref or use default
version = os.getenv("GITHUB_REF_NAME", "v0.1.0")

setup(
    name="techbase",
    author="Angela Jacinto",
    author_email="angelajcnto@gmail.com",
    description="A technical knowledge base system for industrial equipment documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Documentation",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    url="https://github.com/angelajacinto/techbase",
    project_urls={
        "Source": "https://github.com/angelajacinto/techbase",
        "Bug Tracker": "https://github.com/angelajacinto/techbase/issues",
    },
    entry_points={
        'console_scripts': [
            'techbase=techbase.main:main',
        ],
    },
)