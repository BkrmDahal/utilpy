import string
import os
import logging
import re
import urllib.request
import zipfile

import yaml
import requests
from bs4 import BeautifulSoup

def format_filename(s):
    """
    Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.
    
    Args:
        s:``str``
            string
        
    Returns:
        Valid filename : ``str``
    """
    
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_')
    return filename

def walk_directory(dir_path, files_only = True):
    """
    Get list of all file in directory recursive
    
    Args:
        dir_path:``str``
            parent directory to start
        files_only:``bool``
            get list of files only other
    
    Return:
        If file only than list of all files 
        otherwise files and list of directories
        
    """

    list_files = []
    list_dir = []
    for root, directories, filenames in os.walk(dir_path):
        for filename in filenames: 
            list_files.append(os.path.join(root,filename))
        for directory in directories:
            list_dir.append(os.path.join(root, directory))
                
    if files_only:
        return list_files
    else:
        return list_files, list_dir
    
def read_config(filename):
    """
    Parse config yaml file
    
    Args:
        filename:``str``
            path of config file
            
    """
    
    with open(filename, 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            
            
def download_file(url, 
                  save_dir = 'tmp/',
                  filename=None):
    """download and save  the file
    
    Args:
        url:``str``
            url of file
        save_dir:``str``
            directory to save
        filename:``str``
            Name of file to save as
            
    """
    if not filename:
        filename = url.split('/')[-1]
        filename = format_filename(filename)
        
    save_dir_path = save_dir+filename
    
    #make folder, if folder doesnt exists 
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    
    urllib.request.urlretrieve(url, save_dir_path)
    
def download_files(urls, save_dir = 'tmp/'):
    """download all files from urls
    
    Args:
        urls:``list``
            urls of file
        save_dir:``str``
            directory to save
            
    """ 
    for url in urls:
        download_file(url, save_dir, None)
        
def logger(logger_name = __name__, 
           filename = 'log.log', 
           level = logging.DEBUG):
    """
    logger for logging
    
    Args:
        logger_name:``str``
            name of logger
        filename:``str`` 
            path and file name
        level:``str``
            logging level
        
    Return:
        logger funcation for logging:``logger``
        
    """
    #set logger
    logger = logging.getLogger(logger_name)

    # create a file handler
    handler = logging.FileHandler(filename)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.setLevel(level)
    
    return logger

def page_soup(url):
    """
    Make BeautifulSoup of page
    
    Args:
        url:``str``
            url of page
            
    Returns:
        BeautifulSoup of page:``soup``
        
    """
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")
        return soup
    else:
        raise Exception("Please check website. Error code {}.".format(r.status_code))

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    
    Args:
        string:``str``
            string of sentences

    Returns: 
        Lowercase cleaned string:``str``
    """

    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def top_n(lis, n):
    """Get index of top n item from list with value
    
    Args:
        lis:``list``
            list
        n:``int``
            number of top value
            
    Return:
        dict of top value and index: ``dict``
        
    """
    top = sorted(range(len(lis)), key=lambda i: lis[i], reverse=True)[:n]
    value = [lis[i] for i in top]
    return {'index': top, 'value':value}
