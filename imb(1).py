
# Load CIFAR10
import numpy as np
import torchvision
from torchvision import datasets
from torchvision.transforms import transforms

#Load Data

dataset = torchvision.datasets.CIFAR10("../dataload/dataset_CIFAR10", train=True, transform=None,download=True)
test_data = torchvision.datasets.CIFAR10("../dataload/dataset_CIFAR10", train=False, transform=torchvision.transforms.ToTensor(),download=False)
# Get all training targets and count the number of class instances
targets = np.array(dataset.targets)
classes, class_counts = np.unique(targets, return_counts=True)
nb_classes = len(classes)
print(class_counts)

# Create artificial imbalanced class counts
imbal_class_counts = [500, 500, 500, 500, 500, 5000, 5000, 5000, 5000, 5000]
test_class_counts = [1000, 1000, 1000,1000,1000,1000,1000, 1000, 1000, 1000]
# Get class indices
class_indices = [np.where(targets == i)[0] for i in range(nb_classes)]

# Get imbalanced number of instances
imbal_class_indices = [class_idx[:class_count] for class_idx, class_count in zip(class_indices, imbal_class_counts)]
imbal_class_indices = np.hstack(imbal_class_indices)

# Set target and data to dataset
dataset.train_labels = targets[imbal_class_indices]
dataset.train_data = dataset.data[imbal_class_indices]

assert len(dataset.train_labels) == len(dataset.train_data)

print(dataset.train_labels)
print(dataset.train_data)



