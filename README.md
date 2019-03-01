Dash Player: Control and play videos using Dash

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
[![GitHub stars](https://img.shields.io/github/stars/xhlulu/dash-player.svg)](https://github.com/xhlulu/dash-player/stargazers)

Dash Player is a dash component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, and DailyMotion. It is wrapped around the react-player component.

You can find a [demo of the component here](http://dash-player-usage.herokuapp.com).

For updates and more, please see the dash community discussion on Dash Player.

This is a custom community component, so if your organization or company is interested in sponsoring enhancements to this project, [please reach out to the Plotly Dash team](https://plot.ly/dash/pricing).

Example from `usage-advanced.py`

![Gif demoing Dash Player](images/usage-advanced.gif)


## Getting started

Here are the following steps to get started with your own apps
```sh
$ git clone https://github.com/xhlulu/dash-player.git
$ cd dash-player
$ npm install
$ python usage-advanced.py
```

Once that done, you can copy the `dash_player` package in the folder of your app, and import it within your app.

## Usage

`usage.py` provides you with the basic functionality of the app. Use it to learn how to use the component.

`usage-methods.py` lets you test the props that are updated at an interval, which are originally react instance methods.

`usage-advanced.py` gives an overview of the full functionality of the component, and serves as an extensive testing tool.

## Documentation


Prop | Description | Default
---- | ----------- | -------
`id` | The ID used to identify this compnent in Dash callbacks |
`url` | The url of a video or song to play<br/>&nbsp; ◦ &nbsp;Can be an [array](#multiple-sources-and-tracks) or [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream) object
`playing` | Set to `true` or `false` to pause or play the media | `false`
`loop` | Set to `true` or `false` to loop the media | `false`
`controls` | Set to `true` or `false` to display native player controls<br />&nbsp; ◦ &nbsp;Vimeo, Twitch and Wistia player will always display controls | `false`
`volume` | Set the volume of the player, between `0` and `1`<br/>&nbsp; ◦ &nbsp;`null` uses default volume on all players [`#357`](https://github.com/CookPete/react-player/issues/357) | `null`
`muted` | Mutes the player<br/>&nbsp; ◦ &nbsp;Only works if `volume` is set | `false`
`width` | Set the width of the player | `640px`
`height` | Set the height of the player | `360px`
`style` | Add [inline styles](https://facebook.github.io/react/tips/inline-styles.html) to the root element | `{}`
`playsinline` | Applies the `playsinline` attribute where supported | `false`
`currentTime` | Returns the number of seconds that have been played
`secondsLoaded` | Returns the number of seconds that have been loaded
`duration` | Returns the duration (in seconds) of the currently playing media
`intervalCurrentTime`| Interval in milliseconds at which currenTtime prop is updated. | `40`
`intervalSecondsLoaded` | Interval in milliseconds at which secondsLoaded prop is updated. | `500`
`intervalDuration` | Interval in milliseconds at which duration prop is updated. | `500`
`seekTo` | Seek to the given number of seconds, or fraction if amount is between 0 and 1 | `null`


## Built With

* [Dash](https://dash.plot.ly/) - Main server and interactive components
* [react-player](https://www.npmjs.com/package/react-player) - The react component that was wrapped by this

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Xing Han** - *Initial Work* - [@xhlulu](https://github.com/xhlulu)
* **Chris** - *Code Review*

See also the list of [contributors](https://github.com/xhlulu/dash-player/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments