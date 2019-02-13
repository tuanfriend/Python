from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def oktable():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    # for i in range (len(users)):
    #     tblist = tblist + "<td>{{ users['first_name'] }}</td> <td>{{users['last_name']}}</td> <td>{{users['first_name'] users['last_name']}}</td>"
    #     # fname = users['first_name']
    #     # lname = users['last_name']
    #     tblist = tblist + "</tr>"
    return render_template("table.html",users=users)

if __name__ =="__main__":
    app.run(debug=True)