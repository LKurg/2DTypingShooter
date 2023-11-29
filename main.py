import pygame 
import modules.word_list_generator as generator

pygame.init() 

# CREATING CANVAS 
canvas = pygame.display.set_mode((500, 500)) 

# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
exit = False

word_list = generator.generate_words(5)
print(word_list)
selected_word = None
typed_word = ''
selected_word_index = 0

# Main Game Loop
while not exit:
    keys = pygame.key.get_pressed()
    for word in word_list:
        if selected_word is None and keys[pygame.key.key_code(word[selected_word_index])]:
            selected_word = word
            typed_word += word[selected_word_index]
            selected_word_index += 1
            print("Selected Word: " + selected_word)
            print("Typed Word: " + typed_word)
            break
        
    if selected_word is not None:
        if keys[pygame.key.key_code(selected_word[selected_word_index])] and len(selected_word) != selected_word_index:
            typed_word += selected_word[selected_word_index]
            selected_word_index += 1
            print("Typed Word: " + typed_word)
            
        if typed_word == selected_word:
            print("\'" + selected_word + "\' successfully typed" )
            word_list.remove(selected_word)
            selected_word_index = 0
            typed_word = ''
            selected_word = None

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        pygame.display.update()
    
    
	# for event in pygame.event.get(): 
	# 	if event.type == pygame.QUIT: 
	# 		exit = True
	# 	if event.type == pygame.KEYDOWN:
	# 		if event.key == pygame.key.key_code("a"):
	# 			print("A Key Pressed")
	# pygame.display.update() 
