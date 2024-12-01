import os
import requests

def load_input_from_aoc_website(day):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookie = os.environ.get("AOC_SESSION")
    return requests.get(url, cookies = {"session": cookie}
    ).text