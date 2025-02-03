import cv2
import numpy as np

def tiff_to_3d_array(filepath):
    """
    Converts a tiff file into a 3D numpy array.
    
    Parameters
    ----------
    filepath : string
        Location of the filepath for the tiff file.
    
    Returns
    -------
    assembled_array : array
        3d array representing the x and y positions over time.
        (frames, x, y)
    """
    images = []

    _, images = cv2.imreadmulti(filepath, mats = images, flags = cv2.IMREAD_UNCHANGED)

    assembled_array = np.stack(images, axis=0)
    
    return assembled_array