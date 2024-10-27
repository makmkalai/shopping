from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='kalaidivi143'
app.config['MYSQL_DB']='shopping'
mysql=MySQL(app)

app.secret_key="shoppingapp"

@app.route("/",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        mblno=request.form.get("mobile")
        if mblno:
            cur=mysql.connection.cursor()
            cur.execute("select mobile from shoppinguser where mobile=%s",(mblno,))
            data=cur.fetchone()
            cur.close()
            if data:
                session['username']=mblno
                return redirect(url_for("home"))
            else:            
                cur=mysql.connection.cursor()
                cur.execute("insert into shoppinguser(mobile) values(%s)",(mblno,))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for("signup"))
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/single_shoes1")
def single_shoes1():
    return render_template("singleshoes1.html")

@app.route("/single_shoes2")
def single_shoes2():
    return render_template("singleshoes2.html")

@app.route("/single_shoes3")
def single_shoes3():
    return render_template("singleshoes3.html")

@app.route("/single_shoes4")
def single_shoes4():
    return render_template("singleshoes4.html")

@app.route("/single_shoes5")
def single_shoes5():
    return render_template("singleshoes5.html")

@app.route("/single_shoes6")
def single_shoes6():
    return render_template("singleshoes6.html")

@app.route("/single_shoes7")
def single_shoes7():
    return render_template("singleshoes7.html")

@app.route("/single_shoes8")
def single_shoes8():
    return render_template("singleshoes8.html")

@app.route("/single_shoes9")
def single_shoes9():
    return render_template("singleshoes9.html")

@app.route("/single_shoes10")
def single_shoes10():
    return render_template("singleshoes10.html")

@app.route("/single_shoes11")
def single_shoes11():
    return render_template("singleshoes11.html")

@app.route("/single_shoes12")
def single_shoes12():
    return render_template("singleshoes12.html")






@app.route("/cart1")
def cart1():
    name="Birde Classy Casual Men's"
    price=516
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes1"))
    

@app.route("/cart2")
def cart2():
    name="Casual Shoes"
    price=400
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes2"))

@app.route("/cart3")
def cart3():
    name="ITALIAN KICKS Running Sports"
    price=225
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes3"))
    

@app.route("/cart4")
def cart4():
    name="Grey Bolt Mesh Sports Shoes For Men"
    price=376
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes4"))

@app.route("/cart5")
def cart5():
    name="Density Sports Shoes for Men"
    price=331
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes5"))
    

@app.route("/cart6")
def cart6():
    name="Trending Comfortable Shoes For Men"
    price=317
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes6"))

@app.route("/cart7")
def cart7():
    name="Fashionable Men Sport Shoes"
    price=399
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes7"))
    

@app.route("/cart8")
def cart8():
    name="Gym Sports Shoes For Men"
    price=493
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes8"))

@app.route("/cart9")
def cart9():
    name="Walking Shoes For Men"
    price=269
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes9"))
    

@app.route("/cart10")
def cart10():
    name="Running Shoes For Men"
    price=450
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes10"))

@app.route("/cart11")
def cart11():
    name="Fhonex Sport 99 Black Sports Shoes"
    price=357
    user=session["username"]
    cur=mysql.connection.cursor()  
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes11"))
    

@app.route("/cart12")
def cart12():
    name="Men's Sports Shoes Comfrotable"
    price=324
    user=session["username"]
    cur=mysql.connection.cursor()
    cur.execute("insert into total_shoes(shoes_name,price,total_amt,user) values(%s,%s,%s,%s);",
                (name,price,price,user))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("single_shoes12"))







@app.route("/shopping_cart")
def shopping_cart():
    cur=mysql.connection.cursor()
    cur.execute("select * from total_shoes where user=%s",(session["username"],))
    all=cur.fetchall()
    cur.close()
    sum=0
    for i in all:
        sum=sum+i[3]
    return render_template("cart.html",data=all,total=sum)


@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    cur=mysql.connection.cursor()
    cur.execute("delete from total_shoes where id=%s",(id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("shopping_cart"))


@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("signup"))

if __name__=="__main__":
    app.run(debug=True)