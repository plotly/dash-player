import React, {Component} from 'react';
import ReactPlayer from 'react-player';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class PlayerComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {value: props.value};

        this.updateCurrentTime = this.updateCurrentTime.bind(this);
        this.updateInstanceMethods = this.updateInstanceMethods.bind(this);
        // this.getCurrentTime = this.getCurrentTime.bind(this);
        // this.getSecondsLoaded = this.getSecondsLoaded.bind(this);
        // this.getDuration = this.getDuration.bind(this);
        // this.getInternalPlayer = this.getInternalPlayer.bind(this);
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
    duration: PropTypes.number
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
    progressInterval: 1000,
    playsinline: false
};