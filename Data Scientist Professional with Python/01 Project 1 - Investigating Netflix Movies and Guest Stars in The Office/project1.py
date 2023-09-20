import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Pandas Frame Initialize
office_episodes = pd.read_csv('datasets/office_episodes.csv')

# Save relevant columns from dataframe into arrays for easy processing
episode_number = np.array(office_episodes['episode_number'])
viewerships = np.array(office_episodes['viewership_mil'])
scaled_ratings = np.array(office_episodes['scaled_ratings'])

# Create an array with correct coloring based on the scaled rating for each episode
col =  np.empty([len(episode_number)], dtype=object)
col[scaled_ratings < 0.25] = "red"
col[np.logical_and(scaled_ratings >=0.25, scaled_ratings < 0.5)] = "orange"
col[np.logical_and(scaled_ratings >=0.5, scaled_ratings < 0.75)] = "lightgreen"
col[scaled_ratings >= 0.75] = "darkgreen"

# Configure scatterplot and show
plt.scatter(episode_number, viewerships, c=col)
plt.show()