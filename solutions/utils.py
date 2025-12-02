from pathlib import Path

def load_input(day: int) -> str:
    """
    Load the input file for a given day.
    Example: day=1 will load 'input/day01.txt'
    """
    base = Path(__file__).resolve().parent.parent
    path = base / "input" / f"day{day:02d}.txt"
    return path.read_text().strip()