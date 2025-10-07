from pathlib import Path

data_directory= Path(__file__).parents[1] / "data" 

with open(data_directory / "quotes_cleaned.txt") as file:
    print(file.read())