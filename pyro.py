from pyrogram import Client
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from threading import Timer
import time
from PIL import Image, ImageDraw, ImageFont

app = Client("my_account")
def bio():
    # try:
    flag_photo = 0
    with app:
        while True:
            # try:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            fnt = ImageFont.truetype('/home/gilas/Documents/pyrogram/first_project_bot/fonts/Ubuntu-BoldItalic.ttf', 150)
            img = Image.new('RGB', (800,600), color = (73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((100,200), current_time, font=fnt,fill=(255,255,0))
            img.save('pil_text.png')
            app.update_profile(bio=current_time)
            app.set_profile_photo(photo='pil_text.png')
            photos = app.get_profile_photos("me")
            if flag_photo == 1:
                app.delete_profile_photos(photos[1].file_id)
            flag_photo = 1
            time.sleep(60)
            # except:
            #     print('😕 ')
            #     time.sleep(30)

app.run(bio())


