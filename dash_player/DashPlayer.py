# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.types import NumberType  # noqa: F401
except ImportError:
    # Backwards compatibility for dash<=4.1.0
    if typing.TYPE_CHECKING:
        raise
    NumberType = typing.Union[  # noqa: F401
        typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
    ]

ComponentSingleType = typing.Union[str, int, float, Component, None]
ComponentType = typing.Union[
    ComponentSingleType,
    typing.Sequence[ComponentSingleType],
]


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

- url (string; optional):
    The url of the media to be played.

- volume (number; optional):
    A number between 0 and 1 representing the volume of the player. If
    set to None, Dash Player ises default volume on all players.

- width (string; default '640px'):
    A number or string representing the pixel width of the player."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_player'
    _type = 'DashPlayer'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        playing: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        controls: typing.Optional[bool] = None,
        volume: typing.Optional[NumberType] = None,
        muted: typing.Optional[bool] = None,
        playbackRate: typing.Optional[NumberType] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        playsinline: typing.Optional[bool] = None,
        currentTime: typing.Optional[NumberType] = None,
        secondsLoaded: typing.Optional[NumberType] = None,
        duration: typing.Optional[NumberType] = None,
        intervalCurrentTime: typing.Optional[NumberType] = None,
        intervalSecondsLoaded: typing.Optional[NumberType] = None,
        intervalDuration: typing.Optional[NumberType] = None,
        seekTo: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'controls', 'currentTime', 'duration', 'height', 'intervalCurrentTime', 'intervalDuration', 'intervalSecondsLoaded', 'loop', 'muted', 'playbackRate', 'playing', 'playsinline', 'secondsLoaded', 'seekTo', 'style', 'url', 'volume', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'controls', 'currentTime', 'duration', 'height', 'intervalCurrentTime', 'intervalDuration', 'intervalSecondsLoaded', 'loop', 'muted', 'playbackRate', 'playing', 'playsinline', 'secondsLoaded', 'seekTo', 'style', 'url', 'volume', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashPlayer, self).__init__(**args)

setattr(DashPlayer, "__init__", _explicitize_args(DashPlayer.__init__))
