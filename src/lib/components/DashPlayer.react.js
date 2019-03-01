import React, {Component} from 'react';
import ReactPlayer from 'react-player';
import PropTypes from 'prop-types';

/**
 * A Dash component for playing a variety of URLs, including file paths,
 * YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud,
 * and DailyMotion.
 */
export default class DashPlayer extends Component {
    constructor(props) {
        super(props);

        this.updateCurrentTime = this.updateCurrentTime.bind(this);
        this.updateSecondsLoaded = this.updateSecondsLoaded.bind(this);
        this.updateDuration = this.updateDuration.bind(this);
        this.updateIntervals = this.updateIntervals.bind(this);
        this.setSeekTo = this.setSeekTo.bind(this);
    }

    updateCurrentTime(){
        const {setProps} = this.props;
        if (this.refs.player !== null){
            const currentTime = this.refs.player.getCurrentTime();

            if (typeof setProps  === 'function') {
                setProps({currentTime: currentTime});
            }
        }
    }

    updateSecondsLoaded(){
        const {setProps} = this.props;
        if (this.refs.player !== null){
            const secondsLoaded = this.refs.player.getSecondsLoaded();

            if (typeof setProps  === 'function') {
                setProps({secondsLoaded: secondsLoaded});
            }
        }
    }

    updateDuration(){
        const {setProps} = this.props;
        if (this.refs.player !== null){
            const duration = this.refs.player.getDuration();

            if (typeof setProps  === 'function'){
                setProps({duration: duration});
            }
        }
    }

    /**
     * When one of the interval props are changed, this clears the currently
     * assigned handle and set it to the new interval value. It works for
     * currentTime, duration and secondsLoaded.
     */
    updateIntervals(prevProps){
        const {
            intervalCurrentTime,
            intervalDuration,
            intervalSecondsLoaded
        } = this.props;

        // Update interval of current time
        if (typeof this.handleCurrentTime === 'undefined' ||
            prevProps.intervalCurrentTime !== intervalCurrentTime){
            clearInterval(this.handleCurrentTime);
            this.handleCurrentTime = setInterval(
                this.updateCurrentTime,
                intervalCurrentTime
            );
        }
        if (typeof this.handleDuration === 'undefined' ||
            prevProps.intervalDuration !== intervalDuration){
            clearInterval(this.handleDuration);
            this.handleDuration = setInterval(
                this.updateDuration,
                intervalDuration
            );
        }
        if (typeof this.handleSecondsLoaded === 'undefined' ||
            prevProps.intervalSecondsLoaded !== intervalSecondsLoaded){
            clearInterval(this.handleSecondsLoaded);
            this.handleSecondsLoaded = setInterval(
                this.updateSecondsLoaded,
                intervalSecondsLoaded
            );
        }
    }

    /**
     * Applies the seekTo() method to the player if the seekTo prop
     * contains any value, then set seekTo to null. If seekTo was already
     * null, it doesn't do anything.
     */
    setSeekTo(){
        const {
            seekTo,
            setProps
        } = this.props;

        if (seekTo !== null && typeof setProps  === 'function'){
            this.refs.player.seekTo(seekTo);
            setProps({seekTo: null});
        }
    }

    componentDidUpdate(prevProps){
        this.updateIntervals(prevProps);
        this.setSeekTo();
    }

    render() {
        const {
            url,
            playing,
            loop,
            controls,
            volume,
            muted,
            playbackRate,
            width,
            height,
            style,
            playsinline
        } = this.props;

        return (
            <ReactPlayer
                ref="player"
                url={url}
                playing={playing}
                loop={loop}
                controls={controls}
                volume={volume}
                muted={muted}
                playbackRate={playbackRate}
                width={width}
                height={height}
                style={style}
                playsline={playsinline}
            />
        );
    }
}

DashPlayer.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * The url of a video or song to play
     * ◦  Can be an array or MediaStream object
     */
    url: PropTypes.string,

    /**
     * Set to true or false to pause or play the media
     */
    playing: PropTypes.bool,

    /**
     * Set to true or false to loop the media
     */
    loop: PropTypes.bool,

    /**
     * Set to true or false to display native player controls
     * Vimeo, Twitch and Wistia player will always display controls
     */
    controls: PropTypes.bool,

    /**
     * Set the volume of the player, between 0 and 1
     * null uses default volume on all players
     */
    volume: PropTypes.number,

    /**
     * Mutes the player
     * Only works if volume is set
     */
    muted: PropTypes.bool,

    /**
     * Set the playback rate of the player
     * Only supported by YouTube, Wistia, and file paths
     */
    playbackRate: PropTypes.number,

    /**
     * Set the width of the player
     */
    width: PropTypes.string,

    /**
     * Set the height of the player
     */
    height: PropTypes.string,

    /**
     * Add inline styles to the root element
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
     * Returns the number of seconds that have been played
     */
    currentTime: PropTypes.number,

    /**
     * Returns the number of seconds that have been loaded
     */
    secondsLoaded: PropTypes.number,

    /**
     * Returns the duration (in seconds) of the currently playing media
     */
    duration: PropTypes.number,

    /**
     * Interval in milliseconds at which currenTtime prop is updated.
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