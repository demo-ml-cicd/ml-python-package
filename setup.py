from setuptools import find_packages, setup


setup(
    name="ml_example",
    packages=find_packages(),
    version="0.1.0",
    description="Training stuff",
    author="Mikhail Maryufich",
    install_requires=[
        "scikit-learn==0.24.1",
        "pandas==1.1.5",
    ],
    license="MIT",
)