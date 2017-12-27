# HTTP-Server
Basic HTTP Server with a feature to invoke an OS shell in the dir the files are being served from.

I was in need of a quick HTTP-Server for a project I am working on at the time of this post. Of course with Python you could use the one-liner `python -m SimpleHTTPServer`. However I figured my server could use some more features, for convenience sake I have added the option to invoke an OS shell in the directory your files are being served from. This is done so that you can easily move or copy the files you'd like to serve into the relevant directory. I have also added the option to define a host and port of your choosing but a default setting of `127.0.0.1:8000` is included as well.

## Usage

Place the `server.py` file into the directory you wish to serve files from. Start it from the command line and simply answer the prompts. When the server is configured it will start serving the files in said directory.

### Dependencies

For this to work you will need the `SimpleHTTPServer` and `blessings` modules.
