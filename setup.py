from setuptools import setup
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

name = 'My project'
version = '1.2'
release = '1.2.0'

setup(
        name='MyMath',
        version='0.1',
        release='0.1.0',
        description='Pakcage Test',
        url='http://github.com',
        author='I. Ashraf',
        author_email='i.ashraf@example.com',
        license='MIT',
        packages=['mymath'],
        package_dir={'': 'src'},
        cmdclass=cmdclass,
        # these are optional and override conf.py settings
        command_options={
            'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs')}},
        zip_safe=False)
