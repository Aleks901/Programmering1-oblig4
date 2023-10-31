import random

# Lite forord her c:
# Dokumentasjonen er ikke nødvendigvis gjort på standard industri metode, de er mere brukt for å kommentere koden underveis.. 
# Var usikker på om vi var nødt til å gjøre hele oppgaven OOP men valgte likevell å forsøke. 
# Takk for et fint semester! Disse obligene har vært morro! 

# Dersom jeg har ting som skal legges til neste gang jeg koder legger jeg de til i TODO under her: (Hvis det fortsatt er noe her så rakk jeg det ikke)
# TODO : Legg til kort verdi for dealer
# TODO : Fiks dokumentasjon..
# TODO : Få meg et liv.. buying gf 100gp..


class Card:
    def __init__(self, card_type: str, card_worth: str) -> None:
        """Kort klassen styrer hvordan et kort skal bygges opp.

        Args:
            card_type (_str_): hjerter, diamant, kløver og spar.
            card_worth (_str_): Kort verdien
        """
        self.card_type = card_type
        self.card_worth = card_worth


    def __str__(self) -> str:
        """
        Returnerer en string med kort verdi og kort type.

        """
        return f"{self.card_worth} of {self.card_type}"


class Deck:
    def __init__(self) -> None:
        """
        Deck klassen lager et nytt deck basert på 4 kort typer og 13 kort verdier.
        Lagt sammen med en simpel for loop som lager Card objekter blir dette totalt 52 Card objekter i et Deck Objekt.
        Klassen har 2 metoder, en som bruker random shuffle for å stokke kortstokken og en som dealer korta med random choice.
        """
        self.cards = []
        self.card_types = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.card_worth = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for card_type in self.card_types:
            for worth in self.card_worth:
                self.cards.append(Card(card_type, worth))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_card(self) -> str:
        get_card = random.choice(self.cards)
        return get_card


class Player:
    """
    Spiller klassen må kunne ha en hånd, man må kunne legge til kort til hånden dersom man hitter.
    Hånden må kunne cleares dersom spillet ender.
    Hånden må kunne kalkuleres med korrekte verdier basert på kort verdier.
    Til slutt må vi bare ha en måte å få informasjon om hånden.
    """
    def __init__(self, name: str) -> None:
        self.hand = []
        self.name = name
        self.chips = 1000
        

    def add_card(self, card: str) -> None:
        self.hand.append(card)

    def clear_hand(self) -> None:
        self.hand = []

    def calculate_hand_value(self) -> int:
        total_value = 0
        num_aces = 0

        for card in self.hand:
            if card.card_worth in ["Jack", "Queen", "King"]:
                total_value += 10
            elif card.card_worth == "Ace":
                num_aces += 1
                total_value += 11
            else:
                total_value += int(card.card_worth)

        while num_aces > 0 and total_value > 21:
            total_value -= 10
            num_aces -= 1

        return total_value

    def get_hand(self) -> str:
        return [str(card) for card in self.hand]

    def __str__(self) -> str:
        return f"{self.name}'s hand: {', '.join(self.get_hand())} (Value: {self.calculate_hand_value()})"


class Dealer:
    """
    Dealer klassen gjør mye av det samme som spiller klassen, men dealer klassen har også en metode som gjør at det ene kortet ikke vises.
    """
    def __init__(self) -> None:
        self.hand = []

    def add_card(self, card: str) -> None:
        self.hand.append(card)

    def clear_hand(self) -> None:
        self.hand = []

    def calculate_hand_value(self) -> int:
        total_value = 0
        num_aces = 0

        for card in self.hand:
            if card.card_worth in ["Jack", "Queen", "King"]:
                total_value += 10
            elif card.card_worth == "Ace":
                num_aces += 1
                total_value += 11
            else:
                total_value += int(card.card_worth)

        while num_aces > 0 and total_value > 21:
            total_value -= 10
            num_aces -= 1

        return total_value

    def reveal_hidden_card(self):
        if len(self.hand) > 1:
            return str(self.hand[1])
        return None

    def get_visible_hand(self) -> str:
        return [str(card) for card in self.hand[1:]]

    def __str__(self) -> str:
        return f"Dealer's hand: {', '.join(self.get_visible_hand())} ({self.calculate_hand_value()})"


class BlackjackGame:
    """
    BlackjackGame klassen er hvor logikken til spillet bygges opp.
    Player turn metoden starter en while løkke som går stegvis igjennom hva som skal skje i spillerens tur.
    - Viser dealerns skjulte kort med reveal_dealer_card metoden fra dealer klassen. 
    - Spør om du vil hitte eller stå med en input prompt
    - Dersom du hitter så bruker jeg add_card metoden fra player klassen
    - Dersom du står så bryter loopen og dersom du går over 21 bryter loopen.
    Dealer turn metoden gjør mye av det samme, bare automatisk.
    - Dersom dealers hånd verdi er mindre enn 17 MÅ dealer trekke.
    Vinner blir funnet ved en rekke if tests i determine winner
    """
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Dealer()
        self.current_bet = 0

    def deal_initial_cards(self) -> None:
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def reveal_dealer_card(self) -> None:
        print("Dealer's visible card:", str(self.dealer.get_visible_hand()[0]))

    def player_turn(self) -> int:
        while True:
            print("______________________________")
            print("Player's Turn!")
            print(self.player)
            self.reveal_dealer_card()
            action = input("Do you want to hit or stand?: [hit], [stand]: ").lower()
            if action == 'hit':
                self.player.add_card(self.deck.deal_card())
                if self.player.calculate_hand_value() > 21:
                    print("Bust! You went over 21.")
                    print("______________________________")
                    break
            elif action == 'stand':
                break
            else:
                print("Invalid input! Try again!")

    def dealer_turn(self) -> None:
        print("______________________________")
        print("Dealer's Turn!")
        print("Dealer's hand:", ", ".join(map(str, self.dealer.hand)))

        while self.dealer.calculate_hand_value() < 17:
            print("Dealer draws another card..")
            print("______________________________")
            self.dealer.add_card(self.deck.deal_card())
            print("Dealer's hand:", ", ".join(map(str, self.dealer.hand)))
            
        print("Dealer stands with a hand value of", self.dealer.calculate_hand_value())
        print("______________________________")

    def determine_winner(self) -> None:
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()

        if player_value > 21:
            return "Dealer"
        elif dealer_value > 21:
            return "Player"
        elif player_value > dealer_value:
            return "Player"
        elif player_value < dealer_value:
            return "Dealer"
        else:
            return "Push (Tie)"

    def play(self) -> None:
        """
        Play metoden er der rekkefølge logikken bestemmes på spillet, og der spillet kjører fra senere.
        Vi starter med en while løkke som spør etter hvor mye spilleren vil gamble.
        Løkken bryter når spilleren har lagt inn et gyldig beløp.
        Så blir hendene til player og dealer cleared, dette er for at det skal gå ann å spille flere runder.
        Så blir kortene delt ut.
        Etterpå det så bruker jeg metoder fra klassene før til å sjekke om kravene til enten et tapt spill eller et vunnet spill har skjedd med hjelp av if tester.
        Til slutt blir potten clearet og du får oppgitt ditt nye beløp.
        Du blir spurt om du vil starte ny runde, hvis du gjør det starter man fra begynnelsen av play metoden igjen.
        Hvis ikke bryter løkken.
        """
        while True:
            print("Welcome to Blackjack!")
            while True:
                get_bet = input(f"How much would you like to bet? (Current Chips: {self.player.chips}): ")
                if get_bet.isdigit() and 0 <= int(get_bet) <= self.player.chips:
                    self.current_bet = int(get_bet)
                    self.player.chips -= self.current_bet
                    break
                else:
                    print("Invalid bet amount. Please enter a valid bet.")

            self.player.clear_hand()
            self.dealer.clear_hand()
            self.deal_initial_cards()

            if self.player.calculate_hand_value() == 21:
                print("Blackjack! Player wins!")
                blackjack_win = self.current_bet * 2 
                self.player.chips += self.current_bet + blackjack_win
            else:
                self.player_turn()
                if self.player.calculate_hand_value() <= 21:
                    self.dealer_turn()
                    winner = self.determine_winner()
                    if winner == "Player":
                        print(f"{winner} wins!")
                        self.player.chips += self.current_bet * 2
                    elif winner == "Push (Tie)":
                        print("Push (Tie) - Bet returned.")
                        self.player.chips += self.current_bet
                    else:
                        print(f"{winner} wins.")
                        
            self.current_bet = 0
            print(f"Your current amount of chips: {self.player.chips}")
            replay = input("Do you want to play again? (y/n): ").lower()
            if replay != 'y':
                break



        """
        If test som brukes for å sjekke om kode arket skal runnes eller ikke.
        Vanligvis dersom man har en klasse eller klasser som her så importeres de til en annen fil.
        Dermed ville denne snutten ikke vanligvis ha vært her, men for oppgavens skyld så ligger den her så koden kan runnes.
        """
if __name__ == "__main__":
    game = BlackjackGame()
    game.play()