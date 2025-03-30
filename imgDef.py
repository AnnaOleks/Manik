from PIL import Image, ImageTk

def pilt(path, size):
    pilt = Image.open(path)
    pilt = pilt.resize(size)
    return ImageTk.PhotoImage(pilt)
