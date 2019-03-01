# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPlayer(Component):
    """A DashPlayer component.
A Dash component for playing a variety of URLs, including file paths,
YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud,
and DailyMotion.

Keyword arguments:
- id (string; optional): The ID used to identify this compnent in Dash callbacks
- url (string; optional): The url of a video or song to play
◦  Can be an array or MediaStream object
- playing (boolean; optional): Set to true or false to pause or play the media
- loop (boolean; optional): Set to true or false to loop the media
- controls (boolean; optional): Set to true or false to display native player controls
Vimeo, Twitch and Wistia player will always display controls
- volume (number; optional): Set the volume of the player, between 0 and 1
null uses default volume on all players
- muted (boolean; optional): Mutes the player
Only works if volume is set
- playbackRate (number; optional): Set the playback rate of the player
Only supported by YouTube, Wistia, and file paths
- width (string; optional): Set the width of the player
- height (string; optional): Set the height of the player
- style (dict; optional): Add inline styles to the root element
- playsinline (boolean; optional): Applies the html5 playsinline attribute where supported, which allows
videos to be played inline and will not automatically enter fullscreen
mode when playback begins (for iOS).
- currentTime (number; optional): Returns the number of seconds that have been played
- secondsLoaded (number; optional): Returns the number of seconds that have been loaded
- duration (number; optional): Returns the duration (in seconds) of the currently playing media
- intervalCurrentTime (number; optional): Interval in milliseconds at which currenTtime prop is updated.
- intervalSecondsLoaded (number; optional): Interval in milliseconds at which secondsLoaded prop is updated.
- intervalDuration (number; optional): Interval in milliseconds at which duration prop is updated.
- seekTo (number; optional): Seek to the given number of seconds, or fraction if amount is between 0 and 1"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, url=Component.UNDEFINED, playing=Component.UNDEFINED, loop=Component.UNDEFINED, controls=Component.UNDEFINED, volume=Component.UNDEFINED, muted=Component.UNDEFINED, playbackRate=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, style=Component.UNDEFINED, playsinline=Component.UNDEFINED, currentTime=Component.UNDEFINED, secondsLoaded=Component.UNDEFINED, duration=Component.UNDEFINED, intervalCurrentTime=Component.UNDEFINED, intervalSecondsLoaded=Component.UNDEFINED, intervalDuration=Component.UNDEFINED, seekTo=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'url', 'playing', 'loop', 'controls', 'volume', 'muted', 'playbackRate', 'width', 'height', 'style', 'playsinline', 'currentTime', 'secondsLoaded', 'duration', 'intervalCurrentTime', 'intervalSecondsLoaded', 'intervalDuration', 'seekTo']
        self._type = 'DashPlayer'
        self._namespace = 'dash_player'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'url', 'playing', 'loop', 'controls', 'volume', 'muted', 'playbackRate', 'width', 'height', 'style', 'playsinline', 'currentTime', 'secondsLoaded', 'duration', 'intervalCurrentTime', 'intervalSecondsLoaded', 'intervalDuration', 'seekTo']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashPlayer, self).__init__(**args)
