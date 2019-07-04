% Auto-generated: do not edit by hand
\name{dashPlayer}

\alias{dashPlayer}

\title{DashPlayer component}

\description{
A Dash component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, and DailyMotion.
}

\usage{
dashPlayer(id=NULL, url=NULL, playing=NULL, loop=NULL, controls=NULL, volume=NULL,
muted=NULL, playbackRate=NULL, width=NULL, height=NULL, style=NULL,
playsinline=NULL, currentTime=NULL, secondsLoaded=NULL, duration=NULL,
intervalCurrentTime=NULL, intervalSecondsLoaded=NULL, intervalDuration=NULL,
seekTo=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this compnent in Dash callbacks}

\item{url}{Character. The url of a video or song to play
◦  Can be an array or MediaStream object}

\item{playing}{Logical. Set to true or false to pause or play the media}

\item{loop}{Logical. Set to true or false to loop the media}

\item{controls}{Logical. Set to true or false to display native player controls
Vimeo, Twitch and Wistia player will always display controls}

\item{volume}{Numeric. Set the volume of the player, between 0 and 1
null uses default volume on all players}

\item{muted}{Logical. Mutes the player
Only works if volume is set}

\item{playbackRate}{Numeric. Set the playback rate of the player
Only supported by YouTube, Wistia, and file paths}

\item{width}{Character. Set the width of the player}

\item{height}{Character. Set the height of the player}

\item{style}{Named list. Add inline styles to the root element}

\item{playsinline}{Logical. Applies the html5 playsinline attribute where supported, which allows
videos to be played inline and will not automatically enter fullscreen
mode when playback begins (for iOS).}

\item{currentTime}{Numeric. Returns the number of seconds that have been played}

\item{secondsLoaded}{Numeric. Returns the number of seconds that have been loaded}

\item{duration}{Numeric. Returns the duration (in seconds) of the currently playing media}

\item{intervalCurrentTime}{Numeric. Interval in milliseconds at which currenTtime prop is updated.}

\item{intervalSecondsLoaded}{Numeric. Interval in milliseconds at which secondsLoaded prop is updated.}

\item{intervalDuration}{Numeric. Interval in milliseconds at which duration prop is updated.}

\item{seekTo}{Numeric. Seek to the given number of seconds, or fraction if amount is between 0 and 1}
}

\examples{
\dontrun{
library(dash)
library(dashHtmlComponents)
library(dashCoreComponents)
library(dashPlayer)

app <- Dash$new()

app$layout(
  htmlDiv(list(
    htmlDiv(
      children = list(
            dashPlayer(
                id = 'video-player',
                controls = TRUE,
                width='100\%'
            )
      )
    ),
    htmlDiv(list(
      dccInput(id = 'input-url',
               value = 'http://media.w3.org/2010/05/bunny/movie.mp4'),
      htmlButton(children = 'Change URL',
                 id = 'button-update-url')
    )
  )
  )
  )
)

app$callback(output=list(id='video-player', property='url'),
             params=list(
               input(id='button-update-url', property='n_clicks'),
               state(id='input-url', property='value')),
             function(n_clicks, value)
             {
               return(value)
             }
)

app$run_server()
}
}
