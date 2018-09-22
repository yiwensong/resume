import setuptools

setuptools.setup(
    name='md-resume',
    version='0.1.0',
    license='MIT',
    author='yiwen song',
    author_email='songzgy@gmail.com',
    url='https://github.com/yiwensong/resume',
    description='markdown resume prettifier',
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=[
        'Markdown',
    ],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[
        'resume',
        'markdown',
        'pretty',
        'yiwen',
    ],
    entry_points={
        'console_scripts': [
            'generate-resume-pdf = md_resume:main',
        ],
    },
)
