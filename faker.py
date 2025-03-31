import json
import random

def createRandomUser():
    # Pick a random number between 1880 and 2023 (inclusive)
    random_year = random.randint(1880, 2023)

    # random gender in array
    random_gender = random.choice(["boy", "girl"])
    gender = "m" if random_gender == "boy" else "f"

    # Load JSON data from the file
    filename = f'{random_year}/{random_gender}_names_{random_year}.json'

    try:
        with open(filename) as f:
            data = json.load(f)

        # Randomly pick a name from the "names" list
        random_name = random.choice(data['names'])

        # Print the randomly selected name

        print(f"Randomly selected name: {random_year}/{random_name}/{gender} ")

        return {
            "birthofyear": random_year,
            "firstname": random_name,
            "lastname": random_name,
            "gender": gender,
        }

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except KeyError:
        print(f"The 'names' key was not found in the data from {filename}.")
    except json.JSONDecodeError:
        print(f"Error decoding the JSON from {filename}.")
        

print(createRandomUser())