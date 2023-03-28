import os
from deta import Deta
from fastapi import FastAPI
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from jinja2 import Template

app = FastAPI()

webcrate_key = os.getenv("WEBCRATE_KEY")

deta = Deta(webcrate_key)

links = deta.Base("links")

@app.get("/")
def html_handler():
    article_html = links.get("8638322465251595-ym309DoXCT")["meta"]["description"]
    home_template = Template((open("index.html").read()))
    home_css = open("style.css").read()
    return HTMLResponse(home_template.render(content=article_html, css=home_css))