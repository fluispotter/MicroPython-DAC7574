import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MicroPython-DAC7574',
    version='0.0.1',
    author='Fluispotter',
    description='MicroPython driver for the DAC7574 digital-to-analog converter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fluispotter/MicroPython-DAC7574',
    license='ISC',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Topic :: System :: Hardware'
    ],
    python_requires='>=3.9',
)
