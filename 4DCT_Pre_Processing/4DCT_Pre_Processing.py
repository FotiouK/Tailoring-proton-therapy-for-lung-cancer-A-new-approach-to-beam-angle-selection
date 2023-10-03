"""
@author: Kyriakos Fotiou
"""
import numpy as np
from scipy import ndimage


def generate_oar_maps(oar_list):
    """
    Parameters
    ----------
    oar_list : A list of Arrays containign CT in numpy array format 
    Returns
    -------
    oar : Array depicting the composite of all organ contours from the 4D CT scan.
    """
    print('Generate OAR map')
    oar = np.sum(oar_list, axis = 0)
    oar[oar>=1]=1
    return oar


def generate_ct_maps(ct_array):
    """
    Parameters
    ----------
    ct_array : A list of Arrays containign CT in numpy array format 
    Returns
    -------
    AIP_ct : The average attenuation of each voxel is displayed.
    MIP_ct : The voxel with the highest attenuation is displayed.
    MinIP_ct : The voxel with the lowest attenuation is displayed.
    """
    # calculate the average CT
    AIP_ct = np.mean(ct_array, axis=0)
    # calculate MIP CT
    MIP_ct = np.amax(ct_array, axis=0)
    #Calculate MinIP CT
    MinIP_ct = np.amin(ct_array, axis=0)
    return AIP_ct, MIP_ct ,MinIP_ct


def generate_itv_ctv_ictv(tumor_list, voxel_size, expansion_magnitude):
    """
    Parameters
    ----------
    tumor_list : A list of Arrays containign tumor coordinates in numpy array format
    voxel_size : Voxel dimensions of the CT scan
    expansion_magnitude : Magnitude of expansion of the tumour in mm.
    Returns
    -------
    ctv_list : A list of Arrays containign expanded tumor coordinates.
    ictv : Array depicting the composite of all CTV controus.
    """
    print('generate ctv')
    ctv_list =[]
    #Generate ITV
    itv = np.sum(tumor_list, axis=0)
    itv[itv>=1]=1
    #Generate CTV and iCTV
    i= 0
    for tumor in tumor_list:
        i = i +1
        print(i)
        # Calculate the dilation radius for the x-y plane only
        dilation_radius = tuple(expansion_magnitude / np.array(voxel_size))
        new_array = np.zeros_like(tumor)
        ctv = np.zeros_like(tumor)
        # Find the tumor indices
        tumor_indices = np.argwhere(tumor)
        # Get the min and max indices for the tumor in the z-axis
        z_min = np.min(tumor_indices[:, 0])
        z_max = np.max(tumor_indices[:, 0])
    
        # Iterate over the z-axis where there is tumor
        for z in range(z_min, z_max+1):
            # Get the x-y slice of the tumor for this z-index
            tumor_slice = tumor[z,:,:]
    
            # Expand the tumor in the x-y plane using binary dilation
            dilated_array = ndimage.binary_dilation(tumor_slice, structure=np.ones(shape=(3,3),dtype=float),iterations=int(np.floor(np.max(dilation_radius[1]))))
    
            # Update the tumor array with the dilated array for this z-index
            new_array[z,:,:] = dilated_array
            
        dilated_array_z = ndimage.binary_dilation(new_array, structure= np.ones(shape=(3,1,1),dtype=float), iterations=int(np.floor(dilation_radius[0])))
        ctv[:,:,:] =  dilated_array_z
        ctv_list.append(ctv)
    ictv = np.sum(ctv_list, axis=0)
    ictv[ictv>=1]=1

    return itv,ctv_list, ictv



def transform_HU_to_RSP(ct_array):
    """
    Parameters
    ----------
    ct_array : A list of Arrays containign CT in numpy array format 
    Returns
    -------
    RSP_ct_array: A list of Arrays containign the transformed CT from HU to RSP values 

    """
    RSP_ct_array = []
    for array in ct_array:
        new_array = array.copy()
        print("RSP_eval:")
        new_array[array > 40] = new_array[array > 40]*0.000976438425349501+ 1.01685572002769
        new_array[(array > 20) & (array <= 40)] = new_array[(array > 20) & (array <= 40)]*0.00102118905637142 + 1.01596070740725
        new_array[array <= 20] = new_array[array <= 20]*0.000694191199870186 + 1.0290406216673
        RSP_ct_array.append(new_array)
    return RSP_ct_array


