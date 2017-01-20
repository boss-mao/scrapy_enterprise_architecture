import random
import string
from scrapy.utils.python import to_bytes


def multpart_encode(form_data):
    _boundary = to_bytes(''.join(
        random.choice(string.digits + string.ascii_letters) for i in range(20)))
    content_type = "multipart/form-data; boundary=" + _boundary

    body = []
    for name, value in form_data.items():
        body.append(b'--' + _boundary)
        body.append(b'Content-Disposition: form-data; name="' + to_bytes(name) + b'"')
        body.append(b'')
        body.append(to_bytes(value))

    body.append(b'--' + _boundary + b'--')

    return content_type, b'\r\n'.join(body)