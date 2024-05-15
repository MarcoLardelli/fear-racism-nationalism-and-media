import plotly.express as px
import pandas as pd
from random import random,seed
import numpy as np


NO_OF_EVENTS = 100
NO_OF_SAMPLES = 10
NEGATIVE_FRACTION = 0.07 

# -----------

seed(3)

events = []
for i in range(NO_OF_EVENTS):
    is_bad = 1 if random()<NEGATIVE_FRACTION else 0.2
    impact_score = is_bad
    x = random()
    y = random()
    events.append([x,y,is_bad,impact_score])

events_np = np.array(events)

# plot the ground truth

x_range = [-0.1,1.05*max(events_np[:, 0])]
y_range = [-0.1,1.05*max(events_np[:, 1])]

fig = px.scatter(x=events_np[:, 0], y=events_np[:, 1], color=events_np[:, 2], size=events_np[:, 3], color_continuous_scale=['green','red'])
fig.update_layout(
    title="Events (ground truth)",
    xaxis_title="W to E",
    yaxis_title="S to N",
    plot_bgcolor= 'rgba(200, 255, 200, 255)',  # helper to create "model" chart by hand
)
fig.update_xaxes(range=x_range)
fig.update_yaxes(range=y_range)
fig.write_image("ground_truth_model.png") 
fig.show()

# now sample with high impact_score preference

sorted_events = sorted(events, key=lambda x: x[3], reverse=True)
sample = sorted_events[0:NO_OF_SAMPLES]
sample_np = np.array(sample)

# plot samples

fig = px.scatter(x=sample_np[:, 0], y=sample_np[:, 1], color=sample_np[:, 2], size=sample_np[:, 3], color_continuous_scale=['green','red'])
fig.update_layout(
    title="Sampled events",
    xaxis_title="W to E",
    yaxis_title="S to N",
    plot_bgcolor= 'rgba(255, 200, 200, 255)',
)
fig.update_xaxes(range=x_range)
fig.update_yaxes(range=y_range)
fig.write_image("sampled_model.png") 
fig.show()