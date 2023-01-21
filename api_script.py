from flask import Flask, request, render_template
import openai

app = Flask(__name__,template_folder="views")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    input_text = request.form['input_text']
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{input_text}"),
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].text
    return render_template('index.html', input_text=input_text, message=message)

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.2", port=5002, threaded=True)
