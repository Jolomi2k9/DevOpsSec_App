from setuptools import setup

# Read requirements.txt and use its contents as the install requirements
# with open('requirements.txt', 'r', 'utf-8-sig') as f:
#     requirements = f.read().splitlines()

with open('requirements.txt', encoding='utf-8-sig') as f:
    requirements = f.read().splitlines()

setup(
    name='Volun2k9App',
    version='0.1.0',
    packages=['.'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)