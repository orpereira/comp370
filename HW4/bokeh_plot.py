from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
import pandas as pd

# Load the preprocessed data
data = pd.read_csv('/home/ubuntu/comp370/data/nyc_311_limit.csv')

# Extract the list of unique zipcodes
zipcodes = sorted(data['Incident Zip'].unique())

# Data source for the plot
source_all = ColumnDataSource(data={
    'month': data['Month'].unique(),
    'response_time': data.groupby('Month')['Response Time (hours)'].mean().values
})

source_zip1 = ColumnDataSource(data={'month': [], 'response_time': []})
source_zip2 = ColumnDataSource(data={'month': [], 'response_time': []})

# Create the figure
p = figure(title="Monthly Average Incident Response Time (2020)", 
           x_axis_label="Month", 
           y_axis_label="Response Time (hours)", 
           plot_width=800, 
           plot_height=400)

# Add lines for the overall response time and for both zipcodes
line_all = p.line(x='month', y='response_time', source=source_all, line_width=2, color='blue', legend_label='All 2020')
line_zip1 = p.line(x='month', y='response_time', source=source_zip1, line_width=2, color='green', legend_label='Zipcode 1')
line_zip2 = p.line(x='month', y='response_time', source=source_zip2, line_width=2, color='red', legend_label='Zipcode 2')

p.legend.location = "top_left"

# Dropdown widgets for selecting zipcodes
select_zip1 = Select(title="Select Zipcode 1", value=str(zipcodes[0]), options=[str(z) for z in zipcodes])
select_zip2 = Select(title="Select Zipcode 2", value=str(zipcodes[1]), options=[str(z) for z in zipcodes])

# Update function for the zipcodes
def update_zipcode(attr, old, new):
    # Update data for zipcode 1
    zip1_data = data[data['Incident Zip'] == int(select_zip1.value)]
    source_zip1.data = {
        'month': zip1_data['Month'],
        'response_time': zip1_data['Response Time (hours)']
    }
    
    # Update data for zipcode 2
    zip2_data = data[data['Incident Zip'] == int(select_zip2.value)]
    source_zip2.data = {
        'month': zip2_data['Month'],
        'response_time': zip2_data['Response Time (hours)']
    }

# Attach the update function to the dropdowns
select_zip1.on_change('value', update_zipcode)
select_zip2.on_change('value', update_zipcode)

# Initial update (to populate with the initial selections)
update_zipcode(None, None, None)

# Layout the widgets and the plot in a column
layout = column(select_zip1, select_zip2, p)

# Add the layout to the current document (curdoc) for the Bokeh server
curdoc().add_root(layout)
curdoc().title = "NYC 311 Response Time Dashboard"
