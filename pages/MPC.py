
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import json
import pandas as pd
from utils import Header, make_dash_table
import plotly.graph_objs as go
import re
import pathlib

#current working dir
# wd = str(pathlib.Path().absolute())

#load csv
# fileName = wd + "\\Data\\2020-11-21_MPCfinalResult.csv"
#github
fileName = "./Data/2020-11-21_MPCfinalResult.csv"
dfSentiment = pd.read_csv(fileName)

#sentiment graph
fig = px.line(dfSentiment.query("MPCDate<='2020-03-31'").sort_values("MPCDate"), 
                x = "MPCDate", y = "SentimentScore",
                hover_name = "MPCDate", hover_data = {"MPCDate":False})
fig.update_layout(title = 'Net Sentiment Score of MPC Press Statements',
                   xaxis_title = 'Date(Month Year)',
                   yaxis_title = 'Net Sentiment Score',
                     height = 500, width = 750,)
fig.update_traces(mode='markers+lines')

#caption
caption1 = "2016 June - 2018 March (Gov Before GE14)"
caption2 = "2018 June - 2020 March (Gov After GE14)"

#title
title1 = "Frequently Mentioned Words in MPC Press Statements"
title2 = "Sentiment Score of MPC Press Statements"

#wc explaination
explanation1 = "The top 10 most frequently used words in MPC statements before and after GE after quite similar, with growth being used the most frequently in both periods. Terms like banking, strengthen, and faster were used exclusively in statements prior to GE while terms like pressures, household, and slower appeared exclusively in statements post GE"
explanation2 = "Statements published between July 2016 and March 2020 were downloaded and converted into a data processing friendly format using OCR. After some text pre-processing, the data are divided into two sets, i.e. before and after 9 May 2018. Sentiment analysis is performed on each statement using VADER library in Python resulting in a net sentiment score for each statement. The net sentiment of MP statements are relatively more negative post GE14."

#top frequent words
# fileName = wd + "\\Data\\top10words.csv"
#github
fileName = "./Data/top10words.csv"
df = pd.read_csv(fileName)

figWord = go.Figure()
x1 = [-i for i in df['Freq_Before']]
x1Label = [i for i in df['Freq_Before']]
y1 = [i for i in df['Word_Before']]
x2 = [i for i in df['Freq_After']]
y2 = [i for i in df['Word_After']]

#bar before ge14
figWord.add_trace(go.Bar(
    y = y1,
    x = x1,
    name = 'Before GE14',
    orientation = 'h',
    text = ["%s:%s"%(y1[no], str(i)) for no, i in enumerate(x1Label)],
    hoverinfo = 'text',
    textposition='auto',
    marker = dict(
        color = 'rgba(246, 78, 139, 0.6)',
        line = dict(color='rgba(246, 78, 139, 1.0)', width = 2)
    )
            ))

#bar after ge14
figWord.add_trace(go.Bar(
    y = y2,
    x = x2,
    name = 'After GE14',
    orientation = 'h',
    text = ["%s:%s"%(y2[no], str(i)) for no, i in enumerate(x2)],
    hoverinfo = 'text',
    textposition='auto',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width = 2)
    )
            ))

figWord.update_yaxes(visible = False, showticklabels=False)
figWord.update_xaxes(visible = True, showticklabels=False)
figWord.update_layout(barmode='relative', #title = 'Top 10 Most Frequently Used Words in MPC in 2 Different Periods',
                   xaxis_title = 'Frequency',plot_bgcolor='#fff',height = 500, width = 750,)

def create_layout(app):
    return html.Div([Header(app),
                    html.Div([
                                html.Div(
                                    [
                                        html.Br([]),
                                        #title1 - word cloud 
                                        html.Div(
                                            [html.H6(["%s"%title1], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                                ),
                                        #wordcloud
                                        html.Div([
                                                html.Iframe(src = app.get_asset_url("BeforeGE.html"),
                                                            className = "six columns",
                                                            style = {"height": "400px", "width": "50%"}),
                                                html.Iframe(src = app.get_asset_url("AfterGE.html"),
                                                            className = "six columns",
                                                            style = {"height": "400px", "width": "50%"}),
                                                html.Br([]),
                                                html.Div([html.Br(),
                                                html.P("Figure 1: Word Cloud for MPC Statements before (left) and after (right) GE14")],
                                                        style={'textAlign': 'center','fontSize': 12, 'font-style':'italic'}),
                                                html.Div([dcc.Graph(figure = figWord),
                                                html.P("Figure 2: Top 10 Most Frequently Used Words in MPC(left-Before GE;right-After GE)",
                                                style={'textAlign': 'center','fontSize': 12,'font-style':'italic',})],
                                                    className = "twelve columns",
                                                    style = {"padding-top": "0px",
                                                            "padding-left": "0px"},),
                                                  ],
                                                    className = "row"),
                                            #word cloud explaination
                                            html.Div([
                                                html.Br(),
                                                html.Strong(
                                                            "%s"%explanation1
                                                            ),
                                                html.Br(),
                                                # html.Br(),
                                                html.Br()]
                                            ,className = "twelve columns middle-aligned"
                                            ,style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#CAFAFE'
                                                  }),
                                    ],
                                    className = "rows"),
                            html.Div(
                                    [
                                        html.Br(),
                                        #title1 - sentiment score
                                        html.Div(
                                            [html.Br(),
                                            html.Br(),
                                            html.H6(["%s"%title2], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                                ),
                                         #graph
                                        html.Div([
                                            html.Iframe(src = app.get_asset_url("MPCSentiment2.html"),
                                                            className = "six columns",
                                                            style = {"height": "500px", "width": "100%"}),
                                            html.P("Figure 3: Net Sentiment Score of MPC Press Statements",
                                            style={'textAlign': 'center','fontSize': 12,'font-style':'italic'}),                                                            
                                                html.Br(),
                                                html.Div([
                                                    html.Br(),
                                                    html.Strong("%s"%explanation2), 
                                                    html.Br(),
                                                    html.Br()],style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#CAFAFE'})
                                                  ],
                                            className = "row"),
                                    ],
                                    className = "rows"),
                             ],
                         className = "sub_page",
                             )
                    ],
                    className = "page",
                   )
