from setuptools import setup
from setuptools.command.install import install
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="lvtab",
    version="0.0.1",
    license="GPL LGPL",
    description="Tukey inspired, one-liner, pipe-able, tidy data compatible, letter-value tables.",
    author="alexhallam",
    author_email="alexhallam6.28@gmail.com",
    url="https://github.com/alexhallam/lvtab",
    download_url="https://github.com/alexhallam/lvtab/releases/tag/0.0.1",
    keywords=["terminal", "summary-statistics", "letter-value", "tukey", "summary", "statistics", "median", "hinge"],
    py_modules=["lvtab"],
    install_requires=["Click", "pandas", "numpy",'scipy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points="""
      [console_scripts]
      lvtab=lvtab:main
      """,
)
