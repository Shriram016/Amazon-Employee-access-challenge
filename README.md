# Amazon-Employee-access-challenge

When an employee starts to work at a company, he/she needs to obtain the necessary access to fulfill their role. This process is often done manually by an employee raising a request to provide the necessary access and the supervisor would pick up the request and manually grant the access to the employee. This is often a time-consuming process and needs human intervention at most stages. The idea is to replace this manual process by using a machine learning model trained using the existing data that contains details about the employee's role, department name, and so on. This model would help to automatically grant or revoke access and reduce the human involvement required in this process.

We aim to develop a Machine Learning model that takes an employee's access request as input which contains details about the employee's attributes like role, department, etc.. and the model has to decide whether to provide access or not. This problem can be seen as a Binary Classification Problem where our machine learning model should predict one of the two classes(approve/deny) as the outcome.


This dataset is available as a part of the Kaggle competition Amazon.com - Employee Access-Challenge(https://www.kaggle.com/c/amazon-employee-access-challenge/overview). The data consists of real historical data collected from 2010 & 2011. The dataset consists of 2 files train.csv and test.csv. Train.csv contains 32,769 values and test.csv contains 58,921 values.
