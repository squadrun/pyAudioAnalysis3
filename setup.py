import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyAudioAnalysis3',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.13.1',
        'matplotlib>=2.0.2',
        'scipy>=0.19.1',
        'sklearn>=0.0',
        'hmmlearn>=0.2.0',
        'simplejson>=3.13.2',
        'eyeD3>=0.8.4',
        'pydub>=0.20.0',
    ],
    include_package_data=True,
    # license='MIT License',  # example license
    description='Python tool which gives various audio processing functionalities like silence removal',
    long_description=README,
    url='https://github.com/squadrun/pyAudioAnalysis3/tree/ab_add_setup_file',
    # author='Ketan Bhatt',
    # author_email='ketanbhatt1006@gmail.com',
    # classifiers=[
    #     'Environment :: Web Environment',
    #     'Framework :: Django',
    #     'Framework :: Django :: 1.9',  # replace "X.Y" as appropriate
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: MIT License',  # example license
    #     'Operating System :: OS Independent',
    #     'Programming Language :: Python',
    #     # Replace these appropriately if you are stuck on Python 2.
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Topic :: Internet :: WWW/HTTP',
    #     'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    # ],
)