#!/usr/bin/env python3
"""Installation configuration"""
from setuptools import setup, find_packages
from pathlib import Path

root_dir = Path(__file__).parent
long_description = (root_dir / 'README.md').read_text()

setup(
    name='agriautonomous',
    version='2.0.0',
    description='Autonomous Rice Farm Control System',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Spark',
    author_email='spark@agriautonomous.com',
    url='https://github.com/eddy87-del/Agriautonomus',
    license='MIT',
    
    packages=find_packages(where='src') + [''],
    package_dir={'': 'src'},
    
    include_package_data=True,
    package_data={
        '': ['*.json', '*.png', '*.jpg', '*.ico'],
    },
    
    install_requires=[
        'PyQt5==5.15.7',
        'PyQtWebEngine==5.15.7',
        'PySerial==3.5',
        'paho-mqtt==1.6.1',
        'loguru==0.7.0',
        'click==8.1.7',
        'numpy==1.24.3',
        'opencv-python==4.8.0.76',
        'pillow==10.0.0',
    ],
    
    entry_points={
        'console_scripts': [
            'agriautonomous=agriautonomous:main',
            'agri=cli.agri_cli:cli',
        ],
        'gui_scripts': [
            'Agriautonomous=agriautonomous:main',
        ],
    },
    
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System :: Hardware',
    ],
    
    options={
        'bdist_wheel': {
            'universal': False,
        },
    },
)
