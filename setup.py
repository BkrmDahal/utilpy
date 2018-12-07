from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='utilpy',
    version='0.1.3',
    description='Collection of utils that we use often. ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BkrmDahal/utilpy',
    author='Bikram Dahal (Arch analytics)',
    author_email='bikram@archanalaytics.ai',
    license='MIT',
    python_requires='>=3',
    packages=[
        'utilpy'
    ],
    install_requires=[
        'PyYAML',
        'requests',
        'beautifulsoup4',
        'patool'
    ],
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    zip_safe=False
)
