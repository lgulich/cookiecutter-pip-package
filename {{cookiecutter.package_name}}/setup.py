from pathlib import Path

import setuptools

from src.{{cookiecutter.package_name}}.version import __version__

file_path = Path(__file__)
with open(file_path.parent / 'README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='{{cookiecutter.package_name}}',
    version=__version__,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/lgulich/{{cookiecutter.package_name}}',
    description= '{{cookiecutter.package_description}}',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Natural Language :: English',
    ],
    license='{{cookiecutter.license}}',
    package_dir={},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    package_data={'{{cookiecutter.package_name}}': ['py.typed']},
    scripts=[
        'scripts/{{cookiecutter.package_name}}',
    ],
    python_requires='>=3.8',
)
