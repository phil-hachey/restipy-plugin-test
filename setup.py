from setuptools import setup

setup(
    name='restipy-plugin-test',
    py_modules=['region_extractor'],
    entry_points={
        'restipy.interceptors': [
            'region_exractor = region_extractor:RegionExtractor'
        ]
    },
    install_requires=[
        'restipy'
    ],
)
