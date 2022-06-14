from invalidassignmentexception import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.word = ''
        self.playing = False
        self.letter = ''
        self.lifes = 5


    def set_word(self, word):
        self.word = str(word)

    def assign(self, letter):
        game = '_ '*len(self.word)
        #for letter in letters:
        if letter not in self.word:
            #display = game.replace(^'_', letter)
            self.lifes -= 1
            raise InvalidAssignmentException
            #return game
        else:
            index = self.word.find(letter)
            game[index].replace('_ ', letter)
            self.letter = letter
            self.playing = True
            return game
        #     for i in self.word:
        #         if self.word[i] != self.word[]
        #         self.word.replace()
            
        # return display

    def show(self):
        if not self.playing:
            game = '_ '*len(self.word)
            return f'Lifes: 5 - Word: {game}'
        else:
            try:
                game = self.assign(self.letter)
                return f'Lifes: 5 - Word: {game}'
            except InvalidAssignmentException:
                return f'Lifes: 5 - Word: {game}'

    def winner(self):
        #winner winner chicken dinner
        if self.lifes <= 0:
            return False
        #elif:

        #try:

        #    self.assign()
                
            