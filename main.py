# © Liman
# You can freely use this code. 
# You can also edit it. 
# But don't forget to credit me
from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_language(seed, sentence):
    random.seed(seed)
    vowels = ['a', 'e', 'i', 'o', 'u']
    generated_sentence = ""
    
    for letter in sentence:
        if letter.lower() in vowels:
            generated_sentence += random.choice(vowels)
        elif letter.isalpha():
            generated_sentence += random.choice('bcdfghjklmnpqrstvwxyz')
        else:
            generated_sentence += letter
    
    return generated_sentence

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        seed = request.form['seed']
        sentence = request.form['sentence']
        generated_language = generate_language(seed, sentence)
        return render_template('index.html', generated_language=generated_language)
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
