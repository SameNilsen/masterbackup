import json
from os import walk

f = []
original_path = "/fp/projects01/ec12/mornil/originalACE/localACE/ace/testingresults/ace_run_20260428_121335_nrkquiz_offline/detailed_llm_logs/"
for (dirpath, dirnames, filenames) in walk(original_path):
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
        with open(dirpath+"/"+file) as f:
            d = json.load(f)
            with open(original_path+"outfile.txt", "a") as out:
                out.write("\n\n ------------------------------------------------------------------------------------------------------------------------ \n\n")
                out.write(file + "\n")
                if (d.get("prompt") is not None and d.get("response") is not None):
                    out.write("-->Prompt: \n"+d["prompt"] + "\n\n ------------------------------------ \n\n-->Response:\n" + d["response"] + "\n")
                else:
                    out.write("-->Prompt: \n"+d["prompt"] + "\n\n ------------------------------------ \n\n-->Response:\n" + "RESPONSE IS MISSING." + "\n")
    break
