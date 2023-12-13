import random
from Gamer import Gamer

class Game():

    def __init__(self):
        self.players = []
        self.removedPlayers = []

    def menu(self):
        print("\n----- GAME TWENTY-ONE -----")
        print("--- Welcome to the game ---\n")

        self.get_players()

        while True:
            try:
                option = int(input("---- Type one option: ----\n"
                               "[1] Start Game\n"
                               "[2] Finish Game\n"))
            except:
                print("---------------------")
                print("Enter a valid option!")
                print("-------------------\n")
                continue

            if option == 1:
                self.raffle_cards()
            elif option == 2:
                print("Finish Game...")
                exit()
            else:
                print("Type the correct option value\n")

    def get_players(self):
        qtd_gamers = 0
        while qtd_gamers < 2:

            try:
                qtd_gamers = int(input("Enter the number of gamers: \n"))
            except ValueError:
                print("----------------------------------")
                print("This option only accepts integers!")
                print("--------------------------------\n")
                continue

            if qtd_gamers < 2:
                print("--------------------------------------------------------------------------")
                print("The number of gamers is invalid. Enter a number greater than or equal to 2")
                print("------------------------------------------------------------------------\n")

        for i in range(qtd_gamers):
            while True:
                try:
                    name = input(f"Enter the name for Player {i + 1}: \n").upper()

                    if name.isalpha():
                        break
                    else:
                        print("------------------------------")
                        print("Please enter only with letters")
                        print("----------------------------\n")

                except Exception as e:
                    print(f"Error: {e}")

            while True:
                try:
                    bet = int(input(f"Enter the bet for Player {i + 1}: \n"))
                    break
                except ValueError:
                    print("-----------------------------------------")
                    print("Please enter a valid integer for the bet!")
                    print("---------------------------------------\n")
                    continue

            player = Gamer(name, bet)
            self.players.append(player)

    def raffle_cards(self):
        cards_game = [1, 1, 1, 1,
                      2, 2, 2, 2,
                      3, 3, 3, 3,
                      4, 4, 4, 4,
                      5, 5, 5, 5,
                      6, 6, 6, 6,
                      7, 7, 7, 7,
                      8, 8, 8, 8,
                      9, 9, 9, 9,
                      10, 10, 10, 10,
                      10, 10, 10, 10,
                      10, 10, 10, 10]


        while self.players:
            for player in self.players:
                print("-------------------------------------")
                for other_player in self.players:
                    print(f"- CARDS {other_player.name}: {other_player.cards}")
                print("-------------------------------------")

                option = int(input(f"---- {player.name}: ----\n"
                                   "[1] Put more cards\n"
                                   "[0] Not put more cards\n"))

                while option not in [0, 1]:
                    print("Invalid Option! Please choose again.")
                    option = int(input(f"---- {player.name}: ----\n"
                                       "[1] Put more cards\n"
                                       "[0] Not put more cards\n"))

                if option == 1:
                    player.cards += random.choice(cards_game)
                elif option == 0:
                    continue

                if player.cards > 21:
                    print("---------------------------------------------------------------")
                    print(f"{player.name} has {player.cards} cards and is out of the game.")
                    print("---------------------------------------------------------------")

                    self.removedPlayers.append(player)
                    self.players.remove(player)

                    if len(self.players) == 1:
                        if player.cards < 21:
                            total_bets = sum(player.bet for player in self.removedPlayers)
                            if total_bets > 0:
                                winner = self.players[0]
                                winner.bet += total_bets
                                print("--------------------------------------------------------------------------------------------")
                                print(f"The winner is {winner.name} with a total bet of {winner.bet} chips and {winner.cards} carts")
                                print("--------------------------------------------------------------------------------------------")
                            else:
                                print("///")
                                print("No winner this time.")

                            game.menu()

                        else:
                            total_bets = sum(player.bet for player in self.removedPlayers)
                            if total_bets > 0:
                                winner = self.players[0]
                                winner.bet += total_bets
                                print("--------------------------------------------------------------------------------------------")
                                print(f"The winner is {winner.name} with a total bet of {winner.bet} chips and {winner.cards} carts")
                                print("--------------------------------------------------------------------------------------------")
                            else:
                                print("---")
                                print("No winner this time.")

                            game.menu()
                    break

                if player.cards == 21:
                    total_bets = sum(player.bet for player in self.removedPlayers)
                    if total_bets > 0:
                        winner = self.players[0]
                        winner.bet += total_bets
                        print("--------------------------------------------------------------------------------------------")
                        print(f"The winner is {winner.name} with a total bet of {winner.bet} chips and {winner.cards} carts")
                        print("--------------------------------------------------------------------------------------------")
                    else:
                        print("===")
                        print("No winner this time.")

                    game.menu()

        print("-------------------------------------------------")
        print("All players are out of the game. Ending the game.")
        print("-------------------------------------------------")
        exit()

if __name__ == "__main__":
    game = Game()
    game.menu()