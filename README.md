# chaos-game
Fractal generator based on a chaos game inside regular polygons.
> Run chaos-game to see results. Press Q while running to quit. For information on the game itself see https://en.wikipedia.org/wiki/Chaos_game.

# Requirements
- John Zelle's graphics.py module - for download and information see https://mcsp.wartburg.edu/zelle/python/. Put both .py files in the same directory.


# Inputs 
- Number of sides, n, determines the border polygon
- Ratio, r, determines how far towards each vertex to travel with each iteration
- Enabling the vertex rule ensures the same vertex can't be chosen twice in a row

# Example inputs 
- n=3, r=0.5 gives a Sierpinski triangle
- n=4, r=0.5 gives a square fractal, with the vertex rule enabled
- n=5, r=0.618034 (reciprocal of golden ratio) gives a pentaflake, with the vertex rule disabled
- n=5, r=0.55 with the vertex rule enabled is my personal favourite
