
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

#load data
# fileName = wd + '\\Data\\WageIncrement.csv'
#github
fileName = './Data/WageIncrement.csv'
dfWageIncrement = pd.read_csv(fileName)

# fileName = wd + "\\Data\\WageIncrementArea.csv"
#github
fileName = './Data/WageIncrementArea.csv'
dfWageIncrementArea = pd.read_csv(fileName)

#wrangle
#get year from column named variable
dfWageIncrement['Year'] = dfWageIncrement['variable'].map(lambda x:re.sub("Increment_", "", x))
#change jumlah to average in age column
dfWageIncrement['Age'] = dfWageIncrement['Age'].map(lambda x: 'Average' if x=='Jumlah' else x)
#rename column named value
dfWageIncrement.rename(columns = {'value':'Increment'}, inplace = True)

#get year from column named variable
dfWageIncrementArea['Year'] = dfWageIncrementArea['variable'].map(lambda x:re.sub("Increment_", "", x))
#rename values in column named Strata
dfWageIncrementArea['Strata'] = dfWageIncrementArea['Strata'].map(lambda x:"Urban" if x == "Bandar"
                                                                 else "Rural")
#rename column named value
dfWageIncrementArea.rename(columns = {'value':'Increment', 'Strata':'Area'}, inplace = True)
#del column
del dfWageIncrementArea['variable']

#title
title1 = "Wage Increment By Age Group"
title2 = "Wage Increment By Area"

#explaination
explanation1 = "Employees aged below 30 saw a decline in wages increment post GE14 while their counterparts aged 30 and above fared better and saw an increase in wages increment in the same period."
explanation2 = "Employees in the urban area saw a slower increase in wage increment relative to their counterparts in non-urban area post GE14. However, employees in the urban area still experienced higher increment relatively to their counterparts in rural area."

#line graph
#Wage Increment by Age group
fig = px.line(dfWageIncrement, x = "Year", y = "Increment", color = "Age",
                hover_name = "Year", hover_data = {"Year":False},
             color_discrete_sequence=px.colors.qualitative.Alphabet)
fig.update_xaxes(tickvals=["2016", "2017", "2018", "2019"])
fig.update_traces(mode='markers+lines')
fig.update_layout(title='Comparison of Wage Increment',
                   xaxis_title='Year',
                   yaxis_title='Increment (%)',
                 height = 500, width = 750)

#Wage Increment by Area
fig2 = px.line(dfWageIncrementArea, x = "Year", y = "Increment", color = "Area",
                hover_name = "Year", hover_data = {"Area":False, "Year":False},
             color_discrete_sequence=px.colors.qualitative.Alphabet)
fig2.update_xaxes(tickvals=["2016", "2017", "2018", "2019"])
fig2.update_traces(mode='markers+lines')
fig2.update_layout(title='Average Wage Increment Of Urban and Rural Employees',
                   xaxis_title='Year',
                   yaxis_title='Increment (%)',
                  height = 500, width = 750)

def create_layout(app):
    return html.Div([Header(app),
                     html.Div([
                                #title1 - wage increment by age group
                                html.Div(
                                    [
                                        html.Br([]),
                                        html.Div(
                                            [html.H6(["%s"%title1], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                                ),
                                        #graph
                                        html.Div([
                                            html.Iframe(src = app.get_asset_url("Wages_15to29.html"),
                                                            className = "six columns",
                                                            style = {"height": "400px", "width": "50%"}),
                                            html.Iframe(src = app.get_asset_url("Wages_30to59.html"),
                                                            className = "six columns",
                                                            style = {"height": "400px", "width": "50%"}),
                                            html.P("Figure 4: Wage Increment between 2016 and 2019",
                                            style={'textAlign': 'center','fontSize': 12,'font-style':'italic'})
                                                            
                                                  ],
                                            className = "row"),
                                        #graph explaination
                                        html.Div([
                                            html.Br(),
                                            html.Strong(
                                                        "%s"%explanation1
                                                        ),
                                            html.Br(),
                                            html.Br()]
                                        ,className = "twelve columns middle-aligned"
                                        ,style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#EDF5E1'}),
                                    ],
                                    className="rows",
                                        ), 
                            #title2 - wage increment by area types
                                html.Div(
                                    [
                                        html.Br([]),
                                        html.Div(
                                            [
                                            html.Br(),
                                            html.Br(),
                                            html.H6(["%s"%title2], 
                                            className="subtitle padded")],
                                            className="twelve columns",
                                                ),
                                        html.Div([
                                            html.Iframe(src = app.get_asset_url("Wages_UrbanRural.html"),
                                                            className = "six columns",
                                                            style = {"height": "400px", "width": "100%"}),
                                            html.P("Figure 4: Wage Increment of Urban and Rural Employees",
                                            style={'textAlign': 'center','fontSize': 12,'font-style':'italic'}),                                                            
                                                html.Br(),
                                                html.Div([
                                                    html.Br(),
                                                    html.Strong("%s"%explanation2), 
                                                    html.Br(),
                                                    html.Br()],style = {"color": "#374785",'fontSize': 13,
                                                  "padding-top": "0px", "border-style": "solid",'textAlign': 'center','background-color':'#EDF5E1'})
                                                  ],
                                            className = "row"),
                                    ],
                                    className="rows",
                                        ), 
                              ],
                         className = "sub_page",
                             )
                    ],
                    className = "page",
                   )
