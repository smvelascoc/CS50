import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        for var in self.domains:
            for word in self.domains[var].copy():
                if var.length != len(word):
                    self.domains[var].remove(word)
        #raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        modification = False
        if self.crossword.overlaps[x,y]:
            i = self.crossword.overlaps[x,y][0]
            j = self.crossword.overlaps[x,y][1]

            for word1 in self.domains[x].copy():
                for word2 in self.domains[y]:
                    if word1[i] != word2[j]:
                        if word2 == list(self.domains[y])[-1]:
                            self.domains[x].remove(word1)
                            modification = True
                    else:
                        break

        return modification
        #raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs == None:
            arcs = []
            for x in self.domains:
                for y in self.domains:
                    if x != y:
                        arcs.append((x,y))

        while len(arcs) > 0:
            x,y = arcs[0]
            arcs.remove((x,y))
            if self.revise(x,y):
                if len(self.domains[x]) == 0:
                    return False
                for z in (self.crossword.neighbors(x) - {y}):
                    arcs.append((z,x))

        return True

        #raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.crossword.variables:
            if (var not in assignment) or (assignment[var] == None):
                return False
        return True

        #raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for var1 in assignment:
            for var2 in assignment:
                if var1 != var2:
                    # Check all variables are different
                    if assignment[var1] == assignment[var2]:
                        return False
                    #Check all variables lenghts are correct
                    if len(assignment[var1]) != var1.length:
                        return False
                    #Check there is any conflict
                    if self.crossword.overlaps[var1, var2]:
                        i,j = self.crossword.overlaps[var1, var2]
                        if assignment[var1][i] != assignment[var2][j]:
                            return False

        return True
        #raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        order = []
        domain_constraint = []

        for value in self.domains[var]:
            n = 0
            for neightbor in self.crossword.neighbors(var):
                #Checks for the constraint in the domain itself
                if (var not in assignment) and (var in self.domains[neightbor]):
                    n += 1
                #Checks for the constraint in overlapping
                for value2 in self.domains[neightbor]:
                    i,j = self.crossword.overlaps[var,neightbor]
                    if value[i] == value2[j]:
                        n += 1

            # Append the value in domain and its constraint value
            domain_constraint.append((value, n))

        sorted(domain_constraint, key=lambda constr: constr[1])

        for value in domain_constraint:
            order.append(value[0])

        return order
        #raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        p_var = []          #Creates an empty list
        #Check for the variable with the lowest domain lenght
        for var in self.crossword.variables:
            if var not in assignment:
                # Appends in structure : (variable, {Domain, degree})
                p_var.append((var, {"domain": self.domains[var], "degree": len(self.crossword.neighbors(var))}))

        #Sort by domain lenght
        sorted(p_var, key=lambda variable: variable[1]["domain"])

        #Remove all the variables except those with lower domain
        for var in p_var:
            if var[1]["domain"] > p_var[0][1]["domain"]:
                p_var.remove(var)
        #Sorted by
        sorted(p_var, key=lambda variable: variable[1]["degree"], reverse=True)

        return p_var[0][0]
        #raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var=self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None:
                    return result
            assignment.pop(var)
        return None
        #raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
