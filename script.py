import silly
import requests
import mimetypes

image = silly.image()
print(image)
response = requests.head(image)
content_type = response.headers['content-type']
extension = mimetypes.guess_extension(content_type)
print(extension)
open ('image.png', 'wb').write(requests.get(image).content)

print(silly.sentence())