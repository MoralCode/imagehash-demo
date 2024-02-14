from PIL import Image
import imagehash
from dataclasses import dataclass, field

@dataclass
class HashedImage:
	name:str
	path: str
	hashes:dict = field(default_factory=dict, init=False, compare=False)

	def hash(self, algorithm=imagehash.average_hash):
		cached_hash = self.hashes.get(algorithm.__name__)
		if not cached_hash:
			self.hashes[algorithm.__name__] = algorithm(Image.open(self.path))
			return self.hashes.get(algorithm.__name__)
		return cached_hash

	def hamming(self, other, algorithms=[]):
		hamming = 0

		if len(algorithms) == 0:
			print("No Algorithm Supplied")
			return
		else:
			for algorithm in algorithms:
				# ensure both images have bene hashed with that algorithm
				self.hash(algorithm=algorithm)
				other.hash(algorithm=algorithm)
				# add the hamming distance to the total
				hamming += self.hashes.get(algorithm.__name__)-other.hashes.get(algorithm.__name__)
			return hamming


img1 = HashedImage("geoff beekeeping center", "../beekeeping mural/IMG_6392.jpg")
img2 = HashedImage("geoff beekeeping right","../beekeeping mural/IMG_6394.jpg")
img3 = HashedImage("geoff beekeeping left","../beekeeping mural/IMG_6395.jpg")
br = HashedImage("bottle return official center", '../bottlerturn6a14cdbb3c24e89c091361341023f440.jpeg')
realimg = HashedImage("beekeeping official center", "../beekeeping mural/71f42938e5180652b19e2b0d9a36a97c.jpeg")

images = [
	img1, img2, img3, br, realimg
]



def comparison(images = [], comparison_img = None, name="", algorithms=[imagehash.average_hash], include_comparison=False):
	
	print()
	print(name)

	modifier = 0 if comparison_img is None else 1

	if len(images) + modifier >= 2:
		if not comparison_img:
			comparison_img = images[0]
			images = images[1:]
		
		if include_comparison:
			images.append(comparison_img)

		for image in images:
			
			print(f"[{image.hamming(comparison_img, algorithms=algorithms)}] {image.name}")

	else:
		print("not enough images supplied, need at least 2")


comparison(images, name="default")
comparison(images, name="perceptual", algorithms=[imagehash.phash])
comparison(images, name="color", algorithms=[imagehash.colorhash])
comparison(images, name="difference", algorithms=[imagehash.dhash])
