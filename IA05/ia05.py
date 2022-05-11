from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("calc-form.html")


@app.route('/compute', methods=['POST'])
def compute():
    # For a POST request to /compute, request.form is a dictionary that contains the posted
    # form data. It should have values for 'number1', 'number2', and 'operator'.
    # Convert 'number1' and 'number2' to floats, and use comparisons of the 'operator'
    # to determine how to compute the result.
    ...
    # After the loop is complete, render the output page. Send values for
    # the numbers, operator, and result:
    numb1 = request.form['number1']
    numb2 = request.form['number2']
    operation = request.form['operator']
    result = 0.0

    num1 = float(numb1)
    num2 = float(numb2)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2

    return render_template("calc-result.html", number1=num1, number2=num2, operator=operation, result=result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)