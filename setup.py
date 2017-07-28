import os

from setuptools import setup, find_packages, Command

__doc__ = "Flask based web application"


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


setup(
    name='Flask-Demo',
    url='',
    author='',
    author_email='',
    version='0.0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['bumpversion==0.5.3',
                      'Flask==0.12',
                      'Flask-APSCheduler==1.6.0',
                      'Flask-Script==2.0.5',
                      'Flask-Bootstrap==3.3.7.0',
                      'Flask-Cache==0.13.1',
                      'Flask-WTF==0.14',
                      'Flask-SimpleLDAP==1.1.0',
                      'Flask-SQLAlchemy==2.1',
                      'flake8==3.3.0',
                      'gunicorn==19.6.0',
                      'pytest==3.0.3',
                      'mock==2.0.0',
                      'pytest==3.0.3',
                      'requests==2.10.0',
                      'python-magic==0.4.13',
                      ],
    cmdclass={
        'clean': CleanCommand,
    }
)
