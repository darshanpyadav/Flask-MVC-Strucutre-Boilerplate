# -*- coding: utf-8 -*-
from src.app import app


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    debug_mode = True
    app.run(debug=debug_mode, host=host, port=port)
