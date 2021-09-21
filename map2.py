import plotly.express as px
import pandas as pd
#df=px.data.wind()
df = pd.read_csv("sensor.csv")

fig = px.scatter_polar(df, r="distance", theta="direction",
                       color='Oil_color',symbol="Location",
                       title="Sensor Data Visualization",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)

fig.show()
