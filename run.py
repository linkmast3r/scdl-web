from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

os.system("rm -rf music/*")

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/assets/particles.json')
@app.route('/js/particles_app.js')
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
@limiter.limit('5 per minute')
def index():
    return render_template("index.html", title="SoundCloud music downloader")

@app.route('/api', methods=['POST'])
@limiter.limit('5 per minute')
def api():
    try:
        os.system("rm -rf music/*")

        url = request.form.get('url')
        name = request.form.get('button')

        print(name)
        if name == "Download Single File":
    
    
            os.system("scdl -l {} --path music".format(url))

            file = "music/" + os.listdir("music")[0]

            return send_file(file, as_attachment=True)
        elif name == "Download Playlist":
            os.system("scdl -l {} --path music".format(url))
        
            file = os.listdir("music")[0]

            os.system("zip -r music/{}.zip music/{}".format(file, file))

            return send_file("music/{}.zip".format(file), as_attachment=True)
        
        else:
            return render_template("error.html", title="This is WIP")
    except:
        return render_template("error.html", title="An error has ocurred, check if you are using a clean URL or if it is valid.")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
## https://soundcloud.com/badreligion/american-jesus
## https://soundcloud.com/ant0n_admin/sets/tests