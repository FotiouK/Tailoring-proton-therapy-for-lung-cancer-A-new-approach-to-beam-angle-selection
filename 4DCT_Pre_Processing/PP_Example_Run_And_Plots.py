"""
Created on Wed Jan 25 14:09:06 2023

@author: kyria
"""
import os  
import numpy as np
import matplotlib.pyplot as plt 
from scipy import ndimage

"""
Load inputed Arrays
"""
## Generate empty arrays
ct_list = []
tumor_list = []
heart_list = []
cord_list = []
RLung_list = []
LLung_list = []
voxel_size=(3.0,0.9766,0.9766)

### Load CT arrays ### 
# giving directory name
dirname = 'CT'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        ct = np.load(filepath)
        ct_list.append(ct)

### Load Tumor arrays ###
# giving directory name
dirname = 'Tumor'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        tum = np.load(filepath)
        tumor_list.append(tum)

### Load Organs At Risk ###
### Heart ###
# giving directory name
dirname = 'heart'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        hea = np.load(filepath)
        heart_list.append(hea)

### Spinal Cord ###
# giving directory name
dirname = 'cord'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        sc = np.load(filepath)
        cord_list.append(sc)

### Right Lung ###    
# giving directory name
dirname = 'Rlung'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        rl = np.load(filepath)
        RLung_list.append(rl)

### Left Lung ###    
# giving directory name
dirname = 'Llung'
# giving file extension
ext = '.npy'
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        filepath = dirname + '/' + files
        # Load the STL files and add the vectors to the plot
        ll = np.load(filepath)
        LLung_list.append(ll)
        
        
"""
### Call the funations
"""
#Generate AIP,MIP and MinIP CT scans
AIP_ct, MIP_ct ,MinIP_ct = generate_ct_maps(ct_list)
#Transfrom 4D CT scans from HU to RSP.
ct_eval_rsp = transform_HU_to_RSP(ct_list)
#Transfrom AIP and MIP CT scans from HU to RSP.
ct_ave_rsp = transform_HU_to_RSP(AIP_ct)
ct_mip_rsp = transform_HU_to_RSP(MIP_ct)
#Generate OAR Maps
heart = generate_oar_maps(heart_list)
cord = generate_oar_maps(cord_list)
rlung = generate_oar_maps(RLung_list)
llung = generate_oar_maps(LLung_list)
#Generate combined lung contour
lungs = np.add(rlung,llung)
lungs= np.where(lungs >0.1,1,lungs)
#Generate ITV,CTV and iCTV
itv, ctv_list , ictv = generate_itv_ctv_ictv(tumor_list, voxel_size, 5)



"""
### Visualisation Checks ###
"""

"""
### Visualisation of Volumes ###
"""
#Mask all arrays for visualisation.
itv_masked = np.ma.masked_where(itv == 0, itv)
ictv_masked = np.ma.masked_where(ictv == 0, ictv)
hrt_masked = np.ma.masked_where(heart == 0, heart)
crd_masked = np.ma.masked_where(cord == 0, cord)
lungs_masked = np.ma.masked_where(lungs == 0, lungs)

##Plot in the Transverse plane
fig4 = plt.figure('ICTV and ITV', figsize= (4,4))
#plot CT in gray scale 
plt.imshow(ct[41,:,:], cmap='gray')
#color code each volume
plt.imshow(ictv_masked[41,:,:], alpha=0.7,cmap='Reds', vmin = 0)
plt.imshow(itv_masked[41,:,:],alpha=0.7 ,cmap='Blues', vmin = 0)
plt.imshow(crd_masked[41,:,:],alpha=0.5 ,cmap='pink', vmin = 0)
plt.imshow(lungs_masked[41,:,:],alpha=0.5 ,cmap='Greens', vmin = 0)
plt.imshow(hrt_masked[41,:,:],alpha=0.5 ,cmap='Oranges', vmin = 0)
plt.xticks([])
plt.yticks([])
plt.show()

"""
### Visualistion of CT-Scans ###
"""
### Plot AIP MIP and MinIP CT scans ###
fig = plt.figure('CT Scans')
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# plot the average CT on the first subplot
axs[0].imshow(AIP_ct[85,:,:], cmap='gray')
axs[0].set_title('Average CT')
# plot the MIP CT on the second subplot
axs[1].imshow(MIP_ct[85,:,:], cmap='gray')
axs[1].set_title('MIP CT')
# plot the MinIP CT on the third subplot
axs[2].imshow(MinIP_ct[85,:,:], cmap='gray')
axs[2].set_title('MinIP CT')
plt.show()   

### Plot RSP converted CT Scans ###
#Get phase 0 CT from the 4D CT scan set
ct_eval = ct_list[1]
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# plot the RSP average CT on the first subplot
ax1 = axs[0].imshow(ct_ave_rsp[85,:,:])
axs[0].set_title('AIP RSP CT')
# plot the RSP MIP CT on the second subplot
ax2 = axs[1].imshow(ct_mip_rsp[85,:,:])
axs[1].set_title('MIP RSP CT')
# plot the RSP Phase 0 CT on the third subplot
ax3 = axs[2].imshow(ct_eval[85,:,:])
axs[2].set_title('Evaluate RSP CT')
cbar_ax = fig.add_axes([0.925, 0.15, 0.03, 0.7])
plt.colorbar(ax3, cax=cbar_ax)
plt.show()
  
