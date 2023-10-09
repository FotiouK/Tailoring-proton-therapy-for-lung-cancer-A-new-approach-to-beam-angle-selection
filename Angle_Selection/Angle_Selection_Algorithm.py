# -*- coding: utf-8 -*-
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

"""
Functions utilised for the Angle-Selection Algorithm
"""

def calculate_distances(lines_coords ):
    """
    Parameters
    ----------
    lines_coords : Array represending the coordinates that the beam passes through
    Returns
    -------
    distances : Euclidean Chord Distance taking into consideration voxel dimensions. 

    """
    distances = []
    voxel_size= [3.0,1.0527,1.0527]
    for line_coords in lines_coords:
        first_point = np.array(line_coords[0]) * voxel_size
        last_point = np.array(line_coords[-1]) * voxel_size
        num_vox = len(line_coords) -1
        distance = euclidean(first_point, last_point)/(num_vox)
        distances.append(distance)
    return distances



def generate_steps(theta,phi,direction_vector):
    """
    Parameters
    ----------
    theta : Gantry Angle in degrees.
    phi : Couch Angle in degrees
    direction_vector : Vector indicating initial beam direction. In radiotherapy is towards Anterior direction 
    Returns
    -------
    z_step : Step distance in the SI direction for magnitude 1 vector 
    y_step : Step distance in the AP direction for magnitude 1 vector
    x_step : Step distance in the RL direction for magnitude 1 vector

    """
    
    cos_g = np.cos(np.deg2rad(theta))
    sin_g = np.sin(np.deg2rad(theta))
    cos_c = np.cos(np.deg2rad(phi))
    sin_c = np.sin(np.deg2rad(phi))
    
    
    trans_matrix_g = np.array([[1, 0, 0],
                            [0, cos_g, sin_g],
                            [0, -sin_g, cos_g]])
    trans_matrix_c = np.array([[cos_c, 0, -sin_c],
                            [0, 1, 0],
                            [sin_c, 0, cos_c]])
    trans_matrix = np.matmul(trans_matrix_c, trans_matrix_g)
    z_step, y_step, x_step = np.matmul(trans_matrix, [0,-1,0])
    print('step size is' ,z_step, y_step, x_step )
    return (z_step, y_step, x_step)



def get_distal_edge_point(tumor, steps, threshold=40):
    """
    Parameters
    ----------
    tumor : A 3D array describing tumor coordinates
    steps : Steps that will define the direction of the beam based on the angle combinations. 
            Use negative step to find the distal edge.
    threshold : Threshold to limit the binary search so the code does not run forever
    Returns
    -------
    distal_points : A list of all the distal edge points coordinates
    distal_array : A 3D array representing the distal edge.
    """
    print('Calculating distal points')
    distal_points = []
    distal_array = np.zeros_like(tumor)
    z_step, y_step, x_step = steps
    for i in range(tumor.shape[0]):
        for j in range(tumor.shape[1]):
            for k in range(tumor.shape[2]):
                if tumor[i, j, k] == 1:
                    z, y, x = i - z_step, j - y_step, k - x_step
                    count = 0
                    is_distal_edge = False
                    while z >= 0 and int(np.round(z)) < tumor.shape[0] and y >= 0 and int(np.round(y)) < tumor.shape[1] and x >= 0 and int(np.round(x)) < tumor.shape[2] and count < threshold:
                        z_round, y_round, x_round = int(np.round(z)),int(np.round(y)),int(np.round(x))
                        if tumor[z_round, y_round, x_round] == 0:
                            break
                        if tumor[z_round, y_round, x_round] == 1:
                            is_distal_edge = True
                        count += 1
                        z, y, x = z - z_step, y - y_step, x - x_step
                    if is_distal_edge and count < threshold:
                        z, y, x = int(z), int(y), int(x)
                        distal_points.append((z, y, x))
                        distal_array[z,y,x] = 1
            distal_points =[*set(distal_points)]
    return distal_points , distal_array


def generate_lines(tumor, distal_points, steps):
    """
    Parameters
    ----------
    tumor : A 3D array describing tumor coordinates
    distal_points : Array representing the distal edge points for the specific angle combinations 
    steps : Steps that will define the direction of the beam based on the angle combinations
    Returns
    -------
    lines : A 3D array that idicates all the voxels that the beam will pass through
    lines_coords : A list of arrays that indicate the coordinates from the disatl edge point 
                   to the last point of the beam before it goes out of bounds
        DESCRIPTION.

    """
    print('Generating lines')
    lines_coords = []
    lines_coords_set = []
    lines = np.zeros_like(tumor)
    z_step, y_step, x_step = steps
    for distal_point in distal_points:
        i, j, k = distal_point[:3]
        line_coords = []
        line_coords_set = set()
        z, y, x = i,j,k
        while (0 <= int(z) < tumor.shape[0]) and (0 <= int(y) < tumor.shape[1]) and (0 <= int(x) < tumor.shape[2]):
            current_point = (int(z), int(y), int(x))
            if current_point not in line_coords_set:
                line_coords_set.add(current_point)
                line_coords.append(current_point)
            lines[int(z), int(y), int(x)] = 1
            z += z_step
            y += y_step
            x += x_step
        lines_coords.append(line_coords)
        lines_coords_set.append(list(line_coords_set))
    return lines , lines_coords



def main(tumor, phi, theta):
    steps = generate_steps(theta,phi,[0,-1,0])
    distal_points , distal_array= get_distal_edge_point(tumor,steps)
    lines ,lines_coords= generate_lines(tumor, distal_points,steps)
    distance = calculate_distances(lines_coords)
    return lines_coords,distance, lines


def calculate_beam_wepl(ct, lines_coords, distance):
    """
    Parameters
    ----------
    ct : 3D array of the CT scan to be investigated
    lines_coords : List of arrays that indicate the coordinates the beam passes through.
    distance : The Euclidean chord distance.

    Returns
    -------
    beam_wepl : A list of the WEPL values of the projected beams
        [BEV, each voxel is represented by the sum of all voxels behind it along the beam direction]. 

    """
    beam_wepl = []
    for line_cord in lines_coords:
        line_sum = 0
        for coord in line_cord:
            line_sum += ct[coord[0], coord[1], coord[2]]
        beam_wepl.append(line_sum * np.mean(distance))
    return beam_wepl

def oar_irradiated_vol(oar,lines,oar_name):
    """
    Parameters
    ----------
    oar : Array of OAR investigated
    lines : Array showing the beam path for specific angles 
    Returns
    -------
    perc_oar_vol : Percentage volume overlap of the irradiated OAR.

    """
    print('Calculate percentage irradiated volume of "{}"'.format(oar_name))
    oar_total_vol = np.sum(oar)
    lines_oar = np.where(lines>=1, oar,0)
    if np.max(lines_oar)>=1:
        oar_beam_volume = np.sum(lines_oar)
        perc_oar_vol = (oar_beam_volume/oar_total_vol)*100
    else:
        perc_oar_vol = 0
    return perc_oar_vol


def central_angle(ca1,ga1,ca2,ga2):
    """
    Parameters
    ----------
    ca1 : Couch Angle 1
    ga1 : Gantry Anlge 1
    ca2 : Couch Angle 2
    ga2 : Gantry Anlge 2
    Returns
    -------
    ds : Calculated Central Angle between the two beam geometries.
    """
    ga1 = np.add(ga1,90)
    ga2 = np.add(ga2 ,90)
    ca1 = np.deg2rad(ca1)
    ga1 = np.deg2rad(ga1)
    ca2 = np.deg2rad(ca2)
    ga2 = np.deg2rad(ga2)
    ds = np.arccos((np.sin(ga1)*np.sin(ga2))+(np.cos(ga1)*np.cos(ga2)*np.cos(abs(ca1-ca2))))
    ds = np.rad2deg(ds)
    ds = np.round(ds)
    return ds


# define function to check if two angles have a central angle difference of at least 20 degrees
def has_central_angle_diff(ca1, ga1, ca2, ga2,df):
    """
    Parameters
    ----------
    ca1 : Couch Angle 1
    ga1 : Gantry Anlge 1
    ca2 : Couch Angle 2
    ga2 : Gantry Anlge 2
    df : Imposed Beam Separation in Degrees 
    Returns
    -------
    None.
    """
    return central_angle(ca1, ga1, ca2, ga2) >= df

"""
Functions end 
"""

"""
Load Input Arrays
"""
# load transforemd RSP 4DCT
with open("ct_eval_rsp.pkl", "rb") as f:
    ct_list = pickle.load(f)
    print('ct_list loaded')
## Load planning AIP or MIP RSP CT scans
ref_mip_ct= np.load('ct_mip_rsp.npy')
ref_ave_ct= np.load('ct_ave_rsp.npy')
print('load plan CT')
#Load Planning Tumour Volume 
tumor = np.load('ictv.npy')
print('load tumor')

## Load pre-determined angles for itterations
df = pd.read_csv('accepted_angles.csv')
print('load angles')

#Load Investigated OARs
heart = np.load('heart.npy')
print('Load Heart')
cord = np.load('cord.npy')
print('Load Cord')
rlung = np.load('rlung.npy')
print('Load RLung')
llung = np.load('llung.npy')
print('Load LLung')
lungs = np.load('lungs.npy')
print('Load Total lung')


"""
### Call Funations to Identify ΔWEPL and PIV For OARs
"""
## Generate OAR empty arrays
beam_heart = []
beam_cord = []
beam_rlung = []
beam_llung = []
beam_lungs = []
## Generate WEPL empty arrays
oar_beam = []
max_wepl =[]
min_wepl = []
mean_WEPL = []
# Generate empty array for beam geometry
couch_angles= []
gantry_angles =[]

### Load Pregenerated Beam Geometries Template ###
#### If a predeterminned template is used make sure following indetations are corrected ## 
# for index, row in df.iterrows():
#     gantry_angle = row['gantry_angle']
#     couch_angle = row['couch_angle']

### Generate Beam Geometries For Itterations ###
for couch_angle in range(-90, 91, 15 ):       
    for gantry_angle in range(0, 360, 10):
        gantry_angle = gantry_angle%360
        print(f"gantry_angle: {gantry_angle}\tcouch_angle: {couch_angle}")
        lines_coords, distance, lines = main(tumor , couch_angle ,gantry_angle)
    
    ### Calculate Reference WEPL ###
        ref_wepl = calculate_beam_wepl(ref_ave_ct, lines_coords, distance)
    
    ### Calculate Evaluated WEPL ###
        i = 0
        eval_wepls = []
        for ct in ct_list:
            i = i+1 
            print(i)
            eval_beam_wepl = calculate_beam_wepl(ct, lines_coords, distance)
            eval_wepls.append(eval_beam_wepl)
    ### Calculate Diference in WEPL ###        
        dif_phase_wepl = []
        dif_phase_mean_wepl=[]
        ## Calculate absolute diference in WEPL
        for eval_wepl in eval_wepls:
            dif_wepl = np.subtract(np.array(ref_wepl), np.array(eval_wepl))
            dif_phase_mean_wepl.append(np.mean(np.abs(dif_wepl)))
            dif_phase_wepl.append(dif_wepl)
    
    ### Calculate PIV for OARs ###
        heart_irr = oar_irradiated_vol(heart, lines, 'heart')
        cord_irr = oar_irradiated_vol(cord,lines, 'cord')
        rlung_irr = oar_irradiated_vol(rlung,lines, 'rlung')
        llung_irr = oar_irradiated_vol(llung,lines, 'llung')
        lungs_irr = oar_irradiated_vol(lungs,lines, 'lungs')
    
    ### Append WEPL itteration calculations ###
        max_wepl.append(np.max(dif_phase_mean_wepl))
        min_wepl.append(np.min(dif_phase_mean_wepl))
        mean_WEPL.append(np.mean(dif_phase_mean_wepl))    
        gantry_angles.append(gantry_angle)        
        couch_angles.append(couch_angle)
    
    ### Append PIV itteration calculations ###   
        beam_heart.append(heart_irr)
        beam_cord.append(cord_irr)
        beam_rlung.append(rlung_irr)
        beam_llung.append(llung_irr)
        beam_lungs.append(lungs_irr)


### Generate and Save dataframe of patient ###
data = {'couch_angle':couch_angles,
      'gantry_angle':gantry_angles,
      'beam_heart':beam_heart,
      'beam_cord':beam_cord,
      'beam_rlung':beam_rlung,
      'beam_llung':beam_llung,
      'beam_lungs':beam_lungs,
      'wepl':mean_WEPL,
      'max_wepl':max_wepl,
      'min_wepl':min_wepl}      
  
#Generate Pandas Dataframe ###     
df = pd.DataFrame(data, index = couch_angles )
print(df.head())
### Save Dataframe ###
df.to_csv('p104_angle_selection.csv')

"""
Identify Optimal Beam Geometries 
"""

"""
Convert Variables to Z-Score statistics
"""
df['tumour_score'] = stats.zscore(df['wepl'])
df['heart_score'] = stats.zscore(df['beam_heart'])
df['cord_score'] = stats.zscore(df['beam_cord'])
df['lungs_score'] = stats.zscore(df['beam_lungs'])


### Patient Specific Weighting Factors For Each Variable Plan Objecctive ###
# Tumour Weighting Factor
tw = 2
# Heart Weighting Factor
hw = 1
# Spinal Cord Weighting Factor
cw = 0.5
# Lungs Weighting Factor
lw = 1.8

### Create a new Dataframe with converted Z-score and final Z-score Map ###
dz = pd.DataFrame()
dz['couch_angle'] = df['couch_angle']
dz['gantry_angle'] = df['gantry_angle']
dz['tumor_score'] = df['tumour_score']
dz['heart_score'] = df['heart_score']
dz['cord_score'] = df['cord_score']
dz['lungs_score'] = df['lungs_score']
dz['Final_z_score']= df['tumor_score']*tw + df['heart_score']*hw + df['cord_score']*cw + df['lungs_score']*lw

### Save Dataframe ###
dz.to_csv('p104_z_score_data.csv')


### Reduce to the percentage of rows with lowest Z-score value to minimise angle selection iterations. In this example we opted for 25% ###
## Sort the DataFrame by 'Final_z_score' in ascending order ##
dz_sorted = dz.sort_values(by='z_score')
## Calculate the number of rows to select (25% of the total rows) ##
num_rows_to_select = int(len(dz_sorted) * 0.25)
## Select the 25% rows with the lowest 'Final_z_score' values ##
reduced_lowest_z_scores = dz_sorted.head(num_rows_to_select)

### Set Initial Minimum z-value to infinite ###
min_z = float('inf')
### Iterate Over All Possible Combinations Of Three Angles ###
for i, (ca1, ga1, z1) in reduced_lowest_z_scores.iterrows():
    for j, (ca2, ga2, z2) in reduced_lowest_z_scores.iterrows():
        for k, (ca3, ga3, z3) in reduced_lowest_z_scores.iterrows():
            ## Check If The Three Angles Have A Central Angle Difference Of At Least 20 degrees ##
            if has_central_angle_diff(ca1, ga1, ca2, ga2, 20) and \
                has_central_angle_diff(ca2, ga2, ca3, ga3, 20) and \
                has_central_angle_diff(ca3, ga3, ca1, ga1, 20):
                print([ca1, ga1], [ca2,ga2],[ca3, ga3]) 
                ## Calculate Cumulative Z-value ##
                z_value = z1 + z2 + z3
                ## Check If This Is The New Minimum Z-Value ##
                if z_value < min_z:
                    ## Store Angles And Z-Value ##
                    min_combinations = [(ca1, ga1), (ca2, ga2), (ca3, ga3)]
   
                    min_z = z_value
### Print Final Results ###
print("Minimum z-value:", min_z)
print("Optimal Angle combinations:", min_combinations)

