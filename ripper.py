import sys,cv2,numpy as np

class Ripper:
    def __init__(self, split_height, base_name, base_dir='./ss/'):
        self.base_dir     = base_dir
        self.base_name    = base_name
        self.split_height = split_height


    def split_image(self, img, filename):
        height, width, channels = img.shape
        img_height, start, count = int(round(self.split_height*width)), 0, 0
        while (height-start)>img_height:
            clp = img[start:start+img_height]
            cv2.imwrite(self.base_dir+self.base_name+filename+"-"+str(count)+".jpg",clp)
            start += img_height
            count += 1
        else:
            clp = img[start:height]
            blank_img_height = img_height - clp.shape[0]
            blank_img = np.zeros((blank_img_height,width,3), np.uint8)
            blank_img = blank_img+255
            new_img = cv2.vconcat([clp, blank_img])
            cv2.imwrite(self.base_dir+self.base_name+filename+"-"+str(count)+".jpg",new_img)
