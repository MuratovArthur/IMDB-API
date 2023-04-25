from flask import Flask, request, redirect
import csv
import json

file = open('imdb-movie-data.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

def searchingFilms(category):
    result = []
    for row in rows:
        row[2]=row[2].split(',')
        if category in row[2]:
            inner_dict={}
            for i in range(12):
                if(i==2):
                    row[i]=','.join(row[i])
                    inner_dict[header[i]]=row[i]
                else:
                    inner_dict[header[i]]=row[i]
            result.append(inner_dict)
        else:
            row[2]=','.join(row[2])
    final = json.dumps(result)
    return final


app = Flask(__name__)

@app.route('/', methods=['GET'])
def search():
    if(request.args):
        category = (request.args).get("genre").title()
        return searchingFilms(category)
    else:
        return "No results found"

@app.route('/action')
def action():
    return searchingFilms("Action")

@app.route('/adventure')
def adventure():
    return searchingFilms("Adventure")

@app.route('/comedy')
def comedy():
    return searchingFilms("Comedy")

@app.route('/drama')
def drama():
    return searchingFilms("Drama")

@app.route('/romance')
def romance():
    return searchingFilms("Romance")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)