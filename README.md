# ML-245-Final-Project-Repo

# SecureDNP3: A MACHINE LEARNING APPROACH TO IDENTIFY DNP3 PROTOCOL ANOMALIES AND THREATS
![image](https://github.com/ShamalaC/ML-245-Final-Project-Repo/assets/84058719/dde47fed-c325-4430-900c-2c4528a58689)

Group 06
Shubham Pravin Patil, 
Shamala Chandrappa, 
Shabari Vignesh,
Shreya Chilumukuru,
Sowmya Neela
Department of Applied Data Science
San Jose State University

Dataset source : https://ieee-dataport.org/documents/dnp3-intrusion-detection-dataset

Cleaned and Preprocessed dataset : https://drive.google.com/file/d/1bBVPtFhatXYnjcRxNB5g0zwb7sapEkyd/view?usp=drive_link


# Group Members
Shabari Vignesh (017407663), Shamala Chandrappa (017423081), Shreya Chilumukuru (017475315),
Shubham Pravin Patil (017418245), Sowmya Neela (017418219)

# Introduction
In today's ever-evolving cyber landscape and Industrial Internet of Things (IOT), the need for robust
network security measures is paramount. Traditional methods of intrusion detection often fall short in
effectively identifying and mitigating sophisticated threats. To address this challenge, we propose the
development of SecureDNP3, a network intrusion detection system powered by machine learning.
SecureDNP3 leverages advanced machine learning algorithms to analyze network traffic patterns and
identify anomalous behavior indicative of potential intrusions. By harnessing the power of historical
data, it provides a proactive approach to network security, enabling timely detection and response to
emerging threats.

# Objective
Develop and evaluate a machine learning-based network intrusion detection system capable of
accurately detecting and classifying various types of attacks in a DNP3 (Distributed Network Protocol 3)
environment including cold_restart, disable_unsolicited, enumerate, info, init_data, mitm_dos, replay,
stop_app and warm_restart with high precision and recall rates, while minimizing false positives.

# Scope
This project aims to create and deploy a sophisticated intrusion detection system, powered by machine
learning, specifically designed to effectively identify diverse classes of network intrusions with regards
to DNP3 attacks with precision. Prioritizing high accuracy and minimizing false positives, the
SecureDNP3 seeks to elevate the overall security resilience of deployed networks. Its adaptability to
emerging threats ensures a dynamic defense strategy, contributing to a proactive and resilient approach
in securing network environments.

# Methodology
1. Data Collection: Considering publicly available dataset from ieee-dataport.org which is a
comprehensive dataset of network behaviors and attacks of Distributed Network Protocol 3.
The dataset consists of 20200514_DNP3_Disable_Unsolicited_Messages_Attack,
20200515_DNP3_Cold_Restart_Attack, 20200515_DNP3_Warm_Restart_Attack,
20200516_DNP3_Enumerate, 20200516_DNP3_Ιnfo, 20200518_DNP3_MITM_DoS,
20200518_DNP3_Replay_Attack, 20200519_DNP3_Stop_Application_Attack and
Training_Testing_Balanced_CSV_Files folders. Total Dataset size is 1.34 GB.
2. Data Preprocessing: We aim to improve the quality and compatibility of datasets used in machine
learning models. Steps considered to perform data preprocessing include Handling Missing Values,
Transformation and Normalization/Standardization, Encoding Categorical Data and Data partitioning.
3. Exploratory Data Analysis (EDA): Understanding the Dataset Structure, Compute summary
statistics (mean, median, mode, standard deviation, etc.) for numerical features to get a sense of the data
distribution and Class Distribution.
4. Data Visualization: Analyzing and visualizing the data to gain insights.
5. Feature Selection: Identify and keep the most important elements that help distinguish between
regular and malicious network activities with the help of Filter Methods, Wrapper Methods and
Embedded approaches.

# Base Models:Support Vector Machines (SVM), k-Nearest Neighbors (k-NN) and Logistic Regression.
These models offer interpretability, robust classification, and efficient handling of high-dimensional
data, making them suitable for identifying intrusion patterns.
Ensemble Models: Random Forest, Gradient Boosting Machines (GBM) - LightGBM and CATBoost,
Multilayer Perceptron (MLP), Graph Neural Networks, Deep Belief Networks and Long Short-Term
Memory (LSTM). These models combine multiple learners to improve performance and robustness
against noise, enhancing accuracy in identifying instances of intrusion. They also automatically extract
relevant features and capture temporal dependencies in network traffic data, enabling effective detection
of intricate intrusion patterns. Aiming to implement all of these and will compare and choose the best
model.

# Model Evaluation and Model Deployment: Evaluating each model's performance to see which one
is most effective at detecting intrusions with the help of metrics like accuracy, precision, recall,
F1-score, and ROC-AUC etc. Targeting to use a cross-validation method to ensure that the model is
generalizable across multiple data subsets and analyze confusion matrices to better understand the
trade-off between false positives and false negatives. Also considering Grid search or randomized search
techniques to identify the hyper-parameters which require tuning. We will deploy the end-to-end project
on Google colab or Google Cloud repositories.

# Innovation
The innovation in this project could be the developing and leveraging a hybrid model that combines
Multilayer Perceptrons, Graph Neural Networks, and Deep Belief Networks; this innovative approach
enhances cyber threat detection in DNP3 protocol systems. By integrating the strengths of each model
classification, complex relationship mapping, and deep feature learning the system offers nuanced
network behavior understanding and superior adaptability to evolving threats, significantly improving
intrusion detection in critical infrastructures.

# Expected Outcome
The final outcome of this initiative will yield a fully operational Intrusion Detection System (IDS)
leveraging machine learning techniques to classify various DNP3 attacks. The IDS is poised to showcase
notable precision with minimal occurrences of false positives when identifying different classes of
network intrusions. It is strategically designed for seamless integration into current network
infrastructures, facilitating real-time monitoring of network traffic. Additionally, the system contributes
to fortifying the overall security stance of the deployed network by dynamically adapting to novel and
evolving threats as they emerge over time.

# References
[1] Panagiotis Radoglou-Grammatikis, Vasiliki Kelli, Thomas Lagkas, Vasileios Argyriou, Panagiotis
Sarigiannidis. (2022). DNP3 Intrusion Detection Dataset. IEEE Dataport. https://dx.doi.org/10.21227/s7h0-b081
[2] V. Kelli et al., "Attacking and Defending DNP3 ICS/SCADA Systems", 2022 18th International Conference on
Distributed Computing in Sensor Systems (DCOSS), 2022, pp. 183-190, doi: 10.1109/DCOSS54816.2022.00041.
[3] V. Kelli, P. Radoglou-Grammatikis, T. Lagkas, E. K. Markakis and P. Sarigiannidis, "Risk Analysis of DNP3
Attacks", 2022 IEEE International Conference on Cyber Security and Resilience (CSR), 2022, pp. 351-356, doi:
10.1109/CSR54599.2022.9850291.
[4] P. Radoglou-Grammatikis, P. Sarigiannidis, G. Efstathopoulos, P.-A.Karypidis, and A. Sarigiannidis, "Diderot:
An intrusion detection and prevention system for dnp3-based scada systems", in Proceedings of the15th
International Conference on Availability, Reliability and Security, ser. ARES ’20.New York, NY, USA: Association
for Computing Machinery, 2020, doi: 10.1145/3407023.3409314.
[5] J. Shah, "Understanding and study of intrusion detection systems for various networks and domains," 2017
International Conference on Computer Communication and Informatics (ICCCI), Coimbatore, India, 2017, pp.
1-6, doi: 10.1109/ICCCI.2017.8117726.
