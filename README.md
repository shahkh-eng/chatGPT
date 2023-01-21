
# Title

Introduction of AI and How OpenAI's ChatGPT can help us develop Python applications faster.


## Authors

- [@khurram javed](https://github.com/shahkh-eng/)

    
## Features

- Create account on openai website
- Generate API Key
- Python Script that will integrate with ChatGPT API
- Integrate Python Flask Code with HTML code for builting your own GUI

## Installation

Install dependencies

```bash
    pip install openai
    pip install flask
```

## Python Script

```python
    from flask import Flask, request, render_template
    import openai
    
    app = Flask(__name__,template_folder="views")
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/get_response', methods=['POST'])
    def get_response():
        input_text = request.form['input_text']
        openai.api_key = "Type your API Key here"
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
```

## References

1: [OpenAI](https://openai.com)

2: [ChatGPT](https://chat.openai.com)

3: [ChatGPT Blog](https://openai.com/blog/chatgpt)
