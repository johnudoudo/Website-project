from website import Create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)