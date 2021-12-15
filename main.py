from fastapi import FastAPI

app = FastAPI()
temps = []


@app.get("/")
def read_root():
    return {"Hello": "World"}
    return temps


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
@app.post("/webhook")
def webhook(item):
    print(item)
    return {"success": True}
@app.post("/webhook/uplink")
def uplink(item: dict):
    print(item)
    temps.append(item["uplink_message"]["decoded_payload"])
    return {"success": True}