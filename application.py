import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title='Dash on AWS EB!'
########### Set up the layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
            This is Dash running on Elastic Beanstalk.
        '''),
    
])
########### Run the app
if __name__ == '__main__':
    app.run(debug=False, port=3000)