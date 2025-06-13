from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

from fastapi.responses import HTMLResponse #インポート
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>ようこそ！My Webページ</title>
            <style>
                body { font-family: sans-serif; background-color: #f0f0f0; text-align: center; padding-top: 50px; }
                h1 { color: #333366; }
                p { color: #666666; }
            </style>
        </head>
        <body>
            <h1>こんにちは、世界！</h1>
            <p>これはFastAPIで作ったHTMLページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# プレゼント情報を受け取るためのモデル
class Present(BaseModel):
    item: str

@app.post("/present")
async def receive_birthday_present(present: Present):
    return {
        "message": f"🎉 ハッピーバースデー！『{present.item}』をありがとう！お返しにバースデーケーキをどうぞ 🎂"
    }