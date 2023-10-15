import re

def main():
    url = input("URL: ").strip()

    print(f"Username: ", get_username(url))


def search_username(url):
    return re.search(r"^(?:https?://)?(?:www\.)?(?:.+)/([a-z0-9_]+)+$", url, re.IGNORECASE)

def get_username(url):
    if matches := search_username(url):
        return matches.group(1)

if __name__ == "__main__":
    main()
