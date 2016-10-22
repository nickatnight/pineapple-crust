from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
    c = map(chr, range(97, 123))
    if request.method == 'POST':
        term = request.form['srch_term']
        es = Elasticsearch()
        query = es.search(index="music", body={"size": 80, "query":
                                                {"prefix":{"artist":term}}})
        return render_template('search.html', music=query)

    es = Elasticsearch(['http://es:9200'])
    query = es.search(index="music", body={"size": 80, "query":
                                                {"match_all":{ }}})

    return render_template('home.html', chars=c, music=query)

@application.route('/<title_letter>')
def index(title_letter):
    c = map(chr, range(97, 123))

    es = Elasticsearch(['http://es:9200'])
    query = es.search(index="music", body={"size":80, "query":
                                           {"prefix":{"artist": title_letter}}})
    
    return render_template('index.html', music=query, chars=c)

@application.route('/search')
def search():
    query = None
    return render_template('search.html')

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
