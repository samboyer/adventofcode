def make_block(s, id, last, next):
    if next is None:
        next = "null"
    return f"""\
      "{id}": {{
          "opcode": "data_addtolist",
          "next": "{next}",
          "parent": "{last}",
          "inputs": {{ "ITEM": [1, [10, "{s}"]] }},
          "fields": {{ "LIST": ["input_lines", "E`pElDH2j/`9vtKV:X~)"] }},
          "shadow": false,
          "topLevel": false
        }},"""


lines = [(f"node_id_{idx}", l) for idx, l in enumerate(open("input").readlines())]

for i in range(len(lines)):
    if i == 0:
        last = "l3)IDH)}SCN7oz6Cqz|u"
    else:
        last = lines[i - 1][0]

    if i == len(lines) - 1:
        next_id = None
    else:
        next_id = lines[i + 1][0]

    print(make_block(lines[i][1].strip(), lines[i][0], last, next_id))
