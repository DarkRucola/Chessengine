video 1: https://www.youtube.com/watch?v=U4ogK0MIzqk&t=679s
cpw: https://www.chessprogramming.org/Main_Page

0. testing suite
1. Pieces pngs
2. Code repr (king, pawn, knight, bishop, rook, queen 1-6) 0 = none
2.1 white = 8, black = 16

10-110 bit repr - colour-type

3. board repr
4. FEN notation reading
5. direction offsets
6. structure for holding a move
7. something to generate legal moves (care for checks)
8. very much move generation
9. find a realistic depth (6)
10. explore monte-carlo tree search
11. evaluation function
11.1 count material
11.2 ??

12. search function (minimax)
12.1 alpha beta pruning
12.2 move ordering (likely good moves evaluatd first)
12.3 search only captures / only moves that don't lead to a capture

13. zorbist hashing for caching transpositions
14. pieces maps
15. sequential depth searches

16.pull in stockfish evaluation to compare
17. search extension on good moves
18. early game/late game piece evaluation
19. bitboards - repr as bits 
20. advantage for passed pawns, penalty for isolated pawns
21. better legal mov genration (valid positions bitboard)
22. killer moves
23. once you've found a good move keep it as the best and rduce the depth of subsqunt searches, unlss you find a mov that's btter
24. handle repetitions
25. upload the bot on lichess

26. quiescnce sarch - calculat all captures
27. Static valuation xchang
28. montecarlotreesarch

- alpha beta pruning
- qioesnt srch
- move ordring
- tt mnov
- mvv-lva
- two killer movs
- historyhuristics
- transposition tabl
- itrativ deepning
- aspiration windows
- principle variation search
- check extensoins
- pawn move to 2nd/7th rank extension aka passed pawns extensions
- null move pruning
- late move reductions
- reverse futility pruning
- futility pruning
- late move pruning
- internal iterative reductions
- time management with a soft and hard bound
- eval funcotin: piece square tables, king on open file malus, duble pawns malus
- tuner for table positions

https://www.youtube.com/watch?v=Ne40a5LkK6A&t=8s
- PeSTO tables
- texel tuner
- mobility score per piece, per start and endgame
- use shallow searches to improve deep searches
- pricipal variation search
- skip a turn 
- pawns on king side have more value
- negative mobility value to king

- pattern recognition?
