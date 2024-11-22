from fastapi import FastAPI
import gradio as gr
from tool import display


app = FastAPI()
@app.get("/")
def read_main():
    return {"message": "This is your main app"}

app = gr.mount_gradio_app(app, display(), path="/main")