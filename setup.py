from setuptools import setup

setup(
    name="hello-world",
    version="0.0.1",
    description="Greet the world.",
    py_modules=["hello"],
    entry_points={
        "console_scripts": ["hello=hello:main"],
    },
)
