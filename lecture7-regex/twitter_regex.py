import re

url = input ("url: ").strip()

# re.sub is more of cleaning up user data in csv
# re.search - more conditional to allow acceptable answer

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

