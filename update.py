
import pandas as pd
import json
import os

xslx = ["table.xlsx", "fasteners.xlsx"]
print(xslx)

def update_table(doc):
    excel = pd.read_excel(doc, sheet_name=0)
    reindexed = excel.set_index(excel.columns[0])
    json_format_string = reindexed.to_json(orient="index")
    parsed = json.loads(json_format_string)
    content = json.dumps(parsed, indent=4)
    name = os.path.splitext(doc)[0]
    with open(name + ".json", "w") as t:
        t.write(content)
    print("|> %s updated with changes." %doc)

def update_table(doc):
    excel = pd.read_excel(doc, sheet_name=0)
    pass

def update(f):
    try:
        if os.path.exists(f) and f == "table.xlsx":
            update_table(f)
        elif os.path.exists(f) and f == "fasteners.xlsx":
            print("update fastener is not ready")
            # update_table(f)
    except FileNotFoundError as fn:
        print(fn.args)

update("table.xlsx")
update("fasteners.xlsx")