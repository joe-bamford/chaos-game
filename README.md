# chaos-game
Fractal generator based on a chaos game inside regular polygons. Uses John Zelle's graphics.py module - see https://inst.eecs.berkeley.edu/~cs61a/book/examples/parallel/graphics.py.html.

Run chaos-game to see results. Press Q while running to quit. For information on the game itself see https://en.wikipedia.org/wiki/Chaos_game.

Inputs: - Number of sides, n, determines the border polygon
        - Ratio, r, determines how far towards each vertex to travel with each iteration
        - Enabling the vertex rule (VR) ensures the same vertex can't be chosen twice in a row

Example inputs: (1) n=3, r=0.5 gives a Sierpinski triangle
                (2) n=4, r=0.5 gives a square fractal, with VR enabled
                (3) n=5, r=0.618034 (reciprocal of golden ratio) gives a pentaflake, with VR disabled
                (4) n=5, r=0.55 with VR enabled is my personal favourite
