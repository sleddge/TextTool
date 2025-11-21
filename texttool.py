#!/usr/bin/env python3
"""TextTool : petit outil en ligne de commande qui applique différentes opérations
sur des chaînes de caractères (uppercase, lowercase, length, count-words, prefix, etc.).
"""



def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "count-words":
        return len(text.split())
    if cmd == "lenght":
	return str(len(text))
    if cmd == "prefix":
	return text[:10]

    if cmd == "count-words":
        return len(text.split())


    return "Unknown command " + cmd



def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
