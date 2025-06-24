from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ore-no-lovecome",
    version="1.0.0",
    author="Mizushima",
    author_email="example@email.com",
    description="俺のラブコメはこんなはずじゃなかった - 美少女ゲームをメタる青春ラブコメディ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmizu/ore-no-lovecome-ha-konnna-hazu-ja-nakatta",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "mkdocs>=1.5.3",
        "mkdocs-material>=9.5.3",
        "mkdocs-material-extensions>=1.3.1",
        "pymdown-extensions>=10.7",
    ],
    entry_points={
        'console_scripts': [
            'ore-no-lovecome-build=scripts.build:main',
            'ore-no-lovecome-serve=scripts.serve:main',
        ],
    },
)
