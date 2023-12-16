import vedo
import os

def display(path):
    mesh = vedo.Volume(path)
    vedo.show(mesh)

# images_list = os.listdir("Dataset/Images")
labels_list = os.listdir("Dataset/Labels")

if __name__ == "__main__":
    display("Dataset/Labels/" + labels_list[0])
