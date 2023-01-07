from setuptools import setup

versionContext = {}
with open('pytest_session_fixture_globalize/version.py') as f:
    exec(f.read(), versionContext)

setup(
    name='pytest-session-fixture-globalize',
    description='py.test plugin to make session fixtures behave as if written in conftest, even if it is written in some modules',
    long_description=open("README.md").read(),
    version=versionContext['__version__'],
    url='https://github.com/cielavenir/pytest-session-fixture-globalize',
    license='BSD',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['pytest_session_fixture_globalize'],
    entry_points={'pytest11': ['session_fixture_globalize = pytest_session_fixture_globalize.pytest_session_fixture_globalize']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=3.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
