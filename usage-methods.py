import dash_player
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash('')

app.scripts.config.serve_locally = True


app.layout = html.Div([
    dash_player.PlayerComponent(
        id='video-player',
        url='http://media.w3.org/2010/05/bunny/movie.mp4',
        controls=True
    ),

    html.Button('Set seekTo to 10', id='button-seek-to'),

    html.Div(id='div-current-time', style={'margin-bottom': '20px'}),

    html.Div(id='div-method-output')
])


@app.callback(Output('div-current-time', 'children'),
              [Input('video-player', 'currentTime')])
def update_time(currentTime):
    return 'Current Time: {}'.format(currentTime)


@app.callback(Output('div-method-output', 'children'),
              [Input('video-player', 'secondsLoaded')],
              [State('video-player', 'duration')])
def update_methods(secondsLoaded, duration):
    return 'Second Loaded: {}, Duration: {}'.format(secondsLoaded, duration)


@app.callback(Output('video-player', 'seekTo'),
              [Input('button-seek-to', 'n_clicks')])
def set_seekTo(n_clicks):
    return 10


if __name__ == '__main__':
    app.run_server(debug=True)
