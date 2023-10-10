### Angle Selection Algorithm

## Beam Simulation 
To assess the impact of incident beam geometry on plan quality, we developed an angle selection algorithm. This algorithm identifies the irradiated voxels for any given beam geometry by simulating proton beam paths. It relies on couch and gantry angles to determine the relative beam direction, achieved through rotation transformation matrices for an input CT scan oriented along the SI, AP, and RL direction.

**Transformation Matrices:**
</br> For gantry angle (GA) and couch angle (CA), the transformation matrices are defined as follows:

</br> *Gantry Angle Matrix:*      
```plaintext
[1       0       0    ]  
[0    cos(GA)  sin(GA)]
[0   -sin(GA)  cos(GA)]

\\\


*Couch Angle Matrix:*
```plaintext
[cos(CA) 0 -sin(CA)]
[  0     1     0   ]
[sin(CA) 0  cos(CA)]
