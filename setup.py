from pathlib import Path

from setuptools import setup

setup(
    name="wakachigaki",
    version="1.3.2",
    packages=["wakachigaki"],
    author="Yuhsak Inoue",
    author_email="yuhsak.inoue@gmail.com",
    maintainer="Yuhsak Inoue",
    maintainer_email="yuhsak.inoue@gmail.com",
    license="MIT",
    url="https://github.com/yuhsak/wakachigaki-py",
    download_url="https://github.com/yuhsak/wakachigaki-py",
    description="Randomized fast readline for large text files.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)
