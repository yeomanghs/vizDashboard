
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import json
import pandas as pd
from utils import Header, make_dash_table
import plotly.graph_objs as go
import pathlib

#current working dir
# wd = str(pathlib.Path().absolute())

#load data
# jsonFile = wd + "\\Data\\states.geojson"
#github
jsonFile = './Data/states.geojson'
# jsonFile = "D:\\Users\\figohjs\\Documents\\Story\\Data\\states.geojson"
with open(jsonFile) as myJson:
    statesInfo = json.load(myJson)
jsonStateList = [i['properties']['Name'] for i in statesInfo['features']]

# fileName = wd + "\\Data\\GiniChange.csv"
#github
fileName = './Data/GiniChange.csv'
# fileName = "D:\\Users\\figohjs\\Documents\\Story\\Data\\GiniChange.csv"
dfGini = pd.read_csv(fileName)

#choropleth - b4 GE - urban
dfGinib4GE = dfGini.query('typeGov == "before"')
minVal = round(dfGinib4GE['urbanChange'].min(),4)
maxVal = round(dfGinib4GE['urbanChange'].max(),4)
fig = px.choropleth(dfGinib4GE, geojson = statesInfo, locations = 'state', color = 'urbanChange',
                           color_continuous_scale = "Reds",
                           range_color = (minVal, maxVal),
                           featureidkey="properties.Name",
                           labels={'urbanChange':'Improvement'},
                    )
fig.update_geos(fitbounds = "locations", visible = False)
fig.update_layout(
    height = 300, width = 350, margin={"r":0,"t":0,"l":0,"b":0},
    annotations = [dict(
    x = 0.55,
    y = 0.1,
    xref = 'paper',
    yref = 'paper',
    text = 'Urban - Before GE14 from 2014-2016',
    showarrow = False
    )]
)


#choropleth - after GE - urban
dfGiniafGE = dfGini.query('typeGov == "after"')
minVal = round(dfGinib4GE['urbanChange'].min(),4)
maxVal = round(dfGinib4GE['urbanChange'].max(),4)
# minVal = round(dfGiniafGE['urbanChange'].min(),4)
# maxVal = round(dfGiniafGE['urbanChange'].max(),4)
fig2 = px.choropleth(dfGiniafGE, geojson = statesInfo, locations = 'state', color = 'urbanChange',
                           color_continuous_scale = "Reds",
                           range_color=(minVal, maxVal),
                           featureidkey="properties.Name",
                           labels={'urbanChange':'Improvement'},
                    )
fig2.update_geos(fitbounds = "locations", visible = False)
fig2.update_layout(
    height = 300, width = 350, margin={"r":0,"t":0,"l":0,"b":0},
    annotations = [dict(
    x = 0.55,
    y = 0.1,
    xref = 'paper',
    yref = 'paper',
    text = 'Urban - After GE14 from 2016-2019',
    showarrow = False
    )]
)

#choropleth - b4 GE - rural
dfGinib4GE = dfGini.query('typeGov == "before"')
minVal = round(dfGinib4GE['ruralChange'].min(),4)
maxVal = round(dfGinib4GE['ruralChange'].max(),4)
fig3 = px.choropleth(dfGinib4GE, geojson = statesInfo, locations = 'state', color = 'ruralChange',
                           color_continuous_scale = "Reds",
                           range_color = (minVal, maxVal),
                           featureidkey="properties.Name",
                           labels={'ruralChange':'Improvement'},
                    )
fig3.update_geos(fitbounds = "locations", visible = False)
fig3.update_layout(
    height = 300, width = 350, margin={"r":0,"t":0,"l":0,"b":0},
    annotations = [dict(
    x = 0.55,
    y = 0.1,
    xref = 'paper',
    yref = 'paper',
    text = 'Rural - Before GE14 from 2014-2016',
    showarrow = False
    )]
)

#choropleth - after GE - rural
dfGiniafGE = dfGini.query('typeGov == "after"')
minVal = round(dfGinib4GE['ruralChange'].min(),4)
maxVal = round(dfGinib4GE['ruralChange'].max(),4)
# minVal = round(dfGiniafGE['urbanChange'].min(),4)
# maxVal = round(dfGiniafGE['urbanChange'].max(),4)
fig4 = px.choropleth(dfGiniafGE, geojson = statesInfo, locations = 'state', color = 'ruralChange',
                           color_continuous_scale = "Reds",
                           range_color=(minVal, maxVal),
                           featureidkey="properties.Name",
                           labels={'ruralChange':'Improvement'},
                    )
fig4.update_geos(fitbounds = "locations", visible = False)
fig4.update_layout(
    height = 300, width = 350, margin={"r":0,"t":0,"l":0,"b":0},
    annotations = [dict(
    x = 0.55,
    y = 0.1,
    xref = 'paper',
    yref = 'paper',
    text = 'Rural - After GE14 from 2016-2019',
    showarrow = False
    )]
)

#total improvement score
totalb4GE = dfGinib4GE['ruralChange'].sum() + dfGinib4GE['urbanChange'].sum()
totalafGE = dfGiniafGE['ruralChange'].sum() + dfGiniafGE['urbanChange'].sum()

#title
title1 = "Income Distribution in Urban Area (Gini Coefficient)"
title2 = "Income Distribution in Rural Area (Gini Coefficient)"
title3 = "Overall Comparison"

#explaination
explanation1 = "Definition: Improvement = 0.1 when Gini Coefficient reduces from 0.3 (more income inequality) to 0.2 (less income inequality)"\
                " in urban area"
explanation2 = "Defintion: Improvement = 0.1 when Gini Coefficient reduces from 0.3 (more income inequality) to 0.2 (less income inequality)"\
                " in rural area"

#conclusion
conclusion1 = "For urban area, Gov before GE14 did a better job in Peninsular Malaysia as represented in darker shades of red especially in states like Pahang,"\
              "Terengganu and Kelantan (0.01 - 0.03) whereas Gov after GE14 has improved inequality in state of Sabah (0.01)"
conclusion2 = "For rural area, both Gov did equally good job across states. However, Gov before GE14 "\
               "noticeably has not improved states as represented in lighter shades of red like Johor and Kedah (around -0.05)"
conclusion3 = "On an aggregated level, income equality of the country worsen under both Gov. As a comparison, Gov after GE14 "\
                "did a slightly better job (-0.062) compared to previous Gov (-0.125)"

def create_layout(app):
    return html.Div([Header(app),
                    html.Div([
                                #title1
                                html.Div(
                                    [
                                        html.Br([]),
                                        html.Div(
                                            [html.H6(["%s"%title1], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                                ),
                                        html.Div(
                                        [html.Strong(
                                                    "%s"%explanation1
                                                    )]
                                            ,className="twelve columns",style={'font-style':'italic'}
                                                )
                                        ],
                                    className="rows",
                                        ),
                                #choropleth - urban
                                    html.Div([
                                            html.Div([dcc.Graph(figure = fig)]
                                                    ,className = "six columns"),
                                            html.Div([dcc.Graph(figure = fig2)], 
                                                    className = "six columns"),
                                            html.P("Figure 5: Improvement of Gini Coefficient in Urban Area",
                                            style={'textAlign': 'center','fontSize': 12,'font-style':'italic'}),
                                            html.Br(),
                                                html.Div([
                                                    html.Br(),
                                                    html.Strong("%s"%conclusion1), 
                                                    html.Br(),
                                                    html.Br()],style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#EDC7B7'}),
                                            ],
                                            className = "row"),
                                    #title2
                                    html.Div(
                                    [
                                        html.Br([]),
                                        html.Div(
                                            [
                                            html.Br(),
                                            html.H6(["%s"%title2], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                        ),
                                        html.Div(
                                            [html.Strong(
                                                        "%s"%explanation2
                                                        )]
                                                ,className="twelve columns",style={'font-style':'italic'}
                                                )
                                    ],
                                    className="rows",
                                        ),
                                #choropleth - rural
                                    html.Div([
                                            html.Div([dcc.Graph(figure = fig3)]
                                                    ,className = "six columns"),
                                            html.Div([dcc.Graph(figure = fig4)], 
                                                    className = "six columns"),
                                            html.P("Figure 6: Improvement of Gini Coefficient in Rural Area",
                                            style={'textAlign': 'center','fontSize': 12,'font-style':'italic'}),
                                            html.Br(),
                                                html.Div([
                                                    html.Br(),
                                                    html.Strong("%s"%conclusion2), 
                                                    html.Br(),
                                                    html.Br()],style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#EDC7B7'}),
                                            ],
                                            className = "row"),
                                    #title3
                                    html.Div(
                                        [
                                            html.Br([]),
                                            html.Div(
                                                [
                                                html.Br(),
                                                html.Br(),
                                                html.H6(["%s"%title3], 
                                                className="subtitle padded"),
                                                ],
                                                className="twelve columns",
                                                    ),
                                        ],
                                        className="rows",
                                            ),
                                    #bar chart
                                        html.Div(
                                            [
                                            html.Strong(
                                                "Total Improvement Score - Urban vs Rural",
                                                style={"color": "#3a3a3a",'font-style':'italic'},
                                                        ),
                                            dcc.Graph(
                                                id="graph-6",
                                                figure={
                                                            "data": [
                                                                go.Bar(
                                                                    x=["Before GE14", "After GE14"],
                                                                    y=[str(totalb4GE), str(totalafGE)],
                                                                    marker={"color": "#F76C6C"},
                                                                    name="A",
                                                                ),
                                                                    ],
                                                        }
                                                    ),
                                            html.Div([
                                                html.Br(),
                                                html.Strong("%s"%conclusion3),
                                                html.Br(),
                                                html.Br(),
                                                    ],
                                                style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#EDC7B7'})
                                            ],
                                             className = "row" )
                                    ],
                            className = "sub_page")
                    ],
                    className = "page",
                   )
