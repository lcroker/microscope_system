from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="microscope_system",
    version="0.1.0",
    author="Luke Croker",
    author_email="lcroker87@gmail.com",
    description="A control system for microscopes with autofocus and GUI capabilities",
    long_description=long_description (TBA),
    long_description_content_type="text/markdown",
    url="https://github.com/lcroker/microscope_system",
    packages=find_packages(where="microscope_system"),
    package_dir={"": "microscope_system"},
    include_package_data=True,
    install_requires=[
        "PyQt5==5.15.4",
        "numpy==1.20.3",
        "pandas==1.2.4",
        "tifffile==2021.4.8"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'microscope_gui=microscope_system.gui.main_window:main',
        ],
    },
)
