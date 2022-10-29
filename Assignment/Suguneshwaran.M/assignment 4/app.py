import Flask

@app.route('/register', methods =["GET", "POST"])
def register():
    if request.method == "POST":
       
       email = request.form.get("email")
       password = request.form.get("password")
      
       return(
        "<div style='background-color: teal; padding:20px;border-radius: 10px; color: white'>"
        
        "<p>Email: "+email+"</p>"
        "<p>password: "+password+"</p>"
        "</div>"
       )
    return render_template('register.html')

if _name_ == '_main_':
    app.run(debug=True)