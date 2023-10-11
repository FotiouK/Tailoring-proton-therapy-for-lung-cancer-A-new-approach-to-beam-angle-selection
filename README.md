
# Optimal Beam Angles in Proton Therapy for Lung Cancer
Welcome to the Optimal Beam Angles in Proton Therapy for Lung Cancer repository! This project presents a comprehensive proton therapy workflow, encompassing two main algorithms: the Pre-processing Algorithm and the Angle Selection Algorithm. This README provides an overview of the entire workflow, serving as your guide to navigate through the project's subfolders and understand how these algorithms work together to enhance proton therapy planning for mobile tumours.
## Overview
Proton therapy offers a precise and effective way to target cancerous cells while minimising damage to surrounding healthy tissue. However, the intricacies of proton transport in non-stationary mediums introduces challenges. Anatomical changes, driven by respiratory-induced intra-fractional motion, can significantly alter proton radiological paths, leading to dose distribution distortions and potential plan degradation. Our primary objective is to develop a robust methodology to identify optimal beam angles for proton therapy in lung cancer. These angles will not only ensure effective tumor dose delivery but also minimise the accumulated dose in nearby organs at risk (OARs), ultimately improving treatment outcomes.To optimise the angle selection procedure, we have developed a thorough workflow that consists of the following components:

- **Pre-processing Algorithm**: This initial step focuses on preparing the input data, which consists of 4D-CT scans. It involves generating CT scan representations such as the AIP, MIP and MinIP, delineating radiation therapy volumes, and converting Hounsfield Units (HU) to Relative Stopping Power (RSP). The resulting data were inputted in the angle selection algorithm and are essential for effective proton therapy planning.

- **Angle Selection Algorithm**: After pre-processing, the Angle Selection Algorithm is employed. This algorithm thoroughly evaluates the influence of incident beam geometry on plan parameters. It identifies optimal treatment angles that strike a balance between comprehensive tumor coverage and minimising radiation dose to organs at risk. Tumour dose degradation is investigated through Water Equivalent Path Length (WEPL) analysis, while the dose to organs at risk (OARs) is assessed via Percentage Volume Irradiation (PIV).

## Repository Structure

Our repository is organized into subfolders to help you navigate through the two main algorithms:

- **Pre_Processing**: This folder contains the Pre-processing Algorithm documentation. Here, you'll find detailed information on generating CT scan representations, delineating target volumes, and performing HU to RSP conversions.

- **Angle_Selection**: Inside this folder, you'll discover the Angle Selection Algorithm code and documentation. This section provides a detailed documentation of the beam simulation process for different gantry-couch angle combinations. It additionally covers the assessment of how incident beam geometry influences treatment planning parameters and finally the process of identifying optimal beam geometries tailored to each patient

- **Images:** This folder contains all the images used throughout the documentation to provide visual insights and aid in understanding the algorithms and processes described.

## Getting Started

Whether you're a researcher, a medical professional, or an enthusiast interested in proton therapy, our workflow provides valuable insights into the various steps that contribute to precise proton therapy planning. To get started, visit the specific subfolders for in-depth information on each algorithm. Follow the documentation, and don't hesitate to reach out if you have any questions or feedback.

## License

This project is open source and is released under the [MIT License](LICENSE). You are welcome to use, modify, and distribute the code and documentation in accordance with the license terms.

## Contributors

We appreciate the contributions and collaborations from the entire proton therapy community. If you would like to contribute, please follow our [Contribution Guidelines](CONTRIBUTING.md) to ensure smooth collaboration.

## Contact

If you have any questions, suggestions, or need assistance, please don't hesitate to contact us at [contact@example.com].

Thank you for being a part of our proton therapy journey!

[Insert any logos, images, or additional content you want to feature here.]
