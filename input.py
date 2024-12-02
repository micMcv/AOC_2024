import os
import requests

def load_input_from_aoc_website(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookie = os.environ.get("AOC_SESSION")
    return requests.get(url, cookies = {"session": cookie}
    ).text