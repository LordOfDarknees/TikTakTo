import os
from time import sleep

class TikTakTo:
    def __init__(self) -> None:
        self.field = [1,2,3,4,5,6,7,8,9]
        self.players = ["x", "o"]       # Only 2 Players allowed
        self.current_player = self.players[0]
        
    def start_terminal_game(self, break_after_win:bool):
        """
        This will start a terminal tiktakto game.
        """
        if break_after_win:
            self.drawBoard()
            print(f"Player {self.current_player} choose a Number where you wanna place your Mark!")
            choosen_field = self.get_valid_input()
            self.field[choosen_field-1] = self.current_player
            self.switch_player()
            self.check_winner(silent=False)
            return
        
        while True:
            self.drawBoard()
            print(f"Player {self.current_player} choose a Number where you wanna place your Mark!")
            choosen_field = self.get_valid_input()
            self.field[choosen_field-1] = self.current_player
            self.switch_player()
            self.check_winner(silent=False)
            
            
    def external_game(self, choosen_field:str):
        """
        Note: First player is self.players[0] (Default "x")

        Args:
            input (str): the field your choosing
        """
        self.field[choosen_field-1] = self.current_player
        self.switch_player()
        won = self.check_winner(silent=True)
        return self.field, won
        
        
        
    def switch_player(self):
        index = self.players.index(self.current_player)
        self.current_player = self.players[1-index] # Switches to Second player
        # print(self.current_player)
    
    @staticmethod
    def clear_consol():
        command = "clear"
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)
        
        #return print("\n"*100)
        
    def drawBoard(self, clear:bool=True) -> None:
        if clear:
            self.clear_consol()
            
        _board = f"{self.field[0]} | {self.field[1]} | {self.field[2]}\n"\
                f"--+---+--\n"\
                f"{self.field[3]} | {self.field[4]} | {self.field[5]}\n"\
                f"--+---+--\n"\
                f"{self.field[6]} | {self.field[7]} | {self.field[8]}"
        print(_board)
    
    def get_valid_input(self) -> int:
        while True:
            _chosen_field = self.get_input()
            if self.check_valid(_chosen_field):
                return _chosen_field
            print("Please use a valid number!")
    
    @staticmethod
    def get_input() -> int:
        while True:
            _user_choice = input("--> ")
            try:
                _choice = int(_user_choice)
            except ValueError:
                print("Only numbers are allowed!")
            else:
                return _choice
        
    def check_valid(self, field_number) -> bool:
        if field_number in self.field: # Inisde the field are stored numbers so if a number has been picked it would be an x/o so by checking if the number is we know it isnt used
            return True
        return False
    
    def chunks(self, xs):
        n = 3
        res = [xs[i:i+n] for i in range(0, len(xs), n)]
        return res
    
    def chunk_field(self) -> list[list]:
        n = 3
        string = ""
        for x in self.field:
            string += str(x)
        return [string[i:i+n] for i in range(0, len(string), n)]
    
    def check_lists_for_winner(self, field_list: list[list]):
        for s in field_list:
            if all(x == s[0] for x in s):
                winner = s[0]
                return winner
    
    def check_horizontal(self):
        field = self.chunk_field()
        return self.check_lists_for_winner(field)
    
    def check_vertical(self):
        liste = [[], [], []]
        chunks:list = self.chunk_field()
        for x in chunks:
            for b in x:
                index = x.index(b)
                liste[index].append(b)
        return self.check_lists_for_winner(liste)
    
    def check_diagonal(self):
        # There are only 2 Diagonal Patterns so im lazy
        liste = [[self.field[0], self.field[4], self.field[8]],[self.field[2], self.field[4], self.field[6]]]
        return self.check_lists_for_winner(liste)
            
    def reset_board(self):
        self.field = [1,2,3,4,5,6,7,8,9]
        self.current_player = self.players[0]
        
    def winner_msg(self, winner):
        msg = f"\n\n\n{winner} has won!\n\n\n"
        self.clear_consol()
        print(msg)
        sleep(3)
    
    def check_winner(self, silent:bool):
        horizontal = self.check_vertical()
        vertical = self.check_horizontal()
        diagonal = self.check_diagonal()
        
        if not horizontal == None:
            if silent:
                return True
            self.winner_msg(horizontal)
            self.reset_board()
                
        elif not vertical == None:
            if silent:
                return True
            self.winner_msg(vertical)
            self.reset_board()

        elif not diagonal == None:
            if silent:
                return True
            self.winner_msg(diagonal)
            self.reset_board()
            
            
if __name__ == "__main__":
    game = TikTakTo()
    game.start_game()
