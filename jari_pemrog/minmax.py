# ... (existing code)

def minimax(player_main, player_lawan, is_maximizing, depth):
    if depth == 0 or cek0(player_main) or cek0(player_lawan):
        # Calculate the heuristic value of the current state
        return evaluate(player_main, player_lawan)

    if is_maximizing:
        max_eval = float('-inf')
        for move in generate_moves(player_main, player_lawan):
            new_player_main, new_player_lawan = masukan0(move, player_main, player_lawan)
            eval = minimax(new_player_main, new_player_lawan, False, depth - 1)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_moves(player_main, player_lawan):
            new_player_main, new_player_lawan = masukan0(move, player_main, player_lawan)
            eval = minimax(new_player_main, new_player_lawan, True, depth - 1)
            min_eval = min(min_eval, eval)
        return min_eval

def generate_moves(player_main, player_lawan):
    moves = []
    for i in ["R", "L", "P"]:
        for j in ["R", "L"]:
            moves.append((i, j))
    return moves

def evaluate(player_main, player_lawan):
    # Simple evaluation function for demonstration purposes
    return player_main[0] + player_main[1] - (player_lawan[0] + player_lawan[1])

def ai_move(player_main, player_lawan, difficulty):
    if difficulty == "easy":
        return random.choice(generate_moves(player_main, player_lawan))
    elif difficulty == "medium":
        best_score = float('-inf')
        best_move = None
        for move in generate_moves(player_main, player_lawan):
            new_player_main, new_player_lawan = masukan0(move, player_main, player_lawan)
            score = evaluate(new_player_main, new_player_lawan)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    elif difficulty == "hard":
        best_score = float('-inf')
        best_move = None
        for move in generate_moves(player_main, player_lawan):
            new_player_main, new_player_lawan = masukan0(move, player_main, player_lawan)
            score = minimax(new_player_main, new_player_lawan, False, 2)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    else:
        raise ValueError("Invalid difficulty level")

# ... (existing code)

