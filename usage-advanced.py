from textwrap import dedent

import dash_player
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(style={'width': '40%', 'float': 'left'}, children=[
        dash_player.PlayerComponent(
            id='video-player',
            url='http://media.w3.org/2010/05/bunny/movie.mp4',
            controls=True
        ),
        dcc.Markdown(dedent('''
        ### Video Examples
        * mp4: http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4
        * mp3: https://storage.googleapis.com/media-session/elephants-dream/the-wires.mp3
        * webm: http://clips.vorwaerts-gmbh.de/big_buck_bunny.webm
        * ogv: http://clips.vorwaerts-gmbh.de/big_buck_bunny.ogv
        * Youtube: https://www.youtube.com/watch?v=sea2K4AuPOk
        '''))
    ]),

    html.Div(style={'width': '40%', 'float': 'left'}, children=[
        dcc.Input(
            id='input-url',
            value='http://media.w3.org/2010/05/bunny/movie.mp4'
        ),

        html.Button('Change URL', id='button-update-url'),

        dcc.Checklist(
            id='radio-bool-props',
            options=[{'label': val.capitalize(), 'value': val} for val in [
                'playing',
                'loop',
                'controls',
                'muted'
            ]],
            values=['controls']
        ),

        html.P("Volume:", style={'margin-top': '10px'}),
        dcc.Slider(
            id='slider-volume',
            min=0,
            max=1,
            step=0.1,
            value=None,
            marks={0: '0%', 1: '100%'}
        ),

        html.P("Playback Rate:", style={'margin-top': '25px'}),
        dcc.Slider(
            id='slider-playback-rate',
            min=0,
            max=4,
            step=None,
            marks={i: str(i)+'x' for i in [0, 0.25, 0.5, 0.75, 1, 2, 3, 4]},
            value=1
        )
    ]),
])


@app.callback(Output('video-player', 'playing'),
              [Input('radio-bool-props', 'values')])
def update_prop_playing(values):
    return 'playing' in values


@app.callback(Output('video-player', 'loop'),
              [Input('radio-bool-props', 'values')])
def update_prop_loop(values):
    return 'loop' in values


@app.callback(Output('video-player', 'controls'),
              [Input('radio-bool-props', 'values')])
def update_prop_controls(values):
    return 'controls' in values


@app.callback(Output('video-player', 'muted'),
              [Input('radio-bool-props', 'values')])
def update_prop_muted(values):
    return 'muted' in values


@app.callback(Output('video-player', 'volume'),
              [Input('slider-volume', 'value')])
def update_volume(value):
    return value


@app.callback(Output('video-player', 'playbackRate'),
              [Input('slider-playback-rate', 'value')])
def update_playbackRate(value):
    return value


@app.callback(Output('video-player', 'url'),
              [Input('button-update-url', 'n_clicks')],
              [State('input-url', 'value')])
def update_url(n_clicks, value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
