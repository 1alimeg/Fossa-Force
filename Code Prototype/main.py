from website import create_app

# remember that the __init__.py file within the website folder allows the website folder to be a python package...
# that is why you can just write the above import statement

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    
