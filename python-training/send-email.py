#寄送Email的程式
#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="heybear8511@gmail.com"
msg["To"]="dance61199@yahoo.com.tw"
msg["Subject"]="你好"

#寄送純文字的內容
#msg.set_content("測試看看")
#寄送較多樣式的內容(html)
msg.add_alternative("<h3>優惠券</h3>滿五百送一百",subtype="html")

#連線到SMTP Server，驗證寄件人身份並發送郵件
import smtplib
#到網路上搜尋gmail smtp server或yahoo smtp server
server=smtplib.SMTP_SSL["smtp.gmail.com",465]
server.login("heybear8511@gmail.com","輸入密碼")
server.send_message(msg)
server.close()

#測試前記得要去把"低安全性應用程式存取權"打開