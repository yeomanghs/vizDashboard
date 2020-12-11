
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd

#title
titleTable = "Summary"
titleSection1 = "Data Sources"
titleSection2 = "Limitation Acknowledgement"

df = pd.DataFrame({'Col 1': ['Area', 'MPC', 'Wage', 'Income Equality'],
                   'Col 2': ['Before GE14', "Better", "Better", "Worse"], 
                   'Col 3': ['Post GE14', 'Worse', "Worse", "Better"]})
#table desc
tableDesc = "Based on MPC sentiment and wages increment (using national average), we are relatively worse off post GE14. However, based on income distribution, we are better off post GE14."

#links
MPClink = "https://www.bnm.gov.my/index.php?tpl=2016_pr_search_result&ch=en_press&pg=en_press&query_txt=monetary+policy+statement"
Incomelink = "https://newss.statistics.gov.my/newss-portalx/ep/epProductFreeDownloadSearch.seam"
WageLink = "https://www.dosm.gov.my/v1/index.php?r=column/cthemeByCat&cat=157&bul_id=VXRJbkFUNUp5eDl0UFBFRG5CMWlMUT09&menu_id=Tm8zcnRjdVRNWWlpWjRlbmtlaDk1UT09"

#section 2 (limitation acknowledgement) - points
S2point1 =  "Data used only captures snapshots of the indicators (instead of a time series data)"
S2point2 = "Unable to find sufficient data on other aspects like healthcare and crime rate to perform a more holistic comparison study"\


def create_layout(app):
    # Page layouts
    return html.Div(
            [
                html.Div([Header(app)]),
                # page 4
                html.Div(
                    [ 
                    html.Div([
                            html.Div(
                                [
                                #summary section
                                html.Div(
                                    [
                                        html.H6(["%s"%titleTable], className="subtitle padded"),
                                        html.Table(make_dash_table(df),style={'width' : '70%' }),
                                        html.P("%s"%tableDesc),
                                    ],
                                    className="ten columns",
                                        ),
                                ],
                                className = "row",
                                    ),
                                #second section - Data and Source
                                html.Div(
                                    [
                                        html.H6("%s"%titleSection1, className="subtitle padded"),
                                        html.Br([]),
                                        html.Div(
                                            [
                                                html.P(html.Label(['Monetary Policy Statements - ', html.A('Link to source', href = MPClink)])),
                                                html.P(html.Label(['Salaries & Wages Survey Reports - ', html.A('Link to source', href = WageLink)])),
                                                html.P(html.Label(['Household Income & Basic Amenities Survey Reports - ', html.A('Link to source', href = Incomelink)])),
                                            ],
#                                             id="reviews-bullet-pts",
                                            className = "twelve columns"
                                        ),
                                    ],
                                    className = "row",
                                        ),
                        
                                #third section - Limitation acknowledgement
                                html.Div(
                                    [
                                        html.H6("%s"%titleSection2, className="subtitle padded"),
                                        html.Br([]),
                                        html.Div(
                                            [
                                                html.Li("%s"%S2point1,style={'margin-left': '20px'}),
                                                html.Li("%s"%S2point2,style={'margin-left': '20px'}),
                                            ],
                                            id="reviews-bullet-pts",
                                        ),
                                    ],
                                    className = "row",
                                        ),
                            ],
                            className = "rows",
                            )
                    ],
                    className="sub_page",
                    ),
            ],
            className="page",
                    )
