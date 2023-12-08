import random
from Gamer import Gamer

class Game():

    def __init__(self, cards_gamer1, cards_gamer2):
        self.__cards_gamer1 = cards_gamer1
        self.__cards_gamer2 = cards_gamer2

    # def cards_gamer1Get(self):
    #     return self.__cards_gamer1
    # 
    # def cards_gamer1Set(self):
    #     self.__cards_gamer1 = cards_gamer1
    # 
    # def cards_gamer2Get(self):
    #     return self.__cards_gamer2
    # 
    # def cards_gamer2Set(self):
    #     self.__cards_gamer2 = cards_gamer2

    def menu(self):
        print("\n----- GAME TWENTY-ONE -----")
        print("--- Welcome to the game ---\n")

        while True:
            option = int(input("---- Type one option: ----\n"
                               "[1] Start Game\n"
                               "[2] Finish Game\n"))

            if option == 1:
                game.raffle_cards(gamer1.gamer, gamer1.bet_gamer, gamer2.gamer, gamer2.bet_gamer)
            elif option == 2:
                print("Finish Game...")
                exit()
            else:
                print("Type it the option value\n")
            break

    def raffle_cards(self, gamer1, bet_gamer1, gamer2, bet_gamer2):
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
                      10, 10, 10, 10,
                      10, 10, 10, 10]

        option_gamer1 = 1
        option_gamer2 = 1

        self.__cards_gamer1 += random.choice(cards_game)
        self.__cards_gamer2 += random.choice(cards_game)

        while option_gamer1 == 1 or option_gamer2 == 1:

            print("-------------------------------------------")
            print(f"- CARDS {gamer1}: ", self.__cards_gamer1, f"\n- CARDS {gamer2}: ", self.__cards_gamer2)
            print("-------------------------------------------")

            print(f"---- GAMER {gamer1}: ----")
            option_gamer1 = int(input("Choose on option: \n"
                                      "[1] Put more cards\n"
                                      "[0] Not put more cards\n"))

            print(f"---- GAMER {gamer2}: ----")
            option_gamer2 = int(input("Choose on option: \n"
                                      "[1] Put more cards\n"
                                      "[0] Not put more cards\n"))

            if option_gamer1 == 1 and option_gamer2 == 1:
                gameover_player_one = False
                gameover_player_two = False

                if self.__cards_gamer1 == 21:
                    print(f"GAME OVER!!!\n- {gamer1} -", self.__cards_gamer1)
                    print(f"- {gamer1} - WIN THE GAME! CONGRATULATIONS\n")
                    bet_gamer1 += bet_gamer2
                    print(f"- {gamer1} - WON {bet_gamer1} CHIPS!")
                    break
                else:
                    self.__cards_gamer1 += random.choice(cards_game)

                if self.__cards_gamer2 == 21:
                    print(f"GAME OVER!!!\n- {gamer2} -", self.__cards_gamer2)
                    print(f"- {gamer2} - WIN THE GAME! CONGRATULATIONS\n")
                    bet_gamer2 += bet_gamer1
                    print(f"- {gamer2} - WON {bet_gamer2} CHIPS!")
                    break
                else:
                    self.__cards_gamer2 += random.choice(cards_game)

                if self.__cards_gamer1 > 21:
                    print(f"GAME OVER - {gamer1} -, YOUR PONTUATION IS: {self.__cards_gamer1}")
                    print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}\n")
                    if self.__cards_gamer2 == 21 or self.__cards_gamer2 < 21:
                        print(f"GAME OVER - {gamer1} -, YOUR PONTUATION IS: {self.__cards_gamer1}")
                        print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}")
                    break

                if self.__cards_gamer2 > 21:
                    print(f"GAME OVER - {gamer2} -, YOUR PONTUATION IS: {self.__cards_gamer2}")
                    print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}\n")
                    if self.__cards_gamer1 == 21 or self.__cards_gamer1 < 21:
                        print(f"GAME OVER - {gamer2} -, YOUR PONTUATION IS: {self.__cards_gamer2}")
                        print(f"{gamer1}, YOUR PONTUATION IS: {self.__cards_gamer1}")
                    break

                if self.__cards_gamer1 > 21 and self.__cards_gamer2 > 21:
                    print(f"GAME OVER FOR THE PLAYERS!\n")
                    print(f"GAMER {gamer1} YOUR PONTUAUTION IS: {self.__cards_gamer1}")
                    print(f"GAMER {gamer2} YOUR PONTUAUTION IS: {self.__cards_gamer2}")
                    break

                if gameover_player_one and gameover_player_two:
                    print("GAME OVER FOR THE PLAYERS!!!\n")
                    print(f"GAMER {gamer1} YOUR PONTUAUTION IS: {self.__cards_gamer1}")
                    print(f"GAMER {gamer2} YOUR PONTUAUTION IS: {self.__cards_gamer2}")
                    break

            elif option_gamer1 == 1 and option_gamer2 == 0:
                gameover_player_one = False
                gameover_player_two = False

                if self.__cards_gamer1 == 21:
                    print(f"GAME OVER!!!\n- {gamer1} -", self.__cards_gamer1)
                    print(f"- {gamer1} - WIN THE GAME! CONGRATULATIONS\n")
                    bet_gamer1 += bet_gamer2
                    print(f"- {gamer1} - WON {bet_gamer1} CHIPS!")
                    break
                else:
                    self.__cards_gamer1 += random.choice(cards_game)

                if self.__cards_gamer1 > 21:
                    print(f"GAME OVER - {gamer1} -, YOUR PONTUATION IS: {self.__cards_gamer1}")
                    print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}\n")
                    if self.__cards_gamer2 == 21 or self.__cards_gamer2 < 21:
                        print(f"GAME OVER - {gamer1} -, YOUR PONTUATION IS: {self.__cards_gamer1}")
                        print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}")
                    break

                if gameover_player_one and gameover_player_two:
                    print("GAME OVER FOR THE PLAYERS!!!")
                    break

            elif option_gamer1 == 0 and option_gamer2 == 1:
                gameover_player_one = False
                gameover_player_two = False

                if self.__cards_gamer2 == 21:
                    print(f"GAME OVER!!!\n- {gamer2} -", self.__cards_gamer2)
                    print(f"- {gamer2} - WIN THE GAME! CONGRATULATIONS\n")
                    bet_gamer2 += bet_gamer1
                    print(f"- {gamer2} - WON {bet_gamer2} CHIPS!")
                    break
                else:
                    self.__cards_gamer2 += random.choice(cards_game)

                if self.__cards_gamer2 > 21:
                    print(f"GAME OVER - {gamer2} -, YOUR PONTUATION IS: {self.__cards_gamer2}")
                    print(f"{gamer2}, YOUR PONTUATION IS: {self.__cards_gamer2}\n")
                    if self.__cards_gamer1 == 21 or self.__cards_gamer1 < 21:
                        print(f"GAME OVER - {gamer2} -, YOUR PONTUATION IS: {self.__cards_gamer2}")
                        print(f"{gamer1}, YOUR PONTUATION IS: {self.__cards_gamer1}")
                    break

                if gameover_player_one and gameover_player_two:
                    print("GAME OVER FOR THE PLAYERS!!!")
                    break

            elif option_gamer1 == 0 and option_gamer2 == 0:
                if self.__cards_gamer1 > self.__cards_gamer2:
                    if self.__cards_gamer1 < 21:
                        print(f"- {gamer1} - WIN THE GAME! CONGRATULATIONS!\nYOUR PONTUATION IS: {self.__cards_gamer1}\n")
                        print(f"- {gamer2} - GAME OVER!\nYOUR PONTUATION IS: {self.__cards_gamer2}")
                    elif self.__cards_gamer1 >= 21:
                        print(f"GAME OVER - {gamer1} -. YOUR PONTUATION IS: {self.__cards_gamer1}\n")
                        print(f"- {gamer2} - YOUR PONTUATION IS: {self.__cards_gamer2}")

                elif self.__cards_gamer2 > self.__cards_gamer1:
                    if self.__cards_gamer2 < 21:
                        print(f"- {gamer2} - WIN THE GAME! CONGRATULATIONS!\nYOUR PONTUATION IS: {self.__cards_gamer2}\n")
                        print(f"- {gamer1} - GAME OVER!\nYOUR PONTUATION IS: {self.__cards_gamer1}")
                    elif self.__cards_gamer2 >= 21:
                        print(f"GAME OVER - {gamer2} -. YOUR PONTUATION IS: {self.__cards_gamer2}\n")
                        print(f"- {gamer1} - YOUR PONTUATION IS: {self.__cards_gamer1}")

                elif self.__cards_gamer1 == self.__cards_gamer2:
                    print("DRAW!")
                break

            else:
                print("Invalid Option!")

gamer1 = Gamer()
gamer2 = Gamer()
game = Game(0, 0)

if __name__ == "__main__":
    game.menu()
