# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:50:31 2023

@author: kyria
"""

"""
@author: Kyriakos Fotiou
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import pickle 
from scipy import stats
import seaborn as sns


### change later ### 
df1 = pd.read_csv('p104_final_oar_irr.csv')
df = pd.read_csv('p104_final_wepl.csv')
dz = pd.read_csv('p104_z_score_data.csv')

"""
Visualise Beam path
"""
# Generate Beam for couch angle 0 and gantry angle 45#
lines_coords,distance, lines = main(tumor , 0 ,45)
# Mask Beam and Tumour
tumor_masked = np.ma.masked_where(tumor == 0, tumor)
beam = np.ma.masked_where(lines == 0, lines)
# Plot CT scan and beam
plt.imshow(ref_ave_ct[45,:,:], cmap='gray')
plt.imshow(beam[45,::],alpha=0.6, interpolation = 'none', vmin = 0, cmap='Blues')
plt.imshow(tumor_masked[45,:,:],alpha=0.6, interpolation = 'none', vmin = 0, cmap='Reds')
plt.xticks([])
plt.yticks([])
plt.show()




"""
Plot Tumour ΔWEPL and OAR PIV maps 
"""
fig, ax = plt.subplots(1,4, figsize = (20,7), sharey = True, sharex = True)
ax[0].set_title('Heart Irradiation')
sns.heatmap(data=df1.pivot( "gantry_angle", "couch_angle","beam_heart") ,cmap="rainbow",ax=ax[0],  xticklabels = 3, yticklabels = 5)
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].tick_params(bottom=False, left=False)
cbar = ax[0].collections[0].colorbar
cbar.set_label("PIV [%]")
#fig = plt.figure('cord_z_score')
ax[1].set_title('Cord Irradiation')
sns.heatmap(data=df1.pivot( "gantry_angle", "couch_angle","beam_cord") ,cmap="rainbow", ax=ax[1],  xticklabels = 3, yticklabels = 5)
ax[1].set_ylabel('')
ax[1].set_xlabel('')
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].tick_params(bottom=False, left=False)
cbar = ax[1].collections[0].colorbar
cbar.set_label("PIV [%]")
#fig = plt.figure('lungs_z_score')
ax[2].set_title('Lungs Irradiation')
sns.heatmap(data=df1.pivot( "gantry_angle", "couch_angle","beam_lungs") ,cmap="rainbow", ax=ax[2],  xticklabels = 3, yticklabels = 5)
ax[2].set_ylabel('')
ax[2].set_xlabel('')
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['bottom'].set_visible(False)
ax[2].spines['left'].set_visible(False)
ax[2].tick_params(bottom=False, left=False)
cbar = ax[2].collections[0].colorbar
cbar.set_label("PIV [%]")
#fig = plt.figure('tumor_z_score')
ax[3].set_title('Tumor ΔWEPL')
sns.heatmap(data=df.pivot( "gantry_angle", "couch_angle","wepl") ,cmap="rainbow", ax=ax[3],  xticklabels = 3, yticklabels = 5)
ax[3].set_ylabel('')
ax[3].set_ylabel('')
ax[3].set_xlabel('')
ax[3].spines['top'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].spines['bottom'].set_visible(False)
ax[3].spines['left'].set_visible(False)
ax[3].tick_params(bottom=False, left=False)
cbar = ax[3].collections[0].colorbar
cbar.set_label("ΔWEPL [mm]")
### Axis Label Settings ###
fig.text(0.5,0.04, "Couch Angle [deg]", ha="center", va="center")
fig.text(0.05,0.5, "Gantry Angle [deg]", ha="center", va="center", rotation=90)
plt.show()


"""
Plot Tumour and OAR Z-Score Maps
"""
fig, ax = plt.subplots(1,4, figsize = (20,7), sharey = True, sharex = True)
ax[0].set_title('Heart Z-score')
sns.heatmap(data=dz.pivot( "gantry_angle", "couch_angle","heart_score") ,cmap="rainbow",ax=ax[0],  xticklabels = 3, yticklabels = 5)
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].tick_params(bottom=False, left=False)
cbar = ax[0].collections[0].colorbar
cbar.set_label("Z-score")
#fig = plt.figure('cord_z_score')
ax[1].set_title('Cord Z-score')
sns.heatmap(data=dz.pivot( "gantry_angle", "couch_angle","cord_score") ,cmap="rainbow", ax=ax[1],  xticklabels = 3, yticklabels = 5)
ax[1].set_ylabel('')
ax[1].set_xlabel('')
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].tick_params(bottom=False, left=False)
cbar = ax[1].collections[0].colorbar
cbar.set_label("Z-score")
#fig = plt.figure('lungs_z_score')
ax[2].set_title('Lungs Z-score')
sns.heatmap(data=dz.pivot( "gantry_angle", "couch_angle","lungs_score") ,cmap="rainbow", ax=ax[2],  xticklabels = 3, yticklabels = 5)
ax[2].set_ylabel('')
ax[2].set_xlabel('')
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['bottom'].set_visible(False)
ax[2].spines['left'].set_visible(False)
ax[2].tick_params(bottom=False, left=False)
cbar = ax[2].collections[0].colorbar
cbar.set_label("Z-score")
#fig = plt.figure('tumor_z_score')
ax[3].set_title('ΔWEPL Z-score')
sns.heatmap(data=dz.pivot( "gantry_angle", "couch_angle","tumor_score") ,cmap="rainbow", ax=ax[3],  xticklabels = 3, yticklabels = 5)
ax[3].set_ylabel('')
ax[3].set_ylabel('')
ax[3].set_xlabel('')
ax[3].spines['top'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].spines['bottom'].set_visible(False)
ax[3].spines['left'].set_visible(False)
ax[3].tick_params(bottom=False, left=False)
cbar = ax[3].collections[0].colorbar
cbar.set_label("Z-score")
### Axis Label Settings ###
fig.text(0.5,0.04, "Couch Angle [deg]", ha="center", va="center")
fig.text(0.05,0.5, "Gantry Angle [deg]", ha="center", va="center", rotation=90)
plt.show()


"""
Plot Final Z-Score Maps
"""
fig, ax = plt.subplots()
plt.title('Final Z-Score Map')
sns.heatmap(data=dz.pivot( "gantry_angle", "couch_angle","z_score") ,cmap="rainbow",  xticklabels = 3, yticklabels = 5)
ax.tick_params(bottom=False, left=False)
ax.set_ylabel('Gantry Angle [deg]')
ax.set_xlabel('Couch Angle [deg]')
cbar = ax.collections[0].colorbar
cbar.set_label("Z-score")
