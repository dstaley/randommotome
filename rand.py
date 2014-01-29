import random
import io
from flask import Flask, make_response, redirect, url_for, jsonify, send_from_directory, request
import requests
app = Flask(__name__)

wallpapers = [
    "82PA00000047", "82PA00000046", "82PA00000037", "82PA00000034", "82PA00000033", "82PA00000035", "82PA00000042",
    "82PA00000040", "82PA00000048", "82PA00000038", "82PA00000044", "82PA00000043", "82PA00000045", "82PA00000041",
    "82PA00000036", "82PA00000039", "82PA00000049", "82PA00000050", "82PA00000051", "82PA00000052"]
fronts = ["white", "black"]
accents = {
	"OP100024": "Metallic Blue", "OP100026": "Metallic Silver", "OP100028": "Metallic Yellow", "OP100050": "Metallic Red",
	"OP100049": "Metallic Purple", "OP100027": "Metallic Black", "OP100025": "Metallic Orange"}
backs = {
    "OP100008": "Navy", "OP100014": "Turquoise", "OP100019": "Olive", "OP100003": "Mint", "OP100013": "Royal Blue",
    "OP100009": "Spearmint", "OP100021": "Woven Black", "OP100023": "Woven White", "OP100017": "Cement", "OP100002": "Black",
    "OP100004": "Chalk", "OP100005": "Cherry", "OP100006": "Lemon Lime", "OP100007": "Violet", "OP100015": "Crimson",
    "OP100018": "Blush", "OP100010": "Raspberry", "OP100016": "Cabernet", "OP100012": "Bamboo", "OP100020": "Ebony Finish",
    "OP100011": "Teak Finish", "OP100022": "Walnut Finish"}
base_url = "https://commondatastorage.googleapis.com/mm-af-images-prod/devices_out/FLEXR1_out/655_out/full/%scolor-%s%s%s/composited-image-00000.png"


@app.route('/')
def index():
    """Render the Ember application."""
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/random')
def random_motox():
    """Redirect to a random Moto X image."""
    return redirect(url_for('specific_motox',
                            front=random.choice(fronts),
                            back=random.choice(backs.keys()),
                            accent=random.choice(accents.keys()),
                            wallpaper=random.choice(wallpapers)))


@app.route('/random.json')
def random_motox_json():
    """Return a JSON object with random values."""
    if request.args.get('front'):
        front = request.args.get('front')
    else:
        front = random.choice(fronts)

    if request.args.get('back'):
        back = request.args.get('back')
    else:
        back = random.choice(backs.keys())

    if request.args.get('accent'):
        accent = request.args.get('accent')
    else:
        accent = random.choice(accents.keys())

    if request.args.get('wallpaper'):
        wallpaper = request.args.get('wallpaper')
    else:
        wallpaper = random.choice(wallpapers)
        
    return jsonify({
        "front": front,
        "back": back,
        "accent": accent,
        "wallpaper": wallpaper,
        "url": url_for('specific_motox', front=front, back=back, accent=accent, wallpaper=wallpaper)})


@app.route('/img/<front>/<back>/<accent>/<wallpaper>.png')
def specific_motox(front, back, accent, wallpaper):
    """Render a specific configuration as an image."""
    r = requests.get(base_url % (accent, front, wallpaper, back))
    resp = make_response(r.content)
    resp.headers['Content-Type'] = 'image/png'
    return resp

@app.route('/favicon.ico')
def favicon():
    """I hate favicons."""
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    if "HEROKU" in os.environ:
        app.run()
    else:
        app.run(debug=True)