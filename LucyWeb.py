from flask import Flask, render_template

lucy = Flask(__name__)

@lucy.route("/")
def start_func():
    return render_template('LucyWeb.html')

if __name__=='__main__':
    lucy.debug = True
    lucy.run()