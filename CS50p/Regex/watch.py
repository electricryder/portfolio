import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"(?:.+)(https?://)(?:www\.)?(youtube\.com)/embed(/\w+)\".+", s):
        output = re.sub("http://", "https://", matches.group(1)) + matches.group(2) + matches.group(3)
        output = converts(output)
        return output


def converts(s):
    s = s.replace("youtube", "youtu")
    s = s.replace(".com", ".be")
    if s.startswith("http://"):
        s.replace
    return s


if __name__ == "__main__":
    main()
