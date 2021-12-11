from PIL import ImageDraw,Image,ImageFont,ImageShow
import bs4
import requests
import peewee
import cv2


headers ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
}
response = requests.get("https://api.ithillel.ua/ua/feed/coachesSection?entryId=16969&cityId=kv",headers=headers)
all_images = bs4.BeautifulSoup(response.text,"html.parser").find_all("img")
dict_of_path_images = {}


for tag in all_images:
    print(tag)
    link = tag.get("data-src")
    text = tag.get("alt")
    print(link)

    if link:
        name = link.split("/")[-1]
        dict_of_path_images[text] = f"external_data/my_photo/{name}"
        with open(f"external_data/my_photo/{name}", "wb") as file:
            file.write(requests.get(link).content)

else:
    print(response.status_code)

database = peewee.SqliteDatabase("external_data/people.db")

class People(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database

People.create_table()

def drow_mustache(path_img,text):
    im = Image.open(path_img)
    im.load()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("external_data/arial.ttf",size=30)
    res = draw.text((10,25),text=text,fill="red",font=font)
    del draw
    im.save(f"external_data/result/{text}.jpg","PNG")






for key,path in dict_of_path_images.items():
    face_cascade = cv2.CascadeClassifier('external_data/haarcascade_frontalface_default.xml')
    img = cv2.imread(path)

    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Преобразовать в изображение в градациях серого
    except cv2.error as exc:
        print(f"FAIL - {path}")
        continue
    face = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10))

    if len(face):
        people_path = f"external_data/result{key}"
        drow_mustache(text=key,path_img=path)
        People.create(name = people_path)









