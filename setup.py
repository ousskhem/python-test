from setuptools import setup

setup(
    name='api_pricing',
    packages=['api_pricing'],
    include_package_data=True,
    install_requires=[
        'flask',
        'requests'
    ],
)
