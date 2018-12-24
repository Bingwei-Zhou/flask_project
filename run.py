from flask import Flask, render_template, Blueprint
app = Flask(__name__)
@app.route('/')
def hello():
  return "Hello everyone!"
app.run(debug=True)
