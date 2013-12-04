try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Durell Smith',
    'url': '#',
    'download_url': 'Where to download it at',
    'author_email': 'durell.smith@sagacious.io',
    'version': '0.1',
    'install_requires;': ['nose'],
    'packages': ['ex47']
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
