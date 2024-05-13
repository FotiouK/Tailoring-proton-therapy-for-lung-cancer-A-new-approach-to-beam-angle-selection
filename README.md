# Tailoring proton therapy for lung cancer: A new approach to beam angle selection
Welcome to the tailoring proton therapy for lung cancer repository! This project presents a comprehensive proton therapy workflow, encompassing two main algorithms: the Pre-Processing Algorithm and the Angle Selection Algorithm. This README provides an overview of the entire workflow, serving as your guide to navigate through the project's subfolders and understand how these algorithms work together to enhance proton therapy planning for mobile thoracic tumours. 




<img src="https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/assets/108896534/f32736e3-822a-4566-ba69-ab9f1ca5d39c" alt="p100_gif" style="height: 300px;" /> <img src="https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/blob/main/Images/Angle_Selection/p104_Beam_Visualisation.png" alt="Image 2" style="height: 300px;" />


## Overview
Proton therapy offers a precise and effective way to target cancerous cells while minimising damage to surrounding healthy tissue. However, the intricacies of proton transport in non-stationary mediums introduces challenges. Anatomical changes, driven by respiratory-induced intra-fractional motion, can significantly alter proton radiological paths, leading to dose distribution distortions and potential plan degradation. Our primary objective is to develop a robust methodology to identify optimal beam angles for proton therapy in lung cancer. These angles will not only ensure effective tumor dose delivery but also minimise the accumulated dose in nearby organs at risk (OARs), ultimately improving treatment outcomes.To optimise the angle selection procedure, we have developed a thorough workflow that consists of the following components:

- **Pre-processing Algorithm**: This initial step focuses on preparing the input data, which consists of 4D-CT scans. It involves generating CT scan representations such as the AIP, MIP and MinIP, delineating radiation therapy volumes, and converting Hounsfield Units (HU) to Relative Stopping Power (RSP). The resulting data were inputted in the angle selection algorithm and are essential for effective proton therapy planning.

- **Angle Selection Algorithm**: After pre-processing, the Angle Selection Algorithm is employed. This algorithm thoroughly evaluates the influence of incident beam geometry on plan parameters. It identifies optimal treatment angles that strike a balance between comprehensive tumour coverage and minimising radiation dose to organs at risk. Tumour dose degradation is investigated through Water Equivalent Path Length (WEPL) analysis, while the dose to organs at risk (OARs) is assessed via Percentage Volume Irradiation (PIV).

## Repository Structure

Our repository is organised into subfolders to help you navigate through the two main algorithms:

- **[Pre_Processing](https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/tree/main/4DCT_Pre_Processing):** This folder contains the Pre-processing Algorithm documentation and code. Here, you'll find detailed information on generating CT scan representations, delineating radiotherapy volumes, and performing HU to RSP conversions.

- **[Angle_Selection](https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/tree/main/Angle_Selection):** Inside this folder, you'll discover the Angle Selection Algorithm code and documentation. This section provides a detailed documentation of the beam simulation process for different gantry-couch angle combinations. It additionally covers the assessment of how incident beam geometry influences treatment planning parameters and finally the process of identifying optimal beam geometries tailored to each patient

- **[Validation_Angle_Selection](https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/tree/main/Validation_Angle_Selection):** This section delves into the validation process for the Angle Selection Algorithm. It includes information about the patient dataset, the generated proton therapy treatment plans, and subsequent dose analysis. Additionally, you will find the results for all 11 patients utilised in our validation. This provides essential insights into the algorithm's effectiveness in personalising proton therapy treatment plans.

- **[Images](https://github.com/FotiouK/Optimising_Beam_Angles_in_Proton_Therapy_of_Lung_Cancer/tree/main/Images):** This folder contains all the images used throughout the documentation to provide visual insights and aid in understanding the algorithms and processes described.

## Getting Started

Whether you're a researcher, a medical professional, or an enthusiast interested in proton therapy or medical image analysis, our workflow provides valuable insights into the various steps that contribute to precise proton therapy planning. To get started, visit the specific subfolders for in-depth information on each algorithm. Follow the documentation, and don't hesitate to reach out if you have any questions or feedback.

## License 
This project is provided under the MIT License. You are welcome to use, modify, and distribute the codes presented in the repository under the terms of the MIT License. Please refer to the "LICENSE" file and the accompanying license documentation for full details.
Please be aware that this project is intended for research purposes only and should not be used for clinical applications. 

## Contact
If you have any questions, suggestions, or need assistance, please do not hesitate to contact us at [kyriakosfotiou1@gmail.com](mailto:kyriakosfotiou1@gmail.com)
<br>Thank you for joining us on identifying personalised proton therapy solutions for lung cancer patients.
