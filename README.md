# AI_Map_Adjacency

Two files:

RHC: Randomized Hillclimbing algorithm

CSP: Coloring Constraint Satisfaction Problem
Algorithm based on backtracking to assign colors to regions so that each region does not border another region with the same color.

This code uses are very basic recursive algorithm for backtracking. It checks if a color assignment for a specific vertex will contradict any current assignment, if not the color is assigned, and the algorithm moves on to coloring the next vertex. This continues until all vertices are colored or it is impossible to color the remaining vertices. If the impossible state is reached, the algorithm invalidates the last successful color assignment and attempts to continue with the next color possibility. 

```
CSP(country_border_table):
  While # of vertices in graph != # of vertices colored successfully:
     If all vertices are accounted for:
        Return answer array
	   Load next vertex
     For all colors in range:
        If color is safe to add to vertex:
            Add color assignment to answer array
			      Recursively call CSP solver for next line
		    Else:
			      Try next color
```
