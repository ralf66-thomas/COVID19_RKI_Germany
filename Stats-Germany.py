#
# Create Coroa stats using Pandas
#

import pandas as pd
import plotly.graph_objects as go

fn_rki = "./RKI_Covid19_ALL.csv"

#
# Loading Data and generate Graphs
#

data_germany = pd.read_csv(fn_rki)

landes_list = data_germany.groupby("Bundesland").count()

fig1 = go.Figure(layout_title_text="Anzahl Infektionen")
fig2 = go.Figure(layout_title_text="Anzahl Infektionen pro 100.000 Einwohnern")
fig3 = go.Figure(layout_title_text="Anzahl Todesfälle")

for land in landes_list.index:
    data_plot = data_germany[data_germany["Bundesland"] == land]
    fig1.add_trace(go.Scatter(
        x=data_plot["Date"], y=data_plot["Anzahl"], name=land, line=dict(width=4)))
    fig2.add_trace(go.Scatter(
        x=data_plot["Date"], y=data_plot["Fälle/100.000 Einw."], name=land, line=dict(width=4)))
    fig3.add_trace(go.Scatter(
        x=data_plot["Date"], y=data_plot["Todesfälle"], name=land, line=dict(width=4)))
fig1.show()
fig2.show()
fig3.show()

date_list = data_germany.groupby("Date").count()
data_today = data_germany[data_germany["Date"] ==
                          date_list.index[-1]].sort_values(by=["Fälle/100.000 Einw."])
data_7days = data_germany[data_germany["Date"] == date_list.index[-8]]
data_14days = data_germany[data_germany["Date"] == date_list.index[-15]]

fig4 = go.Figure([go.Bar(name="Infektionen Heute", x=data_today["Bundesland"],
                         y=data_today["Fälle/100.000 Einw."], marker_color='blue'),
                  go.Bar(name="Infektionen vor 7 Tagen", x=data_7days["Bundesland"],
                         y=data_7days["Fälle/100.000 Einw."], marker_color='cornflowerblue'),
                  go.Bar(name="Infektionen vor 14 Tagen", x=data_14days["Bundesland"],
                         y=data_14days["Fälle/100.000 Einw."], marker_color='lightblue')])
fig4.update(
    layout_title_text="Anzahl Infektionen pro 100.000 Einwohnern in zeitlichen Vergleich")
fig4.show()
