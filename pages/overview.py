
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd

#title
titleBox = "Interest Area:"
#desc
descBox = "To evaluate the performance of the government two (2) years before and after GE14 "\
        "using monetary policy statements, salaries & wages survey reports, and household income"\
        "& basic amenities survey reports as indicators."

#first section
#title
titleSection1 = "1) Monetary Policy Statements"
#desc
S1desc1 = "MPC Statements released between July 2016 and March 2020"
# S1desc2 = "Second sentence"

#second section
titleSection2 = "Area of Analysis"
#desc in point form
point1 = "1) Monetary Policy"
point2 = "2) Wages"
point3 = "3) Income Distribution"

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    
                    html.Div(
                        [
                            # highlighted box
                            html.Div(
                                [
                                    html.H5("%s"%titleBox),
                                    html.Br([]),
                                    html.P(
                                        "%s"%descBox,
                                        style = {"color": "#fff",'fontSize':11},
                                        className = "row",
                                            ),
                                ],
                                className = "product",
                                     ),
                            html.Div(
                                [
                                    html.H6(html.Strong("%s"%titleSection2), className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            dcc.Link("%s"%point1, href='/bnmReport/MPC'),
                                            html.Br(),
                                            html.Br(),
                                            html.Li("Word Frequency",style={'margin-left': '40px'}),
                                            html.Li("Sentiment",style={'margin-left': '40px'}),
                                            dcc.Link("%s"%point2,href='/bnmReport/Wage'),
                                            html.Br(),
                                            html.Br(),
                                            html.Li("Comparison on Wage Increment",style={'margin-left': '40px'}),
                                            dcc.Link("%s"%point3,href="/bnmReport/IncEquality"),
                                            html.Br(),
                                            html.Br(),
                                            html.Li("Comparison on Income Distribution using Gini Coefficient",style={'margin-left': '40px'}),
                                        ],
                                        id="reviews-bullet-pts"
                                    ),
                                ],
                                className = "row",
                                    ),
                         ],
                    className = "rows"),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
