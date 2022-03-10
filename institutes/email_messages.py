

def account_activation_mail(username, activation_code):
    message = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            

            <style>
                #heading{{
                    font-family: verdana;
                    padding: 20px;
                    background-color: #13a9cf;
                    color: #fff;
                    width: 70%;
                    margin: 0px auto;
                    margin-top: 20px;
                    border: 1px solid #13a9cf;
                    border-top-right-radius: 5px;
                    border-top-left-radius: 5px;
                }}
                
                #msg_box{{
                    font-family: verdana;
                    padding: 20px;
                    font-size: 20px;
                    width: 70%;
                    margin: 0px auto;
                    margin-bottom: 20px;
                    border: 1px solid #13a9cf;
                    border-bottom-right-radius: 5px;
                    border-bottom-left-radius: 5px;
                    padding-left: 40px;
                    padding-right: 0px;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h2 id="heading">ISRDC Jabalpur</h2>
            <div id="msg_box">
                <p>Hi, {}</p>
                <p>
                    Welcome to ISRDC Jabalpur. 
                    Click over the <a href="http://localhost:8000/institutes/activate_account/?username={}&activation_code={}">link</a> to activate your account.
                </p>
                <p>
                    Regards<br>
                    ISRDC Jabalpur Team
                </p>
            </div>
        </body>
        </html>'''.format(username, username, activation_code)

    return message
