from aiohttp import web
import requests, json, sys
import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def index(request):
    return web.FileResponse('./index.html')

get_url="https://py-pro-i.herokuapp.com/api"

async def get_req():
    r=requests.get(get_url)
    stat_code=r.status_code; print(stat_code)
    text_dat=r.text #; print(text_dat)
    return text_dat
    #json_res=r.json(); res=json_res[0]; print(res)

async def py_dat(req):
    data = await get_req()
    web_res=web.Response(text=data)
    return web_res
    #return web.json_response(data)







app = web.Application()
aiohttp_debugtoolbar.setup(app)
app.add_routes([web.get('/', handle),
                web.get("/index", index),
                web.get("/api", py_dat),
                web.get('/{name}', handle)])




if __name__ == '__main__':
    web.run_app(app)
