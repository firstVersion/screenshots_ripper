import sys,cv2,os

class Photographer:
    def __init__(self, base_url, base_name="pg", base_dir='./ss/'):
        self.base_url      = base_url
        self.base_name     = base_name
        self.base_direcoty = base_dir

    def get_image(self, filename, width="372"):
        url         = self.base_url,
        name        = self.base_name+filename,
        directory   = self.base_directory
        command = "webkit2png -F -s 1 -W %s -D %s -o %s %s" % (width, directory, name, url)
        result = os.system(command)
        if result == 0:
            return cv2.imread(directory+name+"-full.png")
