import re


def make_html(filename):
    out = "<cards>\n"

    for card_str in open(filename):
        s = "<card>"
        winning_nums = [
            n for n in card_str.split("|")[0][card_str.index(":") + 1 :].split(" ") if n
        ]

        card_nums = [n for n in card_str.split("|")[1].split(" ") if n]

        for n in winning_nums:
            s += f"<winning_num_{n}></winning_num_{n}>"
        for n in card_nums:
            s += f"<card_num_{n}></card_num_{n}>"

        rec = "0"
        for i in range(0, 100):
            rec = f"<rec_{i}>{rec}</rec_{i}>"
        s += f"<rec_base>{rec}</rec_base>"
        s += "</card>"
        out += s
    out += "</cards>"

    with open("index.html", "w") as f:
        f.write(f'{out}\n<link rel="stylesheet" href="style.css">')


def make_css():
    css = ""
    for i in range(1, 100):
        css += f"winning_num_{i} ~ card_num_{i} ~ rec_base"
        if i != 99:
            css += ",\n"
    css += "{\n  font-size: calc(20px / 24);\n}\n\n"

    for i in range(1, 100):
        css += f"winning_num_{i} ~ card_num_{i} ~ rec_base rec_{i}"
        if i != 99:
            css += ",\n"
    css += "{\n  font-size: 2em;\n}\n\n"
    print(css)


make_html("input")

make_css()
