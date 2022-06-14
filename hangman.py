from invalidassignmentexception import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.word = ''
        self.playing = False
        #self.letter = ''
        self.lifes = 5
        self.guessed_letters = []
        self.contador = 0


    def set_word(self, word):
        self.word = str(word.lower())

    def assign(self, letter):
        letter = letter.lower()
        # game = '_ '*len(self.word)
        if letter not in self.word:
            #display = game.replace('_', letter)
            self.lifes -= 1
            self.guessed_letters.append(letter)
            raise InvalidAssignmentException
            #return game
        else:
            if letter in self.word:
                c = self.word.count(letter)
                self.contador += c
                indices = [i for i, x in enumerate(self.word) if x == letter]
                #me confundio la manera de mostrar cuando vas adivinando letras


    def show(self):
        if not self.playing:
            game = '_ '*len(self.word)
            return f'Lifes: {self.lifes} - Word: {game}'
        else:
            try:
                game = self.assign(self.letter)
                return f'Lifes: {self.lifes} - Word: {game}'
            except InvalidAssignmentException:
                return f'Lifes: {self.lifes} - Word: {game}'

    def winner(self):
        # winner winner chicken dinner
        if self.lifes <= 0:
            return False
        elif self.contador == len(self.word):
            return True
        else:
            return False

    def play(self):
        if self.winner:
            return 'Ganaste'
        else:
            return 'Perdiste'
                
            