import React, {Component, lazy, Suspense} from 'react';
import PropTypes from 'prop-types';

const RealDashPlayer = lazy(() => import(/* webpackChunkName: "dashplayer" */ '../fragments/DashPlayer.react'));

/**
 * A Dash component for playing a variety of URLs, including file paths,
 * YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud,
 * and DailyMotion.
 */

export default class DashPlayer extends Component {
    render() {
        return (
            <Suspense fallback={null}>
                <RealDashPlayer {...this.props} />
            </Suspense>
        );
    }
}

DashPlayer.defaultProps = {
    playing: false,
    loop: false,
    controls: false,
    volume: null,
    muted: false,
    playbackRate: 1,
    width: '640px',
    height: '360px',
    style:{},
    playsinline: false,
    seekTo: null,
    intervalCurrentTime: 100,
    intervalSecondsLoaded: 500,
    intervalDuration: 500
};

DashPlayer.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Used to identify the CSS class of the Dash Player component
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * The url of the media to be played.
     */
    url: PropTypes.string,

    /**
     * Whether or not the media is currently playing. Can be set to True
     * or False to play and pause the media, respectively.
     */
    playing: PropTypes.bool,

    /**
     * Whether or not the media will loop once the player reaches the end.
     * Can be set to True or False to set looping on or off, respectively.
     */
    loop: PropTypes.bool,

    /**
     * Set to true or false to display native player controls
     * Vimeo, Twitch and Wistia player will always display controls
     */
    controls: PropTypes.bool,

    /**
     * A number between 0 and 1 representing the volume of the player.
     * If set to None, Dash Player ises default volume on all players.
     */
    volume: PropTypes.number,

    /**
     * Set to true or false to mute or unmute player volume, respectively.
     * Only works if volume is set.
     */
    muted: PropTypes.bool,

    /**
     * Set the playback rate of the player
     * Only supported by YouTube, Wistia, and file paths.
     */
    playbackRate: PropTypes.number,

    /**
     * A number or string representing the pixel width of the player.
     */
    width: PropTypes.string,

    /**
     * A number or string representing the pixel height of the player.
     */
    height: PropTypes.string,

    /**
     * Optional additional CSS styles. If width or height are supplied within style,
     * then this will override the component-level width or height
     */
    style: PropTypes.object,

    /**
     * Applies the html5 playsinline attribute where supported, which allows
     * videos to be played inline and will not automatically enter fullscreen
     * mode when playback begins (for iOS).
     */
    playsinline: PropTypes.bool,

    // Below are instance Methods that are updated at a fixed intervals, and
    // used as a properties in dash callbacks.
    /**
     * Returns the number of seconds that have been played.
     */
    currentTime: PropTypes.number,

    /**
     * Returns the number of seconds that have been loaded.
     */
    secondsLoaded: PropTypes.number,

    /**
     * Returns the duration (in seconds) of the currently playing media.
     */
    duration: PropTypes.number,

    /**
     * Interval in milliseconds at which currentTime prop is updated.
     */
    intervalCurrentTime: PropTypes.number,

    /**
     * Interval in milliseconds at which secondsLoaded prop is updated.
     */
    intervalSecondsLoaded: PropTypes.number,

    /**
     * Interval in milliseconds at which duration prop is updated.
     */
    intervalDuration: PropTypes.number,

    /**
     * Seek to the given number of seconds, or fraction if amount is between 0 and 1
     */
    seekTo: PropTypes.number
};

export const propTypes = DashPlayer.propTypes;
export const defaultProps = DashPlayer.defaultProps;