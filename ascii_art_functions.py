def mountain_range():
	print(r"""
                  /\                       /\                        /\                       /\
                 /  \                     /  \                      /  \                     /  \
                /    \   /\      /\      /    \   /\               /    \   /\      /\      /    \   /\
               /      \ /  \    /  \    /      \ /  \             /      \ /  \    /  \    /      \ /  \
              /  /\    /    \  /    \  /  /\    /    \    /\     /  /\    /    \  /    \  /  /\    /    \
             /  /  \  /      \/      \/  /  \  /      \  /  \   /  /  \  /      \/      \/  /  \  /      \
            /  /    \/ /\     \      /  /    \/ /\     \/    \ /  /    \/ /\     \      /  /    \/ /\     \
           /  /      \/  \/\   \    /  /      \/  \/\   \     /  /      \/  \/\   \    /  /      \/  \/\   \
       ___/__/_______/___/__\___\__/__/_______/___/__\___\___/__/_______/___/__\___\__/__/_______/___/__\___\___
	""")


def character_selection_horse_and_knight():
	    print(r"""

                 ,;~;,                                                                ,;;,.
                    /\_                                                              /~\
                   (  /                                                             ([-])
                   (()      //)                                                   ,_.~~~.
                   | \\  ,,;;'\                                                 ()--|   ,\
               __ _(  )m=(((((((((((((================--------               ,_//   |   |>)
              /'  ' '()/~' '.(, |                                         (~'  m''~)(   )/
           ,;(      )||     |  ~                                           \(~||~)/ //~\\
          ,;' \    /-(.;,   )                                                 ||   ()   ()
         ,;'   ) /       ) /                                                  ||   ()   ()
               //         ||                                                  ||   ||   ||
               )_\         )_\                                                || ,;.)   (.;,
    	""")


#def pickle_load():
	#while True:
		#try:
			#save_game_name = input('\n > character file name: ')
            #type('\n > loading character...\n')
            #w(1)
            #save_game_load = save_game_name + '.pickle'
            #pickle_in = open(save_game_load,"rb")
            #character_save = pickle.load(pickle_in)
            #type(' > character loaded successfully\n')
            #w(0.3)
            #print('\n > welcome back',character_save['name'],'!')
            #w(0.3)
            #type(' > here are your stats from last time:\n ')
            #w(0.3)
            #print('\n >',character_save)
            #break
        #except:
            #type(' > could not find a file with name')
            #type(save_game_name)

#def pickle_save():
    #w(0.5)
    #print('\n > we should now save your character if you want to come back to it later: ')
    #save_game_name1 = input(' > desired name of file: ')
    #save_game_name12 = save_game_name1 + '.pickle'
    #pickle_out = open(save_game_name12,"wb")
    #pickle.dump(character_save, pickle_out)
    #print('\n > saving character...')
    #w(1)
    #print(' > character saved successfully')
    #pickle_out.close()

def screen_line():
	print(' _____________________________________________________________________________________________________________________')
