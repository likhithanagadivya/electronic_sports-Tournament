from db import get_connection




def add_player():
    name = input("Enter player name: ")
    email = input("Enter email: ")
    game = input("Enter game name: ")
    team = input("Enter team name: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO players
        (player_name, email, game_name, team_name)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, game, team))
    conn.commit()

    print("Player added successfully!")

    cursor.close()
    conn.close()


def view_players():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT player_id, player_name, email,
               game_name, team_name
        FROM players
    """

    cursor.execute(query)

    players = cursor.fetchall()

    print("========== PLAYERS ==========")

    if not players:
        print("No players found.")

    for player in players:
        print(
            f"ID: {player[0]} | "
            f"Name: {player[1]} | "
            f"Email: {player[2]} | "
            f"Game: {player[3]} | "
            f"Team: {player[4]}"
        )

    cursor.close()
    conn.close()


def update_player():
    player_id = input("Enter player ID: ")

    name = input("Enter new player name: ")
    email = input("Enter new email: ")
    game = input("Enter new game name: ")
    team = input("Enter new team name: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE players
        SET player_name = %s,
            email = %s,
            game_name = %s,
            team_name = %s
        WHERE player_id = %s
    """

    cursor.execute(
        query,
        (name, email, game, team, player_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Player updated successfully!")
    else:
        print("Player not found.")

    cursor.close()
    conn.close()


def delete_player():
    player_id = input("Enter player ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        DELETE FROM players
        WHERE player_id = %s
    """

    cursor.execute(query, (player_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Player deleted successfully!")
    else:
        print("Player not found.")

    cursor.close()
    conn.close()



def add_tournament():
    name = input("Enter tournament name: ")
    game = input("Enter game name: ")
    start_date = input("Enter tournament date (YYYY-MM-DD): ")
    prize_pool = input("Enter prize pool: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO tournaments
        (name, game, start_date, prize_pool)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (name, game, start_date, prize_pool)
    )

    conn.commit()

    print("Tournament added successfully!")

    cursor.close()
    conn.close()


def view_tournaments():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            tournament_id,
            name,
            game,
            start_date,
            prize_pool
        FROM tournaments
    """

    cursor.execute(query)

    tournaments = cursor.fetchall()

    print("\n========== TOURNAMENTS ==========")

    if not tournaments:
        print("No tournaments found.")

    for tournament in tournaments:
        print(
            f"ID: {tournament[0]} | "
            f"Name: {tournament[1]} | "
            f"Game: {tournament[2]} | "
            f"Date: {tournament[3]} | "
            f"Prize: ₹{tournament[4]}"
        )

    cursor.close()
    conn.close()




def register_player():
    player_id = input("Enter player ID: ")
    tournament_id = input("Enter tournament ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO registrations
        (player_id, tournament_id, registration_date)
        VALUES (%s, %s, CURDATE())
    """

    cursor.execute(
        query,
        (player_id, tournament_id)
    )

    conn.commit()

    print("Player registered successfully!")

    cursor.close()
    conn.close()


def view_registrations():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            r.registration_id,
            p.player_name,
            p.game_name,
            p.team_name,
            t.name,
            t.game,
            t.start_date
        FROM registrations r
        JOIN players p
            ON r.player_id = p.player_id
        JOIN tournaments t
            ON r.tournament_id = t.tournament_id
    """

    cursor.execute(query)

    registrations = cursor.fetchall()

    print("========== REGISTRATIONS ==========")

    if not registrations:
        print("No registrations found.")

    for r in registrations:
        print(
            f"Registration ID: {r[0]}\n"
            f"Player: {r[1]}\n"
            f"Game: {r[2]}\n"
            f"Team: {r[3]}\n"
            f"Tournament: {r[4]}\n"
            f"Date: {r[5]}"
        )

        print("-" * 40)

    cursor.close()
    conn.close()