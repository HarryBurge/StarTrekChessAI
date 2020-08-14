# When building this use command: python3 setup.py build_ext --inplace

import pyximport; pyximport.install()
from setuptools import setup, Extension
from Cython.Build import cythonize
import os


dirs = [('bin/AI', False, True),
        ('bin/AI/AI\'s', False, True),
        ('bin/Game', False, True),
        ('bin/Game/ControlLoops', False, True),
        ('bin/Game/Maps', False, True),
        ('bin/Game/Pieces/StarTrekChess', False, True),
        ('bin/Utils', False, True),
        ('bin/Visualliser', False, True),
        ('bin/Visualliser/BoardViews', False, True),
        ('bin/Visualliser/UIs', False, True)]


ext_modules = []

for dir, pyx, py in dirs:
    for root, subdirs, files in os.walk(os.getcwd()):

        # Quick check if in there
        if root.find(dir) != -1:
            
            # Check if they are the ending directorys
            rootstructure = root.split('/')
            filestructure = dir.split('/')
            for i in range(-1, -len(filestructure), -1):
                try:
                    if filestructure[i] != rootstructure[i]:
                        break
                except IndexError:
                    raise RuntimeError('File directory given is wrong')

            else:
                
                for file in files:
                    if file not in ['__init__.py']:
                    
                        if pyx and file.split('.')[-1] == 'pyx':
                            modulelist = dir.replace('/', '.')+'.'+file.split('.')[0]
                            path = dir+'/'+file
                            ext_modules.append(Extension(modulelist, sources=[path]))
                        
                        elif py and file.split('.')[-1] == 'py':
                            modulelist = dir.replace('/', '.')+'.'+file.split('.')[0]
                            path = dir+'/'+file
                            ext_modules.append(Extension(modulelist, sources=[path]))


setup(
    name='StarTrekChess',
    ext_modules=cythonize(ext_modules, language_level = "3"),
)
