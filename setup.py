from setuptools import setup, find_packages
packages = find_packages('blogsys')
print packages
setup(
    name='blogsys',
    version='1.2.2',
    description='Blog System base on Django',
    author='boldmanQ',
    author_email='475131479@qq.com',
    url='https://www.boldman.top',
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
        'django-rest-framework==0.1.0',
        'django-ckeditor==5.4.0',
        'django-debug-toolbar==1.9.1',
        'django-redis==4.9.0',
        'Markdown==2.6.11',
        'mysqlclient==1.3.12',
        'Pillow==5.1.0',
        #'xadmin==0.6.1',
        'django-reversion==2.0.13',
        'redis',
        'djangorestframework==3.8.2',
        'coreapi==2.3.3',
    ],
    scripts=[
        'blogsys/manage.py',
    ],
)
