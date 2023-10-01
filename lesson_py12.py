import requests
import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.exit()

    number = 50
    
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={number}&term={sys.argv[1]}")
    
#    print(json.dumps(response.json(), sort_keys=True, indent=4))

    o = response.json()
    
    for result in o["results"]:
        print(result["artistName"],result["trackName"], sep=" --- ")
main()
