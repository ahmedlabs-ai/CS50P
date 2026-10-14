import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'<iframe .*src="([^"]+)".*></iframe>', s)
    if match:
        url = match.group(1)
        video_id_match = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11})', url)
        if "youtube.com" in url or "youtu.be" in url:
            if video_id_match:
                return f"https://youtu.be/{video_id_match.group(1) or video_id_match.group(2)}"
    return None

if __name__ == "__main__":
    main()
