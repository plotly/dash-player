% Auto-generated: do not edit by hand
\name{dashPlayer}

\alias{dashPlayer}

\title{DashPlayer component}

\description{
A Dash component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, and DailyMotion.
}

\usage{
dashPlayer(id=NULL, className=NULL, controls=NULL, currentTime=NULL,
duration=NULL, height=NULL, intervalCurrentTime=NULL,
intervalDuration=NULL, intervalSecondsLoaded=NULL,
loop=NULL, muted=NULL, playbackRate=NULL, playing=NULL,
playsinline=NULL, secondsLoaded=NULL, seekTo=NULL,
seekToMode=NULL, style=NULL, url=NULL, volume=NULL,
width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Used to identify the CSS class of the Dash Player component}

\item{controls}{Logical. Set to true or false to display native player controls
Vimeo, Twitch and Wistia player will always display controls}

\item{currentTime}{Numeric. Returns the number of seconds that have been played.}

\item{duration}{Numeric. Returns the duration (in seconds) of the currently playing media.}

\item{height}{Character. A number or string representing the pixel height of the player.}

\item{intervalCurrentTime}{Numeric. Interval in milliseconds at which currentTime prop is updated.}

\item{intervalDuration}{Numeric. Interval in milliseconds at which duration prop is updated.}

\item{intervalSecondsLoaded}{Numeric. Interval in milliseconds at which secondsLoaded prop is updated.}

\item{loop}{Logical. Whether or not the media will loop once the player reaches the end.
Can be set to True or False to set looping on or off, respectively.}

\item{muted}{Logical. Set to true or false to mute or unmute player volume, respectively.
Only works if volume is set.}

\item{playbackRate}{Numeric. Set the playback rate of the player
Only supported by YouTube, Wistia, and file paths.}

\item{playing}{Logical. Whether or not the media is currently playing. Can be set to True
or False to play and pause the media, respectively.}

\item{playsinline}{Logical. Applies the html5 playsinline attribute where supported, which allows
videos to be played inline and will not automatically enter fullscreen
mode when playback begins (for iOS).}

\item{secondsLoaded}{Numeric. Returns the number of seconds that have been loaded.}

\item{seekTo}{Numeric. Seek to the given number of seconds, or fraction if amount is between 0 and 1}

\item{seekToMode}{Character. Seek to mode (can be "seconds" or "fraction"), overwrites default behaviour
of seekTo that uses fraction or seconds depending on value.}

\item{style}{Named list. Optional additional CSS styles. If width or height are supplied within style,
then this will override the component-level width or height}

\item{url}{Character. The url of the media to be played.}

\item{volume}{Numeric. A number between 0 and 1 representing the volume of the player.
If set to None, Dash Player ises default volume on all players.}

\item{width}{Character. A number or string representing the pixel width of the player.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

