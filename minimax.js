let aiMoves = 0;

const ALPHA_BETA_PRUNING = true;

function bestMove() {
    let bestScore = -Infinity;
    let move;
    aiMoves = 0;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i][j] == '') {
                board[i][j] = ai;
                let score = minimax(board, 0, false, -Infinity, Infinity);
                board[i][j] = '';
                if (score > bestScore) {
                    bestScore = score;
                    move = { i, j };
                }
            }
        }
    }
    console.log('AiMoves:', aiMoves);
    board[move.i][move.j] = ai;
    currentPlayer = human;
}

let scores = {
    X: 10,
    O: -10,
    tie: 0
};

function minimax(board, depth, isMaximizing, alpha, beta) {
    aiMoves++;
    let result = checkWinner();
    if (result !== null) {
        return scores[result];
    }

    if (isMaximizing) {
        let bestScore = -Infinity;
        let AB_Prune = false;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i][j] == '') {
                    board[i][j] = ai;
                    let score = minimax(board, depth + 1, false, alpha, beta);
                    board[i][j] = '';
                    bestScore = max(score, bestScore);
                    alpha = max(score, alpha);
                    if (beta <= alpha && ALPHA_BETA_PRUNING) {
                        AB_Prune = true;
                        break;
                    }
                }
            }
            if (AB_Prune) {
                break;
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        let AB_Prune = false;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i][j] == '') {
                    board[i][j] = human;
                    let score = minimax(board, depth + 1, true, alpha, beta);
                    board[i][j] = '';
                    bestScore = min(score, bestScore);
                    beta = min(score, beta);
                    if (beta <= alpha && ALPHA_BETA_PRUNING) {
                        AB_Prune = true;
                        break;
                    }
                }
            }
            if (AB_Prune) {
                break;
            }
        }
        return bestScore;
    }
}