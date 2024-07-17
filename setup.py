from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="0.0.1",
    description="Greet the world.",
    packages=find_packages(),
    py_modules=["hello"],
    entry_points={
        "console_scripts": ["hello=hello:main"],
    },
)
