import flask
from flask import request
from main import gen_main, gen_img

app =  flask.Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/verify")
def main():

    gen_main()
    return flask.render_template('index.html', image_to_show='load.png')

@app.route("/generate", methods=["post"])
def gen():
    desc = request.form.get('desc_box_txt')
    style = request.form.get('style_op')

    gen_img(desc, style)
    # call the gen apki
    return flask.render_template('index.html', image_to_show="gen_img.jpeg", prompt = desc)

if __name__ == "__main__":
    app.run(debug=True)