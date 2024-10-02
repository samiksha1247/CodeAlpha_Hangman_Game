import random
word_list=['aaple','banana','cherry','potato','new','bike','car','shirt','angle','python'];


lives=6;


chosen_word=random.choice(word_list);

#print(chosen_word);

print("Guess the word! ")
display=[];
for i in range(len(chosen_word)):
	display+='_';

print(display);


gm_over=False;
while not gm_over:

	print("You have ",lives, " incorrect attempts remaining")
	guess_letter=input("Guess a letter ").lower();



	for position in range(len(chosen_word)):
		letter=chosen_word[position]
		if letter==guess_letter:
			display[position]=guess_letter;
			print("Yehh! Your guess was right ")

	print(display)
	
	if guess_letter not in chosen_word:
		lives-=1
		print('You loss 1 attempt,Guess was incorrect')
		if lives==0:
			gm_over=True;
			print('Game over, you loose the word to guess is ',chosen_word);

	if '_' not in display:
		gm_over=True;
		print('yehhh! You Win');

