from flask import *

from test import BookStoreInfo

app = Flask(__name__)

@app.route('/')
def index():  
    return render_template("index.html");

@app.route("/add")  
def add():  
    return render_template("add.html")  

@app.route("/savedetails",methods = ["POST"])
def saveDetails():   
    if request.method == "POST":  
        Regular_Books = request.form.get("Regular Books",0)
        Fiction_Books = request.form.get("Fiction Books",0)
        Novels_Books = request.form.get("Novels Books",0)
        Regular_Days = request.form.get("No of Days for Regular Books",0)
        Fiction_Days= request.form.get("No of Days for Fiction Books",0)
        Novels_Days= request.form.get("No of Days for Novels Books",0)

        rent_books_data = request.form.to_dict()
        book = BookStoreInfo(Regular_Books, Fiction_Books, Novels_Books, Regular_Days, Fiction_Days, Novels_Days )
        book.total_rent = book.rent_calc()
        return render_template("view.html", book=book)
        
if __name__ =='__main__':
    app.run(debug = True)