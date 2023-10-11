
# Optimal Beam Angles in Proton Therapy for Lung Cancer
Welcome to the Proton Therapy Workflow repository! This project presents a comprehensive proton therapy workflow, encompassing two main algorithms: the Pre-processing Algorithm and the Angle Selection Algorithm. This README provides an overview of the entire workflow, serving as your guide to navigate through the project's subfolders and understand how these algorithms work together to enhance radiation therapy planning.

## Overview
Proton therapy is a cutting-edge approach in cancer treatment that utilizes proton beams to precisely target and irradiate tumor tissues while minimizing damage to surrounding healthy organs. To optimize this therapy, we've developed a thorough workflow that consists of the following components:

- **Pre-processing Algorithm**: This initial step focuses on preparing the input data. It involves generating CT scan representations, delineating radiation therapy volumes, and converting Hounsfield Units (HU) to Relative Stopping Power (RSP). The resulting data is essential for effective proton therapy planning.

- **Angle Selection Algorithm**: Once the data is pre-processed, the Angle Selection Algorithm comes into play. This algorithm assesses the impact of incident beam geometry on plan quality, identifying optimal treatment angles while ensuring tumor coverage and minimizing dose to organs at risk. The transformation matrices for couch and gantry angles play a vital role in this step.

## Repository Structure

Our repository is organized into subfolders to help you navigate through the two main algorithms:

- **Pre_Processing**: This folder contains the Pre-processing Algorithm documentation. Here, you'll find detailed information on generating CT scan representations, delineating target volumes, and performing HU to RSP conversions.

- **Angle_Selection**: Inside this folder, you'll discover the Angle Selection Algorithm documentation. This section explains the process of assessing beam geometry, using transformation matrices, and identifying optimal treatment angles.

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
