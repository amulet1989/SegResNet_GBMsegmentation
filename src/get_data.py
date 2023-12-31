import os
from glob import glob
from typing import List, Dict


def get_file_data_label(
    data_path: str, label_path: str, modalities: List[str] = []
) -> List[Dict]:
    """Get the list of patient cases path as
    List[Dict]->[{'image':[paths of images], 'label':[paths of labels]}
    Arg:
         data_path(str): path directory, it has a folder by patient with MRIs
         label_path(str): path directory to labels a .nni.gz by patient
         modalities(List[str]): List of modalities to include example ['T1.', 'T1GD.', ...].
         if you want select all just setup modalities = [] or omit it
     return:
         dict_files(List[Dict]):  [{'image':[paths of images], 'label':[paths of labels]}]
    """
    list_data_ = sorted(os.listdir(data_path))
    list_lab_ = sorted(os.listdir(label_path))

    list_data_files = []
    if modalities == []:
        for folder in list_data_:
            data_mri = sorted(glob(os.path.join(data_path, folder, "*.nii.gz")))
            list_data_files.append(data_mri)
    else:
        files = [f"*{mri}*nii.gz" for mri in modalities]
        for folder in list_data_:
            data_mri = []
            for file in files:
                data_mri += glob(os.path.join(data_path, folder, file))
            list_data_files.append(data_mri)

    list_labels_files = []
    for file in list_lab_:
        label_mri = os.path.join(label_path, file)
        list_labels_files.append(label_mri)

    dict_files = []
    for i in range(len(list_labels_files)):
        diccionario = {"image": list_data_files[i], "label": list_labels_files[i]}
        dict_files.append(diccionario)
    return dict_files
