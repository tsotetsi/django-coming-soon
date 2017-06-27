from setuptools import setup, find_packages

setup(
    name='django-coming-soon',
    version='0.0.1',
    description='Django Coming Soon.',
    author='Thapelo Tsotetsi',
    author_email='info@tsotetsithapelo.com',
    url='http://example.com',
    install_requires=[
        'Django',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
