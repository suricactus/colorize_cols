import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorize-cols",
    version="0.0.2",
    author="Ivan Ivanov",
    author_email="ivan.ivanov@suricactus.com",
    description="Convert a TSV to colored and well formated output for each column.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suricactus/colorize-cols",
    project_urls={
        "Bug Tracker": "https://github.com/suricactus/colorize-cols/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["colorize-cols = colorize_cols.colorize_cols:main"]
    },
)
