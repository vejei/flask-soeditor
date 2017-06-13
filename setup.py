from setuptools import setup


LONG_DESCRIPTION = open('README.md').read()


setup(
    name='Flask-SOEditor',
    version='0.1.1a',
    url='https://github.com/zeleven/flask-soeditor',
    license='MIT',
    author='zeleven',
    author_email='chengsmo@outlook.com',
    description='A Stack Overflow editor extension for Flask.',
    long_description=LONG_DESCRIPTION,
    packages=['flask_soeditor'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
