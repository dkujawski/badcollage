'''
Created on 4/10/2011

@author: dave
'''
import ConfigParser
import Image
import os
import random

class Builder(object):
    ''' classdocs
    '''
    def __init__(self):
        ''' Constructor
        '''
        config = self.get_config()
        self.source_dir = config.get('source', 'dir')
        self.source_img_count = config.getint('output', 'img_count')
        self.source_imgs = list()
        self.out_img_size = config.get('output', 'size')    

    def get_config(self):
        ''' collect the config settings needed
        '''
        _base = os.path.dirname(os.path.abspath(__file__))
        cfg_path = os.path.join(_base, '../../config/build.cfg')
        config = ConfigParser.ConfigParser()
        config.read(cfg_path)
        return config
    
    def get_source_imgs(self):
        # get a list of files from the source directory
        file_list = [os.path.join(self.source_dir, f) 
                     for f in os.listdir(self.source_dir)]
        print len(file_list)
        # get a random sample of files from the source directory
        samples = random.sample(file_list, self.source_img_count)        
        while samples:
            # convert the file paths into image objects
            path = samples.pop()
            img = get_img_obj(path)
            if img:
                # add the image to the main image list
                self.source_imgs.append(img)
            else:
                # if this file is not an image remove it from the file list
                file_list.remove(path)
                if not file_list:
                    # if there are no more paths in the file list stop
                    break
                # add a new random file from the file list and try again
                samples.append(random.choice(file_list))
        return self.source_imgs
    
def get_img_obj(file_path):
    try:
        img = Image.open(file_path)
    except IOError as ioe:
        print ioe, ", skipping:", file_path
        return False
    if img.format:
        return img
    return False
               
if __name__ == "__main__":
    print "this is a test!\n"
    
    b = Builder()
    imgs = b.get_source_imgs()
    print len(imgs)
    
    print "\ndone!"    