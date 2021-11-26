Deep Learning with Class Imbalance

This project is about deep learning with class imbalance.

Files included:

1. base_model.ipynb has the results of base model.

2. model_cifar_10.ipynb is compatible with cifar-10 for further manual dynamic sampling.

3. model_Mnist.ipynv is compatible with Mnist for further manual dynamic sampling.

All files are .ipynb and all pre-request packages are stated in the first block of Jupyter notebook.

This model is compatible with Cifar-10 and Mnist dataset with separated files.

Running instruction:

1. Input the imbalance situation of datasets, which means the number of sample in each class.
   Eg: imbal_class_counts=[250, 250, 250, 500, 500, 500, 2500, 2500, 2500, 5000]

2. Execute the base model with 50 epochs.

3. Manually adjust the number of samples of each class based on the classification report from base model and run all remaining blocks except last one.

4. Update the weight of each sample and make sure X and Y have same dimensions then run.

5. Repeat instruction 3 and 4 till the model converge.

6. Run the last block and get final test results.