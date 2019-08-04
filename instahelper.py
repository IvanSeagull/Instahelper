#pip install instapy-cli

from instapy_cli import client
import datetime #Data

username="Login"  #your login for instagramm
password="Password" #your password for instagramm
text="Text" #text under the post
img="Photo" #the picture you want to post

print("Do you want post it now?   y/n")
answer=input()
if answer==y:
    now = datetime.datetime.now()
    min = now.minute
    day= now.day
    months= now.months
    hour= now.hour


elif answer==n:
    min = int(input("What minute?  "))
    day= int(input('What day?   '))
    months= int(input("What months?   "))
    hour= int(input("What hour?   "))
    now = datetime.datetime.now()
    if day==0:
        day=now.day
    if months==0:
        day=now.month






while True:
    now2 = datetime.datetime.now()
    if now2.hour == hour:
        if now2.minute == min:
            if now2.day == day:
                if now2.minute == min:

                    with client(username, password) as cli:
                        cli.upload(img, text)
                        break
                else:
                    continue
            else:
                continue
        else:

            continue
    else:

        continue
