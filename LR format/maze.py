from dataclasses import dataclass

@dataclass
class Maze:
    solution: str
    printable_blank: str
    printable_solution:str
    
    def __post_init__(self):
        for char in self.solution:
            if not char.upper() in ["L","R"]:
                raise ValueError("Incorrectly formatted solution")

if __name__ == "__main__":
    blank = """
END████████████████████████████
   █     █        █           █
█  █  ████  █  ███████  █  ████
█  █     █  █  █        █  █  █
█  ████  █  ████  ████  █  █  █
█              █  █     █     █
█  █  ███████  █  ████  █  █  █
█  █  █     █  █     █  █  █  █
████  █  ████  ████  ██████████
█     █           █           █
█  ██████████  ████  █  █  ████
█  █  █  █  █     █  █  █     █
█  █  █  █  █  ██████████  ████
█           █                 █
█  ████  █  █  ███████  ████  █
█  █  █  █  █  █     █  █  █  █
█  █  ██████████  ████  █  █  █
█     █  █              █  █  █
████  █  █  ████  ████  █  █  █
█     █        █     █     █  
████████████████████████████START
"""
    printable_solution = """
END████████████████████████████
   █     █        █           █
█  █  ████  █  ███████  █  ████
█  █     █  █  █        █  █  █
█  ████  █  ████  ████  █  █  █
█R  R   L  L L █  █     █     █
█  █  ███████  █  ████  █  █  █
█  █  █     █  █     █  █  █  █
████  █  ████  ████  ██████████
█     █      R █              █
█  ██████████  ████  █  █  ████
█  █  █  █  █L    █  █  █     █
█  █  █  █  █  ██████████  ████
█           █R           L  L █
█  ████  █  █  ███████  ████  █
█  █  █  █  █  █     █  █  █  █
█  █  ██████████  ████  █  █  █
█     █  █              █  █  █
████  █  █  ████  ████  █  █  █
█     █        █     █     █  
████████████████████████████START
"""
    m = Maze("LLRLRLLLRR", blank, printable_solution)

    print(f"Maze:\n{m.printable_blank}")
    print(f"Solution is: {m.solution}\n")
    print(f"Annotated maze solution:\n{m.printable_solution}")
