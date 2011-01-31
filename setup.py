import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def package_data(package):
    package_data = []
    for dirpath, dirnames, filenames in os.walk(
            os.path.join(os.path.dirname(__file__), package)):
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            continue
        elif filenames:
            for f in filenames:
                package_data.append(
                    os.path.join(dirpath[len(package)+len(os.sep):], f))
    return {package: package_data}

setup(
    name='django-admin-notifications',
    version='0.6.3',
    description="A simple app to allow apps to register notifications "
                "that can be displayed in the admin via a template tag.",
    long_description=read('README.rst'),
    author='Andy Baker',
    author_email='andy@andybak.net',
    license='BSD',
    url='http://github.com/andybak/django-admin-notifications/',
    packages=[
        'admin_notifications',
    ],
    package_data=package_data('admin_notifications'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)