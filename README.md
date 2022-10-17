# Dash Player

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
[![GitHub stars](https://img.shields.io/github/stars/xhlulu/dash-player.svg)](https://github.com/xhlulu/dash-player/stargazers)

Dash Player is a Dash component for playing a variety of URLs, including file paths, YouTube, Facebook, Twitch, SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, and DailyMotion. It is wrapped around the [ReactPlayer](https://github.com/cookpete/react-player) component.

For updates and more, please see the ongoing changes to this repository's issue tracker or the Dash community discussion on Dash Player.

This is a custom community component, so if your organization or company is interested in sponsoring enhancements to this project, [please reach out to the Plotly Dash team](https://plot.ly/dash/pricing).

## Getting started

Here are the following steps to get started with using Dash Player in your own Dash apps

```sh
$ git clone https://github.com/plotly/dash-player
$ cd dash-player
$ npm install
```

Once that's done, you can copy the `dash_player` package in the folder of your app, and import it within your app.

## Build manually

To generate builds manually, run the following:

```sh
$ npm install webpack webpack-cli
$ npm run build
```

## Usage

`usage.py` provides you with the basic functionality of the app. Use it to learn the most basic implementation of a Dash Player component.

`usage-methods.py` allows you to test properties that are updated at an interval.

`usage-advanced.py` gives an overview of the full functionality of the component, and serves as an extensive testing tool.

## Documentation

| Prop                    | Description                                                                                                                                                                       | Default |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `id`                    | The ID used to identify this component in Dash callbacks.                                                                                                                         |
| `className`             | The CSS class used to identify this component in external stylesheets.                                                                                                            |
| `url`                   | The url of the media to be played.                                                                                                                                                |
| `playing`               | Whether or not the media is currently playing. Can be set to `True` or `False` to play and pause the media, respectively.                                                         | `false` |
| `loop`                  | Whether or not the media will loop once the player reaches the end. Can be set to `True` or `False` to set looping on or off, respectively.                                       | `false` |
| `controls`              | Set to true or false to display native player controls. Vimeo, Twitch and Wistia player will always display controls.                                                             | `false` |
| `volume`                | A number between `0` and `1` representing the volume of the player. If set to None, Dash Player ises default volume on all players.                                               | `null`  |
| `muted`                 | Set to true or false to mute or unmute player volume, respectively. Only works if volume is set.                                                                                  | `false` |
| `playbackRate`          | Set the playback rate of the player (only supported by YouTube, Wistia, and file paths).                                                                                          |
| `width`                 | A number or string representing the pixel width of the player.                                                                                                                    | `640px` |
| `height`                | A number or string representing the pixel height of the player.                                                                                                                   | `360px` |
| `style`                 | Optional additional CSS styles. If width or height are supplied within style, then this will override the component-level width or height.                                        | `{}`    |
| `playsinline`           | Applies the html5 playsinline attribute where supported, which allows videos to be played inline and will not automatically enter fullscreen mode when playback begins (for iOS). | `false` |
| `currentTime`           | Returns the number of seconds that have been played                                                                                                                               |
| `secondsLoaded`         | Returns the number of seconds that have been loaded                                                                                                                               |
| `duration`              | Returns the duration (in seconds) of the currently playing media                                                                                                                  |
| `intervalCurrentTime`   | Interval in milliseconds at which currenTtime prop is updated.                                                                                                                    | `40`    |
| `intervalSecondsLoaded` | Interval in milliseconds at which secondsLoaded prop is updated.                                                                                                                  | `500`   |
| `intervalDuration`      | Interval in milliseconds at which duration prop is updated.                                                                                                                       | `500`   |
| `seekTo`                | Seek to the given number of seconds, or fraction if amount is between `0` and `1`                                                                                                 | `null`  |

## Built With

- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [ReactPlayer](https://www.npmjs.com/package/react-player) - The react component that was wrapped by this

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Xing Han** - _Initial Work_ - [@xhlulu](https://github.com/xhlulu)
- **Alex Hsu** - _Maintainer/Ongoing Developer_ - [@alexshoe](https://github.com/alexshoe)
- **Chris** - _Code Review_

See also the list of [contributors](https://github.com/xhlulu/dash-player/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
