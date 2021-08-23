from flask import Flask
from flask import request, Response
import server

app = Flask(__name__)

@app.route('/')
def index():
    src = request.args.get("src", "USD")
    dst = request.args.get("dst", "USD")
    amount = request.args.get("amount", 1)
    result = float('%.2f' % server.converter(float(amount), src, dst))
    str_result = str(amount)+' '+server.find_currency(src)
    str_result_con = str(server.converter(float(amount), src, dst))+' '+server.find_currency(dst)+"""<br/><br/>"""+'Last Update: '+server.date
    print(result)
    return """
    <!DOCTYPE html>
    <html lang="en" style="background-color:black;">
    <head>
        <meta charset="UTF-8">
        <title>Esti Abargel</title>
    </head>
    <body>
        <div class="container" style="border: 3px solid yellow;
                                        background-color: azure; 
                                        width: 95vw;
                                        background-repeat:no-repeats ;
                                        margin-top:7%;
                                        border-radius:15px;
                                        align-items: center;
                                        height: 90vh;
                                        margin: auto;
                                        padding: 10px;
                                        padding-top:5.5vh;
                                        padding-left:5.5vh;
                                        vertical-align: middle;
        ">
            <h1 style="font-size:8vh;
                        font-weight: bold;
                        text-align: center;"
            >😎Welcome to Real Time Currency Convertor😎</h1>
            <div style="background-color: black;
                        color:yellow; 
                        width:25vw;
                        background-repeat:no-repeats;
                        align-items: center;
                        text-align:center;
                        font-size:3vh;
                        font-weight: bold;
                        height:18vh;
                        margin:auto;
                        padding:10px;
                        vertical-align: middle;
                        border:3px solid yellow;
                        border-radius:5px;
            "name="str_result">"""+str_result+"""<br/> equals <br/>"""+str_result_con+"""</div>
            <form method="get">
                <div style="color:black;
                            align-items: center;
                            width:25vw;
                            height:25vh;
                            margin:auto;
                            padding:10px;
                            display:inline-block;
                            position: absolute;
                            top: 55%;
                            left: 35%;
                ">
                    <select name="src" id="src" onchange = "this.form.submit()" name="src" style="display:inline-block;
                                                                                                    font-weight: bold;
                                                                                                    font-size:3vh;
                                                                                                    padding-bottom: 10px;
                                                                                                    border:3px solid yellow;
                                                                                                    border-radius:5px;
                                                                                                    text-align:center;display:
                                                                                                    justify-content: center;
                                                                                                    align-items: center;
                                                                                                    vertical-align: middle;
                                                                                                    background-color:black;
                                                                                                    color:yellow;
                                                                                                    width:5vw;
                                                                                                    height:6vh;
                    ">"""+get_options(src)+""" </select><br/>
                    <input name="amount" style="display:inline-block;
                                                font-weight: bold;
                                                font-size:3vh;
                                                padding-bottom: 10px;
                                                border:3px solid yellow;
                                                border-radius:5px;
                                                text-align:center;display:
                                                justify-content: center;
                                                align-items: center;
                                                vertical-align: middle;
                                                background-color:black;
                                                color:yellow;
                                                width:5vw;
                                                height:4vh;
                    "id="amount" name="amount" type="text" onchange = "this.form.submit()" value="""+str(amount)+""">
                </div>
                <div style="font-size:5vh;
                            display:inline-box;
                            position:absolute;
                            left:44vw;
                            top:58vh;
                            font-weight: bold;
                            font-size:7vh;
                            color:yellow;
                ">convert to</div>
                <div style="color:black;
                                width:25vw;
                                height:25vh
                                align-items: center;
                                align-items: center;
                                margin:auto;
                                padding:10px;
                                display:inline-block;
                                position: absolute;
                                top: 55%;
                                left: 60%;
                ">
                    <select name="dst" id="dst" name="dst" style="display:inline-block;
                                                                    font-weight: bold;
                                                                    font-size:3vh;
                                                                    padding-bottom: 10px;
                                                                    border:3px solid yellow;
                                                                    border-radius:5px;
                                                                    text-align:center;display:
                                                                    justify-content: center;
                                                                    align-items: center;
                                                                    vertical-align: middle;
                                                                    background-color:black;
                                                                    color:yellow;
                                                                    width:5vw;
                                                                    height:6vh;
                    "onchange = "this.form.submit()">"""+get_options(dst)+"""</select><br/>
                    <div name="result" style="display:inline-block;
                                                font-weight: bold;
                                                font-size:3vh;
                                                padding-bottom: 10px;
                                                border:3px solid yellow;
                                                border-radius:5px;
                                                text-align:center;display:
                                                justify-content: center;
                                                align-items: center;
                                                vertical-align: middle;
                                                background-color:black;
                                                color:yellow;
                                                width:5vw;
                                                height:4vh;
                    ">"""+str(result)+"""</div>
                </div>
            </form>
        </div>
    </body>
    </html>
    """

currencies = server.list_currencies
def get_options(current_option):
    c = ""
    for currency in currencies:
        if currency == current_option:
            c += """<option selected>""" + currency + """</option>"""
        else:
            c += """<option>"""+currency+"""</option>"""
    return c


# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8080, debug=True)