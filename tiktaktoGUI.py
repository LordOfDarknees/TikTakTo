from TikTakToClass import TikTakTo
import customtkinter

# Unfinished

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__() # Tbh no idea what it does i think it makes sure only 1 instance can exist
        self.Game = TikTakTo()
        self.title(f"Player {self.Game.current_player} starts!")
        self.geometry("600x600")
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1,2), weight=1)
        self.resizable(False, False)
        self.cell1 =customtkinter.CTkButton(self, text=1, corner_radius=0, command= lambda: self.selection(1))
        self.cell1.grid(row=0, column=0, sticky="nwse", padx=5, pady=5)
        self.cell2 =customtkinter.CTkButton(self, text=2, corner_radius=0, command= lambda: self.selection(2))
        self.cell2.grid(row=0, column=1, sticky="nwse", padx=5, pady=5)
        self.cell3 =customtkinter.CTkButton(self, text=3, corner_radius=0, command= lambda: self.selection(3))
        self.cell3.grid(row=0, column=2, sticky="nwse", padx=5, pady=5)
        
        self.cell4 =customtkinter.CTkButton(self, text=4, corner_radius=0, command= lambda: self.selection(4))
        self.cell4.grid(row=1, column=0, sticky="nwse", padx=5, pady=5)
        self.cell5 =customtkinter.CTkButton(self, text=5, corner_radius=0, command= lambda: self.selection(5))
        self.cell5.grid(row=1, column=1, sticky="nwse", padx=5, pady=5)
        self.cell6 =customtkinter.CTkButton(self, text=6, corner_radius=0, command= lambda: self.selection(6))
        self.cell6.grid(row=1, column=2, sticky="nwse", padx=5, pady=5)
        
        self.cell7 =customtkinter.CTkButton(self, text=7, corner_radius=0, command= lambda: self.selection(7))
        self.cell7.grid(row=2, column=0, sticky="nwse", padx=5, pady=5)
        self.cell8 =customtkinter.CTkButton(self, text=8, corner_radius=0, command= lambda: self.selection(8))
        self.cell8.grid(row=2, column=1, sticky="nwse", padx=5, pady=5)
        self.cell9 =customtkinter.CTkButton(self, text=9, corner_radius=0, command= lambda: self.selection(9))
        self.cell9.grid(row=2, column=2, sticky="nwse", padx=5, pady=5)
    
    def reset(self):
        self.Game = TikTakTo()
        self.title(f"Player {self.Game.current_player}")
    
    def selection(self, field:int):
        won = False
        if self.Game.check_valid(self.Game.check_valid(field)):
            current_player = self.Game.current_player
            match field:
                case 1:
                    self.cell1.configure(text=current_player)
                case 2:
                    self.cell2.configure(text=current_player)
                case 3:
                    self.cell3.configure(text=current_player)
                case 4:
                    self.cell4.configure(text=current_player)
                case 5:
                    self.cell5.configure(text=current_player)
                case 6:
                    self.cell6.configure(text=current_player)
                case 7:
                    self.cell7.configure(text=current_player)
                case 8:
                    self.cell8.configure(text=current_player)
                case 9:
                    self.cell9.configure(text=current_player)
            _field, won = self.Game.external_game(field)
            self.title(f"Player {current_player} ")
        if won:
            self.title(f"{current_player} won! Nice")
            
    
    

if __name__ == "__main__":
    app().mainloop()
        
        