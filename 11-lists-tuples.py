# program to show lists and tuples
# this is a sample code from MIT OCW 18.00

techs = ["TIT", "LNCT", "OIST", "BIST", "SIRT", "JNCT"]
univs = ["RGPV", "SSGITS", "GCE", "BU", "IISER"]

print(techs)

# appending to techs
techs.append("VIT")
print(techs)

print(univs)

univs.extend(["AGTU", "DU"])
print(univs)


bakwas = ["TIT", "VIT"]
for institute in bakwas:
    if institute in techs:
        techs.remove(institute)

print(techs)


all_colleges = univs + techs
print(all_colleges)

gov_univs = ["GCE", "SSGITS", "IISER", "RGPV"]
for univ in gov_univs:
    all_colleges.remove(univ)

print(all_colleges)

