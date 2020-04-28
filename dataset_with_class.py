import torch
from PIL import Image
from torchvision.datasets import VisionDataset
from torchvision import datasets, transforms


class SingleClassData(VisionDataset):
    def __init__(self, transform, data, targets):
        super(SingleClassData, self).__init__(root='./data', transform=transform)
        self.transform = transform
        self.data = data
        self.targets = targets

    def __getitem__(self, index):
        img, target = self.data[index], self.targets[index]
        img = Image.fromarray(img)
        img = self.transform(img)
        return img, target

    def __len__(self):
        return len(self.targets)


def dataset_with_class(train=True):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    dataset = datasets.CIFAR100('./data', train=train, transform=transform, download=True)
    data_list = []
    for i in range(100):
        index = torch.tensor(dataset.targets) == i
        data = dataset.data[index]
        targets = torch.tensor(dataset.targets)[index]
        single_class_data = SingleClassData(transform, data, targets)
        data_list.append(single_class_data)
    return data_list
