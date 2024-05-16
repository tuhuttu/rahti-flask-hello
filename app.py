import flask


PAGE = """
<!DOCTYPE html>
<html>
  <body>
    <h1>Hello world</h1>
  </body>
</html>
"""


# Flask app object
app = flask.Flask(__name__)


# Routes
@app.route("/", methods=['GET'])
def home():
    return flask.render_template_string(PAGE,)


# Entry function
def main():
    '''
      Main entry function
    '''

    app.run(port=8080,
            host='0.0.0.0')


if __name__ == "__main__":
    main()
