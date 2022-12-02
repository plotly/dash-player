from textwrap import dedent

from dash import Dash, dcc, html, Input, Output, State, ALL, ctx, no_update
import dash_player

app = Dash(__name__)
server = app.server

app.scripts.config.serve_locally = True

urls = {
    "mp4": "https://media.w3.org/2010/05/bunny/trailer.mp4",
    "mp3": " https://media.w3.org/2010/07/bunny/04-Death_Becomes_Fur.mp3",
    "webm": "https://media.w3.org/2010/05/sintel/trailer.webm",
    "ogv": "http://media.w3.org/2010/05/bunny/movie.ogv",
    "Youtube": "https://www.youtube.com/watch?v=sea2K4AuPOk",
}

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    style={"width": "45%", "padding": "10px"},
                    children=[
                        html.H1(
                            "dash-player Advanced Usage", style={"marginTop": "0px"}
                        ),
                        dash_player.DashPlayer(
                            id="video-player",
                            url="https://media.w3.org/2010/05/sintel/trailer.mp4",
                            controls=True,
                            width="100%",
                            height="250px",
                        ),
                        dcc.Input(
                            id="input-url",
                            value="https://media.w3.org/2010/05/sintel/trailer.mp4",
                            style={"width": "calc(100% - 110px)"},
                        ),
                        html.Button(
                            "Change URL",
                            id="button-update-url",
                            style={"width": "100px", "margin": "10px 0px"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Markdown("### Player Info"),
                                        html.Div(
                                            id="div-current-time",
                                            style={"margin": "10px 0px"},
                                        ),
                                        html.Div(
                                            id="div-seconds-loaded",
                                            style={"margin": "10px 0px"},
                                        ),
                                        html.Div(
                                            id="div-duration",
                                            style={"margin": "10px 0px"},
                                        ),
                                    ],
                                    id="div-video-info",
                                    style={"width": "60%"},
                                ),
                                html.Div(
                                    [
                                        dcc.Markdown("### Video Examples"),
                                        html.Div(
                                            [
                                                html.Button(
                                                    i,
                                                    id={
                                                        "type": "url-btn",
                                                        "value": urls[i],
                                                    },
                                                )
                                                for i in urls
                                            ],
                                            style={
                                                "display": "flex",
                                                "flexDirection": "column",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flexDirection": "row",
                                "padding": "10px",
                            },
                        ),
                    ],
                ),
                html.Div(
                    style={"width": "45%", "padding": "10px"},
                    children=[
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="radio-bool-props",
                                    options=[
                                        {"label": val.capitalize(), "value": val}
                                        for val in [
                                            "playing",
                                            "loop",
                                            "controls",
                                            "muted",
                                        ]
                                    ],
                                    value=["controls"],
                                ),
                                html.Div(
                                    [
                                        dcc.Input(
                                            id="seekto-input",
                                            type="number",
                                            placeholder="seekTo value",
                                        ),
                                        html.Button("seekTo", id="seekto-btn"),
                                    ],
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flexDirection": "row",
                                "justifyContent": "space-between",
                                "marginBottom": "5px",
                            },
                        ),
                        html.P("Volume:", style={"marginTop": "30px"}),
                        dcc.Slider(
                            id="slider-volume",
                            min=0,
                            max=1,
                            step=0.05,
                            value=None,
                            updatemode="drag",
                            marks={0: "0%", 1: "100%"},
                        ),
                        html.P("Playback Rate:", style={"marginTop": "25px"}),
                        dcc.Slider(
                            id="slider-playback-rate",
                            min=0,
                            max=4,
                            step=None,
                            updatemode="drag",
                            marks={
                                i: str(i) + "x"
                                for i in [0, 0.25, 0.5, 0.75, 1, 2, 3, 4]
                            },
                            value=1,
                        ),
                        html.P(
                            "Update Interval for Current Time:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="slider-intervalCurrentTime",
                            min=40,
                            max=1000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [40, 100, 200, 500, 1000]},
                            value=100,
                        ),
                        html.P(
                            "Update Interval for Seconds Loaded:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="slider-intervalSecondsLoaded",
                            min=200,
                            max=2000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [200, 500, 750, 1000, 2000]},
                            value=500,
                        ),
                        html.P(
                            "Update Interval for Duration:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="slider-intervalDuration",
                            min=200,
                            max=2000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [200, 500, 750, 1000, 2000]},
                            value=500,
                        ),
                    ],
                ),
            ],
            style={
                "display": "flex",
                "flexDirection": "row",
                "justifyContent": "space-between",
            },
        ),
    ],
    style={"margin": "20px"},
)


@app.callback(
    Output("video-player", "url"),
    Output("input-url", "value"),
    Input("button-update-url", "n_clicks"),
    Input({"type": "url-btn", "value": ALL}, "n_clicks"),
    State("input-url", "value"),
    prevent_initial_call=True,
)
def update_url(n_clicks, url_n_clicks, value):
    if ctx.triggered_id == "button-update-url":
        return value, no_update
    return ctx.triggered_id["value"], ctx.triggered_id["value"]


@app.callback(Output("video-player", "playing"), Input("radio-bool-props", "value"))
def update_prop_playing(values):
    return "playing" in values


@app.callback(Output("video-player", "loop"), Input("radio-bool-props", "value"))
def update_prop_loop(values):
    return "loop" in values


@app.callback(Output("video-player", "controls"), Input("radio-bool-props", "value"))
def update_prop_controls(values):
    return "controls" in values


@app.callback(Output("video-player", "muted"), Input("radio-bool-props", "value"))
def update_prop_muted(values):
    return "muted" in values


@app.callback(Output("video-player", "volume"), Input("slider-volume", "value"))
def update_volume(value):
    return value


@app.callback(
    Output("video-player", "playbackRate"), Input("slider-playback-rate", "value")
)
def update_playbackRate(value):
    return value


# Instance Methods
@app.callback(
    Output("div-current-time", "children"), Input("video-player", "currentTime")
)
def update_time(currentTime):
    return f"Current Time: {currentTime}"


@app.callback(
    Output("div-seconds-loaded", "children"),
    Input("video-player", "secondsLoaded"),
)
def update_methods(secondsLoaded):
    return f"Second Loaded: {secondsLoaded}"


@app.callback(
    Output("div-duration", "children"),
    Input("video-player", "duration"),
)
def update_methods(duration):
    return f"Duration: {duration}"


@app.callback(
    Output("video-player", "intervalCurrentTime"),
    Input("slider-intervalCurrentTime", "value"),
)
def update_intervalCurrentTime(value):
    return value


@app.callback(
    Output("video-player", "intervalSecondsLoaded"),
    Input("slider-intervalSecondsLoaded", "value"),
)
def update_intervalSecondsLoaded(value):
    return value


@app.callback(
    Output("video-player", "intervalDuration"),
    Input("slider-intervalDuration", "value"),
)
def update_intervalDuration(value):
    return value


@app.callback(
    Output("video-player", "seekTo"),
    Input("seekto-btn", "n_clicks"),
    State("seekto-input", "value"),
)
def update_prop_seekTo(n_clicks, seekto):
    return seekto


if __name__ == "__main__":
    app.run(debug=True)
