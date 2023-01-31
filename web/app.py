"""
John Doe's Flask API.
"""

from flask import Flask,send_from_directory,abort
import configparser
import os

app = Flask(__name__)

@app.route("/<path:request>")
def hello(request):
    #return "UOCIS docker demo!\n"
    if os.path.exists('pages/' + request):
        return send_from_directory('pages/',request),200
    elif '~' in request or '..' in request:
        abort(403)
    else:
        abort(404)


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/','403.html')
@app.errorhandler(404)
def not_found(e):
    return send_from_directory('pages/', '404.html')




def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config


if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    app.run(debug=config["SERVER"]["DEBUG"], host='0.0.0.0', port = config["SERVER"]["PORT"])

    

    

    