from PIL import Image
import imagehash
from dataclasses import dataclass, field

@dataclass
class HashedImage:
	name:str
	path: str
	hashes = field(default_factory=dict, init=False, compare=False)

	def hash(self, algorithm=imagehash.average_hash):
		cached_hash = self.hashes.get(algorithm.__name__)
		if not cached_hash:
			self.hashes[algorithm.__name__] = algorithm(Image.open(self.path))
			return self.hashes.get(algorithm.__name__)
		return cached_hash


img1_path = HashedImage("geoff beekeeping center", "../beekeeping mural/IMG_6392.jpg")
img2_path = HashedImage("geoff beekeeping right","../beekeeping mural/IMG_6394.jpg")
img3_path = HashedImage("geoff beekeeping left","../beekeeping mural/IMG_6395.jpg")
br_path = HashedImage("bottle return official center", '../bottlerturn6a14cdbb3c24e89c091361341023f440.jpeg')
realimg_path = HashedImage("beekeeping official center", "../beekeeping mural/71f42938e5180652b19e2b0d9a36a97c.jpeg")

images = [
	img1_path, img2_path, img3_path, br_path, realimg_path
]



def comparison(images = [], comparison_img = None, name="", algorithm=imagehash.average_hash):
	
	print()
	print(name)

	modifier = 0 if comparison_img is None else 1

	if len(images) + modifier >= 2:
		if not comparison_img:
			comparison_img = images[0]
			images = images[1:]
		
		hash_real = algorithm(Image.open(realimg_path))
		hash1 = algorithm(Image.open(img1_path))
		hash2 = algorithm(Image.open(img2_path))
		hash3 = algorithm(Image.open(img3_path))
		br_hash = algorithm(Image.open(br_path))

		print(f"real: {hash_real}")
		print(f"1: {hash1}")
		print(f"2: {hash2}")
		print(f"3: {hash3}")
		print(f"br: {br_hash}")

		#ffd7918181c9ffff
		print(hash_real)
		#9f172786e71f1e00
		# print(hash == otherhash)
		# #False
		print(hash_real - hash1)  # hamming distance
		#33

		print(hash_real - hash2)  # hamming distance

		print(hash_real - hash3)  # hamming distance
		print(hash_real - br_hash)  # hamming distance
	else:
		print("not enough images supplied, need at least 2")


comparison(name="default")
comparison(name="perceptual", algorithm=imagehash.phash)
comparison(name="color", algorithm=imagehash.colorhash)
comparison(name="difference", algorithm=imagehash.dhash)