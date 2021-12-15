from fastapi import FastAPI

app = FastAPI()
temps = []


@app.get("/")
def read_root():
    return {"Hello": "World"}
    return temps


@app.get("/items/{item_id}")
def webhook(item):

@app.post("/webhook/uplink")
def uplink(item: dict):
    print(item)
    temps.append(item["uplink_message"]["decoded_payload"])
    return {"success": True}