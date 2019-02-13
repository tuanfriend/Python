from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<height>/<width>/<color1>/<color2>")

def show_board(height,width,color1,color2):
    board = ""
    print(board)
    for i in range(int(height)):
        for j in range(int(width)):
            if i%2 == 0:
                if j%2 == 0:
                    board += "<div class='color1'></div>"
                if j%2 != 0:
                    board += "<div class='color2'></div>"
            else:
                if j%2 == 0:
                    board += "<div class='color2'></div>"
                if j%2 != 0:
                    board += "<div class='color1'></div>"
        board = board + "<br>"
    return render_template("checkergame.html",board=board,color1=color1,color2=color2)

if __name__ =="__main__":
    app.run(debug=True)