import React, {Component} from 'react';
import ReactPlayer from 'react-player';
import PropTypes from 'prop-types';

/**
 * A Dash component for playing a variety of URLs, including file paths,
 * YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud,
 * and DailyMotion.
 */
export default class PlayerComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {value: props.value};

        this.updateCurrentTime = this.updateCurrentTime.bind(this);
        this.updateInstanceMethods = this.updateInstanceMethods.bind(this);
        this.setSeekTo = this.setSeekTo.bind(this);
        setInterval(this.updateCurrentTime, 40);  // 25 FPS
        setInterval(this.updateInstanceMethods, 500);
    }

    updateCurrentTime(){
        const {setProps} = this.props;
        const currentTime = this.refs.player.getCurrentTime();
        if (setProps  !== null) {
            setProps({currentTime: currentTime});
        }
    }

    updateInstanceMethods(){
        const {setProps} = this.props;
        const secondsLoaded = this.refs.player.getSecondsLoaded();
        const duration = this.refs.player.getDuration();

        if (setProps  !== null) {
            setProps({
                secondsLoaded: secondsLoaded,
                duration: duration
            });
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

        if (seekTo !== null && setProps !== null){
            this.refs.player.seekTo(seekTo);
            setProps({seekTo: null});
        }
    }

    componentDidUpdate(){
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
            progressInterval,
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
                progressInterval={progressInterval}
                playsline={playsinline}
            />

        );
    }
}

PlayerComponent.propTypes = {
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
     * The time between onProgress callbacks, in milliseconds
     */
    progressInterval: PropTypes.string,

    /**
     * Applies the playsinline attribute where supported
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
     * Seek to the given number of seconds, or fraction if amount is between 0 and 1
     */
    seekTo: PropTypes.number
};

PlayerComponent.defaultProps = {
    playing: false,
    loop: false,
    controls: false,
    volume: null,
    muted: false,
    playbackRate: 1,
    width: '640px',
    height: '360px',
    style:{},
    progressInterval: 1000,
    playsinline: false,
    seekTo: null
};