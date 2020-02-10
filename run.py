from datax import create_app

app = create_app()

# runs the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
