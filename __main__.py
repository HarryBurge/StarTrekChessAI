from bin import StarTrekChessAI
from os import walk, system, name, mkdir
import time

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


yn = True
while yn:
    clear()
    print('''
----Star Trek Chess AI---------------
1 - Single Game 1 v 1
2 - Single Game 1 v bot
3 - Single Game bot v bot
11 - Visual genetic train bot v bot+1

99 - Exit
-------------------------------------
    ''')
    option = input('>> ')

    if option == '1':
        clear()
        StarTrekChessAI.main_1v1()
    elif option == '2':
        clear()
        StarTrekChessAI.main_1vbot()
    elif option == '3':
        clear()
        StarTrekChessAI.main_botvbot()


    elif option == '11':
        yn2 = True
        while yn2:
            clear()
            print('''
-----Genetic Visual Trainer----------
1 - Verbose train

99 - Back
-------------------------------------
            ''')
            option2 = input('>> ')

            if option2 == '1':
                number_of_boards = int(input('num_of_boards>> '))

                print('----AI options----')
                f = []
                for (dirpath, dirnames, filenames) in walk('bin/AI/AIs'):
                    f.extend(filenames)
                    break
                try:
                    f.remove('__init__.py')
                except:
                    pass

                for index,i in enumerate(f):
                    print(str(index) + ' - ' + i)

                print('------------------')

                ai_paths = ['bin.AI.AIs.'+f[int(input('AI 1>> '))][:-3], 'bin.AI.AIs.'+f[int(input('AI 2>> '))][:-3]]
                ai_save_files = []

                for i in range(len(ai_paths)):
                    print('\n----'+ ai_paths[i].split('.')[-1] + '----')

                    f = []
                    try:
                        mkdir('bin/AI/AIs/' + ai_paths[i].split('.')[-1]+ '_wb')
                    except:
                        pass

                    for (dirpath, dirnames, filenames) in walk('bin/AI/AIs/' + ai_paths[i].split('.')[-1]+ '_wb'):
                        f.extend(filenames)
                        break
                    try:
                        f.remove('__init__.py')
                    except:
                        pass

                    print('0 - None')

                    for index,i in enumerate(f):
                        print(str(index+i) + ' - ' + i)

                    print('-------------------------')

                    temp = int(input('AI 1 Save>> '))
                    ai_save_files.append(None if temp==0 else 'bin/AI/AIs/' + ai_paths[i].split('.')[-1]+ '_wb/' + f[temp-1])
                
                clear()
                StarTrekChessAI.main_botvbot_train_genetic(number_of_boards, ai_paths, ai_save_files, verbose=True)


            elif option2 == '99':
                yn2 = False
            else:
                print('Option chosen is incorrect')
                print('-------------------------------------')
                time.sleep(0.5)


    elif option == '99':
        yn = False
    else:
        print('Option chosen is incorrect')
        print('-------------------------------------')
        time.sleep(0.5)