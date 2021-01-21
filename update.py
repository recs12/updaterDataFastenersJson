
import json
import os
import pandas as pd

__version__ = "0.0.0"

xslx = ["table.xlsx", "fasteners.xlsx"]
print(xslx)


def update_table(doc):
    excel = pd.read_excel(doc, sheet_name=0)
    excel = excel.applymap(str)
    reindexed = excel.set_index(excel.columns[0])
    json_format_string = reindexed.to_json(orient="index")
    parsed = json.loads(json_format_string)
    content = json.dumps(parsed, indent=4)
    name = os.path.splitext(doc)[0]
    with open(name + ".json", "w") as t:
        t.write(content)
    print("|> %s updated with changes." % doc)


def update_fasteners(doc):
    excel = pd.read_excel(doc, sheet_name=0)
    excel = excel.applymap(str)
    json_format_string = excel.to_json(orient="records")
    parsed = json.loads(json_format_string)
    content = json.dumps(parsed, indent=4)
    name = os.path.splitext(doc)[0]
    with open(name + ".json", "w") as t:
        t.write(content)
    print("|> %s updated with changes." % doc)


def update(f):
    try:
        if os.path.exists(f) and f == "fasteners.xlsx":
            update_fasteners(f)
        elif os.path.exists(f) and f == "table.xlsx":
            update_table(f)

    except FileNotFoundError as fn:
        print(fn.args)


if __name__ == "__main__":
    print(__version__)
    update("table.xlsx")
    update("fasteners.xlsx")
    _ = input("Press any keys to exit...")
