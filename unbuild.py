
import os
import shutil

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

                    if file.split('.')[-1] in ['c', 'so']:
                        os.remove(root+'/'+file)

shutil.rmtree('build')