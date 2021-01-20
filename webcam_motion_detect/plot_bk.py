from capture1 import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Startn"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Endn"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=500, width=500, title="Motion graph")
p.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[("Start","@Startn"),("End","@Endn")])
p.add_tools(hover)


q=p.quad(left="Start",right="End",bottom=0,top=1, color="green", source=cds)


output_file("fig1.html")
show(p)
