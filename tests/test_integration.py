import dash
from dash import html, Input, Output, State
from dash_player import DashPlayer


def test_001_child_with_0(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div(id="nully-wrapper", children=0)
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)

    assert dash_duo.find_element("#nully-wrapper").text == "0"
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("test_001_child_with_0-layout")


def test_002_dash_player_exists_with_size(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div(
        children=[
            DashPlayer(
                id="video-player",
                url="https://media.w3.org/2010/05/bunny/movie.ogv",
                playing=True,
                controls=True,
                width="640px",
                height="360px",
            )
        ]
    )
    dash_duo.start_server(app)
    assert (
        dash_duo.find_element("#video-player").get_attribute("style")
        == "width: 640px; height: 360px;"
    )
    assert (
        dash_duo.find_element("#video-player > video").get_attribute("src")
        == "https://media.w3.org/2010/05/bunny/movie.ogv"
    )
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("test_002_dash_player_exists-layout")


def test_003_styling(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div(
        children=[
            DashPlayer(
                id="video-player",
                url="https://media.w3.org/2010/05/bunny/movie.ogv",
                playing=True,
                controls=True,
                style={"border": "5px solid red", "border-radius": "10px"},
            )
        ]
    )
    dash_duo.start_server(app)
    assert (
        dash_duo.find_element("#video-player").get_attribute("style")
        == "border: 5px solid red; border-radius: 10px; width: 640px; height: 360px;"
    )
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("test_002_dash_player_exists-layout")


def test_003_toggle_properties_via_callback(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div(
        children=[
            DashPlayer(
                id="video-player",
                url="https://media.w3.org/2010/05/bunny/movie.ogv",
            ),
            html.Button(id="playing-btn"),
            html.Div(id="playing-div"),
            html.Button(id="loop-btn"),
            html.Div(id="loop-div"),
            html.Button(id="controls-btn"),
            html.Div(id="controls-div"),
            html.Button(id="muted-btn"),
            html.Div(id="muted-div"),
        ]
    )

    @app.callback(
        Output("video-player", "playing"),
        Input("playing-btn", "n_clicks"),
        State("video-player", "playing"),
        prevent_initial_call=True,
    )
    def update_playing(n_clicks, playing):
        return not playing

    @app.callback(
        Output("video-player", "loop"),
        Input("loop-btn", "n_clicks"),
        State("video-player", "loop"),
        prevent_initial_call=True,
    )
    def update_loop(n_clicks, loop):
        return not loop

    @app.callback(
        Output("video-player", "controls"),
        Input("controls-btn", "n_clicks"),
        State("video-player", "controls"),
        prevent_initial_call=True,
    )
    def update_controls(n_clicks, controls):
        return not controls

    @app.callback(
        Output("video-player", "muted"),
        Input("muted-btn", "n_clicks"),
        State("video-player", "muted"),
        prevent_initial_call=True,
    )
    def update_muted(n_clicks, muted):
        return not muted

    @app.callback(
        Output("playing-div", "children"),
        Output("loop-div", "children"),
        Output("controls-div", "children"),
        Output("muted-div", "children"),
        Input("video-player", "playing"),
        Input("video-player", "loop"),
        Input("video-player", "controls"),
        Input("video-player", "muted"),
    )
    def output_properties(playing, loop, controls, muted):
        return f"{playing}", f"{loop}", f"{controls}", f"{muted}"

    dash_duo.start_server(app)

    playing_btn = dash_duo.find_element("#playing-btn")
    loop_btn = dash_duo.find_element("#loop-btn")
    controls_btn = dash_duo.find_element("#controls-btn")
    muted_btn = dash_duo.find_element("#muted-btn")

    playing_btn.click()
    dash_duo.wait_for_text_to_equal("#playing-div", "True", timeout=10)
    assert dash_duo.find_element("#playing-div").text == "True"

    loop_btn.click()
    dash_duo.wait_for_text_to_equal("#loop-div", "True", timeout=10)
    assert dash_duo.find_element("#loop-div").text == "True"

    controls_btn.click()
    dash_duo.wait_for_text_to_equal("#controls-div", "True", timeout=10)
    assert dash_duo.find_element("#controls-div").text == "True"

    muted_btn.click()
    dash_duo.wait_for_text_to_equal("#muted-div", "True", timeout=10)
    assert dash_duo.find_element("#muted-div").text == "True"

    dash_duo.percy_snapshot("test_003_toggle_properties_via_callback-layout")
