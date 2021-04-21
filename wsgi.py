from view import app  # imports app to run the app routes from view

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5000')  # main run engine of website
# runs on LAN with port 8080