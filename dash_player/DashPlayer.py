# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPlayer(Component):
    """A DashPlayer component.
A Dash component for playing a variety of URLs, including file paths,
YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud,
and DailyMotion.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Used to identify the CSS class of the Dash Player component.

- controls (boolean; default False):
    Set to True or False to display native player controls Vimeo,
    Twitch and Wistia player will always display controls.

- currentTime (number; optional):
    Returns the number of seconds that have been played.

- duration (number; optional):
    Returns the duration (in seconds) of the currently playing media.

- height (string; default '360px'):
    A number or string representing the pixel height of the player.

- intervalCurrentTime (number; default 100):
    Interval in milliseconds at which currentTime prop is updated.

- intervalDuration (number; default 500):
    Interval in milliseconds at which duration prop is updated.

- intervalSecondsLoaded (number; default 500):
    Interval in milliseconds at which secondsLoaded prop is updated.

- loop (boolean; default False):
    Whether or not the media will loop once the player reaches the
    end. Can be set to True or False to set looping on or off,
    respectively.

- muted (boolean; default False):
    Set to True or False to mute or unmute player volume,
    respectively. Only works if volume is set.

- playbackRate (number; default 1):
    Set the playback rate of the player Only supported by YouTube,
    Wistia, and file paths.

- playing (boolean; default False):
    Whether or not the media is currently playing. Can be set to True
    or False to play and pause the media, respectively.

- playsinline (boolean; default False):
    Applies the html5 playsinline attribute where supported, which
    allows videos to be played inline and will not automatically enter
    fullscreen mode when playback begins (for iOS).

- secondsLoaded (number; optional):
    Returns the number of seconds that have been loaded.

- seekTo (number; optional):
    Seek to the given number of seconds, or fraction if amount is
    between 0 and 1.

- style (dict; optional):
    Optional additional CSS styles. If width or height are supplied
    within style, then this will override the component-level width or
    height.

- url (string; optional):
    The url of the media to be played.

- volume (number; optional):
    A number between 0 and 1 representing the volume of the player. If
    set to None, Dash Player ises default volume on all players.

- width (string; default '640px'):
    A number or string representing the pixel width of the player."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_player'
    _type = 'DashPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, url=Component.UNDEFINED, playing=Component.UNDEFINED, loop=Component.UNDEFINED, controls=Component.UNDEFINED, volume=Component.UNDEFINED, muted=Component.UNDEFINED, playbackRate=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, style=Component.UNDEFINED, playsinline=Component.UNDEFINED, currentTime=Component.UNDEFINED, secondsLoaded=Component.UNDEFINED, duration=Component.UNDEFINED, intervalCurrentTime=Component.UNDEFINED, intervalSecondsLoaded=Component.UNDEFINED, intervalDuration=Component.UNDEFINED, seekTo=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'controls', 'currentTime', 'duration', 'height', 'intervalCurrentTime', 'intervalDuration', 'intervalSecondsLoaded', 'loop', 'muted', 'playbackRate', 'playing', 'playsinline', 'secondsLoaded', 'seekTo', 'style', 'url', 'volume', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'controls', 'currentTime', 'duration', 'height', 'intervalCurrentTime', 'intervalDuration', 'intervalSecondsLoaded', 'loop', 'muted', 'playbackRate', 'playing', 'playsinline', 'secondsLoaded', 'seekTo', 'style', 'url', 'volume', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashPlayer, self).__init__(**args)
