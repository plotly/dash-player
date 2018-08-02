from setuptools import setup

exec (open('dash_player/version.py').read())

setup(
    name='dash_player',
    version=__version__,
    author='plotly',
    packages=['dash_player'],
    include_package_data=True,
    license='MIT',
    description='A Dash component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, and DailyMotion.',
    install_requires=[]
)
