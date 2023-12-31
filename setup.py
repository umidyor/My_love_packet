from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='mylove',
    version='1.1.0',
    description='Drawing picture for loves',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Umidyor',
    author_email='umidyor007@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='drawing love,love picture',
    packages=find_packages(),
    install_requires=['pillow','requests'],
)