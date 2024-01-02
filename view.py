import vedo

def display_side_by_side(path1, path2):
    mesh1 = vedo.Volume(path1)
    mesh2 = vedo.Volume(path2)

    vedo.show(mesh1, mesh2, shape=(1, 2))

if __name__ == "__main__":
    file1 = "./1.3.6.1.4.1.14519.5.2.1.6279.6001.302134342469412607966016057827.nii.gz"
    file2 = "segmented-lungs.nii.gz"
    display_side_by_side(file1, file2)

