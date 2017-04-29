from flask import Flask
import polynanna
app = Flask(__name__)

@app.route('/')
def polyapp():
    polyanna = polynanna.main()
    return str([p.name for p in polyanna.participants])


if __name__ == '__main__':
    app.run()
