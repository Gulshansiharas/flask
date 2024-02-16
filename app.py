from flask import Flask
# initializing
app=Flask(__name__)
# Creating url we use the below command
@app.route('/Gulshan')
def index():
    return 'Hello,World!'
if __name__ == '__main__':
    app.run(debug=True)
