import plotly.express as px
import pandas as pd

print("getting data.....")
df = px.data.carshare()

fig = px.scatter_map(df,lat='centroid_lat',lon='centroid_lon', color='peak_hour',size='car_hours',color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, title = 'Car Share Data', )
fig.update_layout(mapbox_style='open-street-map')
fig.show()
