import zipfile
import os
import shutil

import patoolib

from .utils import walk_directory, format_filename

def _zipdir(dir_path, ziph, exclude=None, include=None):
    """
    write file to zip object
    
    Args:
        dir_path:``str``
            parent directory to zip
        ziph:``Zipfile``
            Zipfile from zipfile
        exclude:``list``
            list of file to exclude
        include:``list``
            list of file to include
    
    """
    # ziph is zipfile handle
    files = walk_directory(dir_path)

    for p in files:
        if exclude:
            for f in exclude:
                if f not in p:
                    ziph.write(p)
        elif include:
            for f in include:
                if f in p:
                    ziph.write(p)
        else:
            ziph.write(p)

   
def zip_folder(dir_path, filename=None, exclude=None, include=None):
    """
    zip all file in folder, 

    Args:
        dir_path:``str``
            parent directory to zip
        filename:``str``
            filename of zip file
        exclude:``list``
            list of file to exclude
        include:``list``
            list of file to include
    """
    
    if not filename:
        filename = format_filename(dir_path) + '.zip'

    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    _zipdir(dir_path, zipf, exclude, include)
    zipf.close()

def unzip_file(filename, save_dir='data'):
    """
    unzip all file
    
    Args:
        filename:``str``
            filename of zip file
        sav_dir:``str``
            parent directory to zip
            
    .. warning:: for ``rar`` file type, install ``rar`` and ``unrar``

        .. code-block:: sh

            apt install rar && apt install unrar
    """
    
    # check if save_dir exists  
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    
    if filename[-3:]=='zip':
        zip_ref = zipfile.ZipFile(filename, 'r')
        zip_ref.extractall(save_dir)
        zip_ref.close()
    elif filename[-3:]=='rar':
        patoolib.extract_archive(filename, outdir=save_dir)
        
def parse_path(path, fn_only=False, ext=False, al=True):
    """get the directory from filename,
    
    Args:
        path:``str``
            path of file
        fn_only:``bol``
            get the file name only from path
        ext:``bol``
            split file name into name and extension
        al: ``bol``
            get list of dir and file name
            
    Returns:
        list of value: ``list``
          
    """
    
    dir_ = os.path.dirname(path)
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    
    if fn_only:
        return filename
    elif ext:
        return name, ext
    elif al:
        return dir_, name, ext
    else:
        return dir_
        

def move_file(filename, out_dir):
    """
    move file/dir
    
    Args:
        filename:``str``
            filename of file to be moved or name of dir to be moved
        out_dir:``str``
            output directory
            
    """
    
    # check if out_dir exists
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
        
    shutil.move(filename, out_dir)

def delete_dirs(folder_names):
    """
    delete folder and all its contents
    
    Args: `
        folder_names:`str`` or ``list``
            string or list of folders
    """
    
    if isinstance(folder_names, str):
        shutil.rmtree(folder_names)
        os.makedirs(folder_names)
    elif isinstance(folder_names, list):
        for f in folder_names:
            shutil.rmtree(f)
            os.makedirs(f)
    else:
        raise TypeError("Input should be str or list ")
        
def make_dirs(folder_names):
    """
    make folder if it doesnot exist
    
    Args: 
        folder_names:``str`` or ``list``
            string or list of folders
    """
    if isinstance(folder_names, str):
        if not os.path.exists(folder_names):
            os.makedirs(folder_names)
    elif isinstance(folder_names, list):
        _ = [ os.makedirs(f) for f in folder_names if not os.path.exists(f) ]
    else:
        raise TypeError("Input should be str or list ")
