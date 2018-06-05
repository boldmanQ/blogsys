from setuptools import setup, find_packages
packages = find_packages('blogsys')
print packages
setup(
    name='blogsys',
    version='0.1',
    description='Blog System base on Django',
    author='boldmanQ',
    author_email='475131479@qq.com',
    url='https://www.the5fire.com',
    packages=find_packages('blogsys'),
    package_dir={'': 'blogsys'},
#    package_data={
#        'blogsys': [
#            'themes/default/static/css/*.css',
#            'themes/default/static/js/*.js',
#            'themes/default/templates/*/*.html',
    include_package_data=True,
    install_requires=[
        'django==1.11.10',
    ],
    scripts=[
        'blogsys/manage.py',
    ],
)
