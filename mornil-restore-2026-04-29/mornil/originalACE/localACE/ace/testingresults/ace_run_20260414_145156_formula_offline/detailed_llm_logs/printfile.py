import json
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\Morten\Masterproject\VS\general\outACEml2_2"):
    print(dirpath)
    liste = []
    newlist = {}
    for file in filenames:
        if file.endswith(".json"):
            newlist[file.split("2026")[1]] = file

    print("\n")
    for key in sorted(newlist.keys()):
        file = newlist[key]
        print("\n\n ------------------------------------------------------------------------------------------------------------------------ \n\n")
        print(file + "\n")
        with open(dirpath+"\\"+file) as f:
            d = json.load(f)
            with open(r"C:\Users\Morten\Masterproject\VS\general\outACEml2_2\outfile.txt", "a") as out:
                out.write("\n\n ------------------------------------------------------------------------------------------------------------------------ \n\n")
                out.write(file + "\n")
                out.write("-->Prompt: \n"+d["prompt"] + "\n\n ------------------------------------ \n\n-->Response:\n" + d["response"] + "\n")
            # print(d["prompt"])
            # print("\n\n ------------------------------------ \n\n")
            # print(d["response"])
    break
