import API
import calculations
from flask import Flask, redirect, url_for, render_template, request
#SET TAGS IN JSON: idk how they named it so here are the tags in the json file
#Basic: CORE
#Classic: EXPERT1
#Rise Of Shadows: DALARAN
#Saviors Of Uldum: ULDUM
#Descent of Dragons: DRAGONS
#Descent of Dragons(Adventure): YEAR_OF_THE_DRAGON
#Ashes Of Outland: BLACK_TEMPLE
#Demon Hunter Set: DEMON_HUNTER_INITIATE
app = Flask(__name__)
cards = API.create_list()
summonList = ['The Fist of Ra-den', 'Skyfin', 'Chromatic Egg', 'Ysera Unleashed', "Zarog's Crown", 'Bane of Death', 'Dark Prophecy', 'Serpentine Portal', 'Netherwind Portal', \
"Apexis Blast", 'Power Of Creation', 'Big Bad Archmage', "Conjurer's Calling", 'Faceless Lackey', 'Mutate/Witchy Lackey', 'Explosive Evolution']
@app.route("/")
def home():
    return render_template("appList.html", content=summonList)

@app.route("/CalcFrontEnd")
def CalcFrontEnd():
    if request.method == "POST":
        user = request.form["nm"]
    return render_template("CalcFrontEnd.html", methods= ["POST", "GET"])

if __name__ == "__main__":
    app.run(debug=True)

print(calculations.summon(cards, 1, None, 'DEMON', None, 'TAUNT', None, None))













