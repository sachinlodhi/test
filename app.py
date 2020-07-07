from flask import Flask, render_template
from threading import Thread
from selenium import webdriver
app = Flask(__name__)

resp = 'hi'
@app.route('/')
def hello_world():
    global resp
    return render_template("index.html", c = resp)

def selfunc():
    global resp
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    resp = str(driver.page_source)



if __name__ == '__main__':
    t1 = Thread(target = selfunc, name = "t1")
    t1.start()
    app.run()

