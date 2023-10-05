**Generating CT Scan Representations from 4D CT** 
<br /> In radiation therapy, both for diagnostic, treatment planning and volume delineations for cancers in the thoracic regions, a 3D representation of a 4D CT scan can be constructed. Among various multiplanar reconstructed scans, the three most prominently used are the Average Intensity Projection (AIP), the Maximum Intensity Projection (MIP), and the Minimum Intensity Projection (MinIP). In the 4DCT preprocessing all of the above CT scan representations are generated.
<br>
 * **AIP:** Displays the average attenuation of all voxels of the index.
 * **MIP:** Displays the voxel with highest attenuation of the index.
 * **MinIP:** Displays the voxel with minimum attenuation of the index. 
<p align="center">
  <img src="../Images/AIP_MIP_MinIP.png">
</p>

**Radiation Therapy Volumes**
<br /> The first step of treatment planning is the delineation of the target volumes and organs at risk on the planning CT scan. In the utilised dataset, the Gross Tumour Volume (GTV) and organ volumes were delineated by an experienced oncologist. To account for for subclinical microscopic malignant regions that are not visible in the GTV, an isotropic margin is imposed to generate the Clinical Target Volume (CTV). Additionally, to account for internal physiological movements, size and shape variations of the tumour the Internal Target Volume is constructed. For lung cancer cases where a 4D CT scan is acquired, we can construct the iGTV and iCTV through a geometric summation of GTV and CTV volumes from all breathing phase. Furthermore, to incorporate the extend of the motion of OARs a similar geometric summation was performed. In the scan bellow we can identify the iGTV in blue, iCTV in red, the lungs in green, the heart in orange and the spinal cord in white for patient 104
<p align="center">
  <img src="../Images/Pre_Processing/ICTV_and_ITV.png">
</p>

**Hounsfield Units (HU) to Relative Stopping power (RSP)**
A CT voxel value is a representation of the voxel’s photon attenuation relative to water. However, for the purposes of proton beam therapy, since the interaction mechanisms of the two radiation types vary, a conversion from HU to proton Relative Stopping Power (RSP) needs to be performed to estimate the proton beam range. To achieve this, a stoichiometric calibration of the CT scanner should be performed, as described by Schneider et al, to generate a conversion Hounsfield Unit Look up Table (HULT). The HULT utilised in the pre-processing code was for the specific CT scan utilised during image acquisition of our dataset and should be re-calculated for any other scan utilised. The converted CT scans for patient 104 are visualised below, with Phase 0 on the left, the AIP in the middle and the MIP on the right. Voxel values now represent the proton stopping power within each voxel relative to the stopping power in water. 
