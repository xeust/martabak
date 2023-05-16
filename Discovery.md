---
app_name: "Martabak"
title: "Turn a note on WebCrate into a website."
tagline: "Turn a note on WebCrate into a website."
theme_color: "#f3e6b1"
git: "https://github.com/xeust/martabak"
---

Martabak turns a note for a link in WebCrate's into a website.

To use Martabak, you need to set two configuration variables: 
1. create a Data Key for your WebCrate instance and insert it into Martabak's `WEBCRATE_KEY` configruation variable. 
2. Select the `id` of the link with the note you want to turn into a website and insert it into the `LINK_ID` configuration variable.

You can get the `id` of any WebCrate link in the URL of the link in WebCrate, or by visiting your WebCrate's data, opening up the "links" Base, and selecting the `id` of a link.