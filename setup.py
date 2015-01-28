from setuptools import setup, find_packages


setup(
    name='cs399-band',
    version='0.1.0',
    description='CS399 Theatre',
    long_description=open('README.md').read(),
    keywords=[
        'class',
        'django',
        'nau'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/yourbuddyconner/cs399-theatre',
    download_url='https://github.com/yourbuddyconner/cs399-theatre/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
