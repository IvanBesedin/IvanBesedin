from fastapi import FastAPI

app = FastAPI()
temps = []


@app.get("/")
def read_root():
    return temps

@app.post("/webhook")
def webhook(item):
    print(item)
    return {"success": True}

@app.post("/webhook/uplink")
def uplink(item: dict):
    print(item)
    temps.append(item["uplink_message"]["decoded_payload"])
    return {"success": True}