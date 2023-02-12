import json
from typing import OrderedDict

with open("foods.json", "rt", encoding="UTF8") as file:
    datas = json.load(file)
    newjsons = []
    for data in datas:
        file_data = {}
        if data["model"] == "foods.store":
            file_data["model"] = data["model"]
            file_data["pk"] = data["pk"]
            fields = data["fields"]
            fields.pop("following_users")
            team = fields.pop("team")
            if team == 9:
                team = 3
            fields["stadium"] = team
            file_data["fields"] = fields
            newjsons.append(file_data)


with open("nfoods.json", "w", encoding="UTF8") as outfile:
    json.dump(newjsons, outfile, indent=4, ensure_ascii=False)
