table = {"python":"Guido van Rossum", "perl":"larry wall", "tcl":"john ousterhout" }
print(table)

print("\t")

table = {"python":"Guido van Rossum", "perl":"larry wall", "tcl":"john ousterhout" }

language = "perl"  #cannot someone easily access over information through dictionery
creator = table[language]
print(creator)

print("\t")

for lang in table.keys():
    print(lang, "\t", table[lang])