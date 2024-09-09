
# Candy Crush - Combination Detector
## Description
This project is a simplified version of the popular game Candy Crush. The game is played on a grid where players can swap "candies" (represented by random numerical values) to form combinations of three or more. When a combination is made, the candies are removed, and new candies fall to fill the empty spaces.

The objective of the game is to continue playing as long as possible by forming new combinations. The score increases each time a combination is detected and removed.

## Features
* Grid Initialization: Creates an n x n grid with randomly generated candies.
* Horizontal and Vertical Combination Detection: Identifies combinations of three or more identical candies in the grid.
* Candy Swap: Allows players to select and swap two adjacent candies.
* Gravity: After combinations are removed, candies above them fall down, filling the vacant spaces.
* Valid Move Check: Ensures that the two selected candies are adjacent and that the swap results in a valid combination.
* Graphical Display: Visualizes the game grid using the matplotlib library.
## Code Structure
### Main Functions:
* init_jeu(size): Creates a game grid with random candies.
* affichage_grille(grille, nb_type_bonbons): Displays the game grid graphically.
* horizontal(grille) & vertical(grille): Detects horizontal and vertical candy combinations.
* copier_jeu(grille): Creates a copy of the current grid.
* boucher_trous(grille): Fills the empty spaces in the grid with new candies.
* nettoyer(grille): Removes all combinations from the grid before the player begins a new round.
* entrer_coordonnees(jeu): Asks the player to select two candies to swap.
* add_zeros(grille, element_neutre): Adds a border of neutral cells around the grid.
* detect_grille(grille, x, y): Detects candy combinations after a swap.
* grille_jouable(grille): Cleans the grid of existing combinations and prepares it for gameplay.
* permutation(grille, x, y, a, b): Swaps two candies in the grid.
* gravite(grille, L): Applies gravity to the candies after a combination is removed.
* randomly_generated_tab(): Randomly generates a row of candies.
* detecte_coordonnees_combinaisons(L): Checks if a valid combination of three candies has been made.
### Tests:
* test_detecte_coordonnees_combinaison(): Tests several cases to check for candy combinations.
* Installation and Execution
## Prerequisites:
* Python 3.x
* matplotlib library for graphical display.

## Usage
At the start of the game, a grid of candies will be displayed.
You can enter the coordinates of the candies you want to swap, as long as they are adjacent.
If the swap results in a combination, the combination will be removed, candies will fall, and new ones will appear.
The game continues as long as combinations can be made.
