import codecs
from setuptools import setup, find_packages


TESTS_REQUIRE = [
    'zope.configuration',
    'zope.testrunner',
]

def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()

setup(
    name='nti.i18n',
    version='1.0.0.dev0',
    author='Jason Madden',
    author_email='jason@nextthought.com',
    description="i18n and L10n data and interfaces",
    long_description=_read('README.rst'),
    url="https://github.com/NextThought/nti.i18n",
    license='Apache',
    keywords='i18n l10n zope component iana data locales',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope3',
    ],
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.interface',
        'zope.cachedescriptors',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
    },
)
