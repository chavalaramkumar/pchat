from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Sample data for chatbot responses for each programming language
data_arrays = {
    'java': [
        {'question': 'what is the remedies for slow performance', 'answer': 'Increase RAM and optimize code.'},
        {'question': 'print a + b in python sum of two numbers code in python', 'answer': 'a = 10\nb = 20\nprint(a + b)'},
        {'question': 'What is the capital of Germany?', 'answer': 'Berlin'}
    ],
    'python': [
        {'question': 'how to declare a variable in python?', 'answer': 'You can declare a variable by just assigning it a value: x = 10'},
        {'question': 'how to create a function in python?', 'answer': 'def my_function():\n    pass'},
        {'question': 'What is the capital of France?', 'answer': 'Paris'}
    ],
    'c': [
        {'question': 'how to declare a variable in C?', 'answer': 'int x = 10;'},
        {'question': 'how to create a function in C?', 'answer': 'int myFunction() {\n    return 0;\n}'},
        {'question': 'What is the capital of Italy?', 'answer': 'Rome'}
    ],
    'html': [
        {'question': 'how to create a simple HTML page?', 'answer': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Title</title>\n</head>\n<body>\n    <h1>Hello World!</h1>\n</body>\n</html>'},
        {'question': 'what is the basic structure of HTML?', 'answer': 'The basic structure is <!DOCTYPE html><html><head><title></title></head><body></body></html>'},
        {'question': 'What is the capital of Spain?', 'answer': 'Madrid'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    data = request.json
    user_message = data['message']
    active_language = data['language']  # Get the active programming language

    # Get the corresponding data array based on the active language
    data_array = data_arrays.get(active_language, [])

    # Loop through the corresponding data array and return the matching answer
    for element in data_array:
        if user_message.lower() in element['question'].lower():
            return jsonify({"response": element['answer']})

    # Default response if no match found
    return jsonify({"response": 'The data you provided is out of my knowledge. For more info, contact 8343818181 or ping support@technicalhub.io.'})

if __name__ == "__main__":
    app.run(debug=True)
