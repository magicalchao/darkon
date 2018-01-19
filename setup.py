from setuptools import setup, find_packages
import json


info = json.load(open('info.json'))
with open('requirements.txt') as f:
    deps = [str(dep.strip()) for dep in f.readlines()]

setup(
    name=info['name'],
    packages=find_packages('.'),
    version=info['version'],
    description='Toolkit to Hack Your Deep Learning Models',
    long_description=open('setup.rst').read(),
    author=info['authors'],
    url=info['github_url'],
    download_url='{}/tarball/v{}'.format(info['github_url'], info['version']),
    keywords=['AI', 'ML', 'DL', 'deep learning', 'machine learning', 'neural network',
              'deep neural network', 'debug neural networks', 'performance hacking',
              'tensorflow', 'tf'],
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=deps,
    extras_require={
        'tensorflow-gpu':  ['tensorflow-gpu>=1.3'],
        'tensorflow': ['tensorflow>=1.3']
    }
)
