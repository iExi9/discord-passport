from setuptools import setup


setup(
   name='discord_passport',
   version='0.3',
   description='discord-passport is easier way to create simple Oauth with Discord-API',
   license="MIT",
   long_description=open('README.md','r', encoding='utf-8').read(),
   long_description_content_type='text/markdown',
   author='Zaid Ali',
   author_email='email@iexi.xyz',
   keywords=['discord','api','oauth'],
    packages=['discord_passport'],
    install_requires=["requests"],
    package_dir={'discord_passport': 'discord_passport'},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
