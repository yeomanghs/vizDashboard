import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Br(),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5(html.B("Are We Better Off Post GE14?"))],
                        className = "twelve columns main-title",
                        style={'textAlign': 'center',
                        'color': '#374785',},
                    ),
                ],
                className = "twelve columns",
                style = {"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                html.B("Overview"),
                href = "/bnmReport/overview",
                className = "tab first",
                style={'color':'#24305E'},
            ),
            dcc.Link(
                html.B("MPC"),
                href = "/bnmReport/MPC",
                className = "tab",
                style={'color':'#24305E'},
            ),
            dcc.Link(
                html.B("Wages"),
                href = "/bnmReport/Wage",
                className = "tab",
                style={'color':'#24305E'},
            ),
            dcc.Link(
                html.B("Income Distribution"),
                href = "/bnmReport/IncEquality",
                className = "tab",
                style={'color':'#24305E'},
            ),
            dcc.Link(
                html.B("Conclusion"), 
                href="/bnmReport/conclusion", 
                className="tab",
                style={'color':'#24305E'},
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
