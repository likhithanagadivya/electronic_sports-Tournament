from tournament import (
    add_player,
    view_players,
    update_player,
    delete_player,
    add_tournament,
    view_tournaments,
    register_player,
    view_registrations
)


def player_menu():

    while True:

        print("\n========== PLAYER MENU ==========")
        print("1. Add Player")
        print("2. View Players")
        print("3. Update Player")
        print("4. Delete Player")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_player()

        elif choice == "2":
            view_players()

        elif choice == "3":
            update_player()

        elif choice == "4":
            delete_player()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def tournament_menu():

    while True:

        print("\n======= TOURNAMENT MENU =======")
        print("1. Add Tournament")
        print("2. View Tournaments")
        print("3. Register Player")
        print("4. View Registrations")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_tournament()

        elif choice == "2":
            view_tournaments()

        elif choice == "3":
            register_player()

        elif choice == "4":
            view_registrations()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def main():

    while True:

        print("\n")
        print("=" * 45)
        print("     E-SPORTS TOURNAMENT SYSTEM")
        print("=" * 45)

        print("1. Player Management")
        print("2. Tournament Management")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            player_menu()

        elif choice == "2":
            tournament_menu()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()