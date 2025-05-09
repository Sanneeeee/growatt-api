efrom setuptools import setup, find_packages

setup(
    name='growatt-api-devices',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Sanneeeee',
    author_email='sanne.boels@student.hu.nl',
    description='My modified fork of the Growatt API wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sanneeeee/growatt-api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
