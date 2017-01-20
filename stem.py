import flask,json
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer

app = flask.Flask('Whisk Stemmer')

@app.route('/init',methods=['POST'])
def init():
  return flask.Response(response='{}',
                        status=200,
                        mimetype='application/json')

@app.route('/run', methods=['POST'])
def main():
    full_params = flask.request.get_json()
    if 'value' in full_params:
      query = full_params['value']['query']
      p = PorterStemmer()
      wn = WordNetLemmatizer()
      res = [z
             for z
             in [wn.lemmatize(y)
                 for y
                 in [p.stem(x)
                     for x
                     in word_tokenize(query)]]
             if z not in string.punctuation]
      
      dict_results = {'result': " ".join(res) }
      json_results = json.dumps(dict_results)
      return flask.Response(response=json_results,
			    status=200,
                            mimetype='application/json')
    else:
      return flask.Response(response=json.dumps({'result': ""}),
			    status=200,
                            mimetype='application/json')
