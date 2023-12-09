from setuptools import setup

requirements = [
    'blinker==1.7.0',
    'click==8.1.7',
    'colorama==0.4.6',
    'Flask==3.0.0',
    'Flask-SQLAlchemy==3.1.1',
    'greenlet==3.0.1',
    'itsdangerous==2.1.2',
    'Jinja2==3.1.2',
    'MarkupSafe==2.1.3',
    'SQLAlchemy==2.0.23',
    'typing_extensions==4.8.0',
    'Werkzeug==3.0.1',
    'gunicorn'
]

setup(
    name='Volun2k9App',
    version='0.1.0',
    packages=['.'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)