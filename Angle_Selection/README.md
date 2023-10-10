### Angle Selection Algorithm

## Beam Simulation 
To assess the impact of incident beam geometry on plan quality, we developed an angle selection algorithm. This algorithm identifies the irradiated voxels for any given beam geometry by simulating proton beam paths. It relies on couch and gantry angles to determine the relative beam direction, achieved through rotation transformation matrices for an input CT scan oriented along the SI, AP, and RL direction.

**Transformation Matrices:**
</br> For gantry angle (GA) and couch angle (CA), the transformation matrices are defined as follows:

</br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Gantry Angle Matrix:* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Couch Angle Matrix:*
```plaintext                             
[1       0       0    ]                  [cos(CA) 0 -sin(CA)]
[0    cos(GA)  sin(GA)]                  [  0     1     0   ]
[0   -sin(GA)  cos(GA)]                  [sin(CA) 0  cos(CA)]
```

</br> Instead of directly transforming the scans, we divide the beam path into discrete steps, initiating from the tumour’s distal edge points and inversely simulating the proton beam paths. We utilise a directional vector [0,-1,0] to represent each step's direction, ensuring that for gantry and couch angles of 0 degrees, the beam travels normally towards the patient from the anterior direction. This methodology helps generate the step vector of magnitude 1 describing the beam path for any arbitrary gantry-couch angle combination.


<img align="left" width="100" height="100" src="image_url"> <!-- Replace 'image_url' with the URL of your image -->


**Distal Edge Identification:**
</br> To identify the tumour’s distal edge for various angle combinations, we employ a binary search approach. The algorithm uses the estimated step distance, derived from beam geometry, and the tumour’s spatial coordinates to search in the opposite direction of the step distance. Starting the search from each voxel within the tumor, the algorithm evaluates adjacent voxels along the beam path. The binary search continues until non-tumor tissue is encountered or a predetermined threshold is reached at the tumor boundary. Successful execution of the binary search results in an array containing the distal edge coordinates of the tumor.

**Generating Beam Rays**
Subsequently, we simulate beam rays inversely, using the estimated distal edge points and the beam step vector. Initiating from the identified distal edge points, the algorithm generates lines representing beam trajectories by incrementing the coordinates in the opposite direction of the beam ray. This iterative process continues until the proton ray reaches the image boundaries, encompassing all distal edge points. To handle steps with decimal places, only the coordinate corresponding to a unique voxel traversed by the beam is rounded up, while the rolling sum of coordinates retains decimal precision. The output consists of a list of lists, where each inner list contains the irradiated voxels along the proton ray's path, terminating at a distal edge point.
