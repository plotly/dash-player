import React, { Component } from 'react';
import ReactPlayer from 'react-player';
import { propTypes, defaultProps } from '../components/DashPlayer.react';

export default class DashPlayer extends Component {
    constructor(props) {
        super(props);

        this.updateCurrentTime = this.updateCurrentTime.bind(this);
        this.updateSecondsLoaded = this.updateSecondsLoaded.bind(this);
        this.updateDuration = this.updateDuration.bind(this);
        this.updateIntervals = this.updateIntervals.bind(this);
        this.setSeekTo = this.setSeekTo.bind(this);
        this.ref = this.ref.bind(this);
    }

    updateCurrentTime() {
        const { setProps } = this.props;
        if (this.player !== null) {
            const currentTime = this.player.getCurrentTime();

            if (typeof setProps === 'function') {
                setProps({ currentTime: currentTime });
            }
        }
    }

    updateSecondsLoaded() {
        const { setProps } = this.props;
        if (this.player !== null) {
            const secondsLoaded = this.player.getSecondsLoaded();

            if (typeof setProps === 'function') {
                setProps({ secondsLoaded: secondsLoaded });
            }
        }
    }

    updateDuration() {
        const { setProps } = this.props;
        if (this.player !== null) {
            const duration = this.player.getDuration();

            if (typeof setProps === 'function') {
                setProps({ duration: duration });
            }
        }
    }

    /**
     * When one of the interval props are changed, this clears the currently
     * assigned handle and set it to the new interval value. It works for
     * currentTime, duration and secondsLoaded.
     */
    updateIntervals(prevProps) {
        const { intervalCurrentTime, intervalDuration, intervalSecondsLoaded } =
            this.props;

        // Update interval of current time
        if (
            typeof this.handleCurrentTime === 'undefined' ||
            prevProps.intervalCurrentTime !== intervalCurrentTime
        ) {
            clearInterval(this.handleCurrentTime);
            this.handleCurrentTime = setInterval(
                this.updateCurrentTime,
                intervalCurrentTime
            );
        }
        if (
            typeof this.handleDuration === 'undefined' ||
            prevProps.intervalDuration !== intervalDuration
        ) {
            clearInterval(this.handleDuration);
            this.handleDuration = setInterval(
                this.updateDuration,
                intervalDuration
            );
        }
        if (
            typeof this.handleSecondsLoaded === 'undefined' ||
            prevProps.intervalSecondsLoaded !== intervalSecondsLoaded
        ) {
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
    setSeekTo() {
        const { seekTo, setProps, seekToMode } = this.props;
        console.log(seekToMode);
        if (seekTo !== null && typeof setProps === 'function') {
            this.player.seekTo(seekTo, seekToMode);
            setProps({ seekTo: null });
        }
    }

    componentDidUpdate(prevProps) {
        this.updateIntervals(prevProps);
        this.setSeekTo();
    }

    componentDidMount() {
        this.updateDuration();
    }

    ref(player) {
        this.player = player;
    }

    render() {
        const {
            id,
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
            playsinline,
            className
        } = this.props;

        return (
            <ReactPlayer
                ref={this.ref}
                id={id}
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
                playsinline={playsinline}
                class={className}
            />
        );
    }
}

DashPlayer.defaultProps = defaultProps;
DashPlayer.propTypes = propTypes;
