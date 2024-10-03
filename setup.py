import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fico',
    version='0.0.3',
    author='fabiosaracco',
    description='Fitness and Complexity calculator.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fabiosaracco/fico',
    license='MIT',
    packages=['fico'],
    install_request=['numpy'],
)
