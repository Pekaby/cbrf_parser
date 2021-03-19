from  lib.get.web_request import web_request
from  lib.parser.parser import pa
import requests
from gi.repository import Notify

request = web_request()
response = request.get()

print(request.get_status_code())

parser = pa(request.html_text())

parser.find_by_code('840')

Notify.init("Pekaby App")

Notify.Notification.new(
    "It's time to course!",
    parser.get_name() + ': ' + parser.get_course(),
    "/home/dtron/image.png"
).show()
print(parser.get_course())

