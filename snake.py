
#Snake Game

import pygame, sys, random, time

check_errors = pygame.init()

#check for initializing errors

if check_errors[1] > 0:
	print ('pygame not initialized due to errors.')
	sys.exit()
else:
	print ('pygame was initialized succesfully')

#Play Surface
canvas = pygame.display.set_mode((700,400))
pygame.display.set_caption('Arcade SNAKE')
#time.sleep(5)
 
#Colors

red = pygame.Color(255,0,0) #Game over text
green = pygame.Color(0,255,0) # Snake
black = pygame.Color(0,0,0) # Score
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42) # food


#FPS
fps_controller = pygame.time.Clock()

#Important Variables
snake_pos = [100,50]
snake_body = [[100,50],[90,50],[80,50]]
food_pos = [random.randrange(1,70)*10, random.randrange(1,40)*10]
food_spawn = True
direction = 'RIGHT'
change_direction  = direction
score = 0

def game_over():
	my_font = pygame.font.SysFont('monaco', 72) #Gets font and size of font
	GOtext = my_font.render('Game Over!', True, red) # Renders what text to print and the color, using the previous variable that picked the font and its size
	GOrect = GOtext.get_rect() # Turns the printed text into a rectangle
	GOrect.midtop = (350,20) #writes the coordinate of the rectangle
	canvas.blit(GOtext,GOrect) #Puts the text and the rectangle that has the text onto the canvas
	show_score(2)# displays score in the middle
	pygame.display.flip() # updates canvas
	time.sleep(5)
	pygame.quit()
	sys.exit()

def show_score(loc):
	score_font = pygame.font.SysFont('monaco', 25)
	score_text = score_font.render('score:'+str(score), True, black)
	score_rect = score_text.get_rect()
	if loc == 1:
		score_rect.midtop = (650,20)
	elif loc == 2:
		score_rect.midtop = (350,200)

	canvas.blit(score_text, score_rect)
	



#Main Logic

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if event type is a quit type it will quit the game
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN: #if a key is pressed, the following will happen
			if event.key == pygame.K_RIGHT or event.key == ord('d'): #changes direction to right
				change_direction = 'RIGHT'
			elif event.key == pygame.K_LEFT or event.key == ord('a'): #left
				change_direction = 'LEFT'
			elif event.key == pygame.K_UP or event.key == ord('w'): #up
				change_direction = 'UP'
			elif event.key == pygame.K_DOWN or event.key == ord('s'): # down
				change_direction = 'DOWN'
			elif event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	if change_direction == 'RIGHT' and not direction == 'LEFT': #it will not let snake go right, if it is going left, otherwise, it can go right
		direction = 'RIGHT'
	if change_direction == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if change_direction == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if change_direction == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		snake_pos[0] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'UP':
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10


	snake_body.insert(0, list(snake_pos)) # this adds the updated snake head position as a list to the snake body, so the snake body follows the head
	if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]: # if the snake eats the food, the last body rectangle is not removed(size increases)
		score +=1
		food_spawn = False
	else: 
		snake_body.pop() # if it does not eat the good, as it updates the most front position based on snake head, it removed the last position

	if food_spawn == False:
		food_pos = [random.randrange(1,70)*10, random.randrange(1,40)*10] #spawns food again once the food is eaten
		food_spawn = True #he didny put this under the if

	canvas.fill(white)

	for position in snake_body:
		pygame.draw.rect(canvas, green, pygame.Rect(position[0],position[1],10,10)) #loops through the snake body and draws each position using the x and y coordinates of each block


	pygame.draw.rect(canvas, brown, pygame.Rect(food_pos[0],food_pos[1],10,10)) # draws food
	
	#NO BORDERS
	#if snake_pos[0] > 700 or snake_pos[0]<0:
	#	snake_pos[0] = snake_pos[0] % 700
	#if snake_pos[1] > 400 or snake_pos[1] < 0:
	#	snake_pos[1] = snake_pos[1] % 400
	#BORDERS
	if (snake_pos[0] > 700 or snake_pos[0]<0) or (snake_pos[1]>400 or snake_pos[1]<0): #if the snake goes out of the canvas it ends the game
		game_over()

	for block in snake_body[1:]: # the [1:] is used because the first position of the snake body will be the same as the snake head, we want to see if anything else is equivalent to the snakes position
		if block[0] == snake_pos[0] and block[1] == snake_pos[1]:# if any other body position besides the first is the same as the snake pos, then it will end the game
			game_over()

	show_score(1)

	pygame.display.flip()
	fps_controller.tick(21)

