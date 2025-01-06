def main():
    FRANKENSTEIN_PATH = "books/frankenstein.txt"
    contents = read_file(FRANKENSTEIN_PATH)
    wc = count_words(contents)
    chars = count_chars(contents)
    generate_report(FRANKENSTEIN_PATH, wc, chars)
    
def generate_report(path, wc, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found in the document\n")
    for k, v in sorted(chars.items()):
        print(f"The '{k}' character was found {v} times")
    print ("--- End report ---")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(contents):
    return len(contents.split())

def count_chars(contents):
    allowed = 'abcdefghijklmnopqrstuvwxyz'
    chars = {}
    for c in contents.lower():
        if c not in chars.keys():
            if c in allowed:
                chars[c] = 1
        else:
            chars[c] += 1
    return chars


if __name__ == "__main__":
    main()