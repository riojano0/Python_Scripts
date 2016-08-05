import io
from PIL import Image

# Image path
path = ["img/john.jpg", "img/sansa.jpg", "img/brandon.jpg"]
imgs = []

# images to streams,  to be able to save in the BLOB column
for p in path:
	i = Image.open(p)
	stream = io.BytesIO()
	i.save(stream, format="JPEG")
	imgs.append(stream.getvalue())

# examples list with images(stream)
starks = [(1, "John", imgs[0]), (2, "Sansa", imgs[1]), (3, "Brandon", imgs[2])]