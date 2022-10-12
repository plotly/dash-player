# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashPlayer <- function(id=NULL, className=NULL, controls=NULL, currentTime=NULL, duration=NULL, height=NULL, intervalCurrentTime=NULL, intervalDuration=NULL, intervalSecondsLoaded=NULL, loop=NULL, muted=NULL, playbackRate=NULL, playing=NULL, playsinline=NULL, secondsLoaded=NULL, seekTo=NULL, style=NULL, url=NULL, volume=NULL, width=NULL) {
    
    props <- list(id=id, className=className, controls=controls, currentTime=currentTime, duration=duration, height=height, intervalCurrentTime=intervalCurrentTime, intervalDuration=intervalDuration, intervalSecondsLoaded=intervalSecondsLoaded, loop=loop, muted=muted, playbackRate=playbackRate, playing=playing, playsinline=playsinline, secondsLoaded=secondsLoaded, seekTo=seekTo, style=style, url=url, volume=volume, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashPlayer',
        namespace = 'dash_player',
        propNames = c('id', 'className', 'controls', 'currentTime', 'duration', 'height', 'intervalCurrentTime', 'intervalDuration', 'intervalSecondsLoaded', 'loop', 'muted', 'playbackRate', 'playing', 'playsinline', 'secondsLoaded', 'seekTo', 'style', 'url', 'volume', 'width'),
        package = 'dashPlayer'
        )

    structure(component, class = c('dash_component', 'list'))
}
