import os, csv, sys, json


#os.chdir("/storage/emulated/0/AppProjects/Drag_n_Drop/")

def grab_csv(csvfilename):
    json_dict = {}
    with open(csvfilename, "rb") as csvfile:
        reader = csv.DictReader(csvfile)
#        headers = reader[0].keys()
#        print headers
        rowcount = 0
        for row in reader:
            for key in row.keys():
                if rowcount == 0 and row[key] != "":
                    json_dict[key] = [row[key]]
                elif row[key] != "":
                    json_dict[key].append(row[key])
            rowcount += 1
        return json_dict
def write_json(csvfilename, json_dict):
    json_filename = csvfilename.replace(".csv",".json")
    with open(json_filename, "w") as fp:
        fp.write("var lessonname = '" + csvfilename.replace(".csv","") + "';")
        fp.write("var lesson = ")
        json.dump(json_dict, fp, indent=4)
    return json_filename

def write_html(json_filename):
    html_filename = json_filename.replace(".json", ".html")
    #Open orignial drag_n_drop.html
    html_contents = ""
    with open("drag_n_drop2.html", "r") as fp:
        html_contents += fp.read()
    #Point to json file in same folder
    json_link = json_filename.split("/")[1]
    html_contents = html_contents.replace("examplelesson.json", json_link)
    with open(html_filename, "w") as fp:
        fp.write(html_contents)


if __name__ == '__main__':
    filename = "Unit 1 - in, un, dis, mis.csv"
    write_json(filename, grab_csv(filename))
