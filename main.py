from PIL import Image
import imagehash
from dataclasses import dataclass, field
import argparse
import csv


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




if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Read CSV and run difference analysis.')
	parser.add_argument('csv_file', help='Path to the CSV file containing names for each image and their file path', default="input.csv")

	args = parser.parse_args()
	csv_file_path = args.csv_file

	images = []

	with open(csv_file_path, 'r') as file:
		csv_reader = csv.DictReader(file)
		for row in csv_reader:
			name = row['name']
			filepath = row['filepath']
			images.append(HashedImage(name, filepath))

	comparison(images, name="all algorithms", algorithms=[imagehash.average_hash,imagehash.phash,imagehash.colorhash,imagehash.dhash])

	comparison(images, name="average alg")
	comparison(images, name="perceptual", algorithms=[imagehash.phash])
	comparison(images, name="color", algorithms=[imagehash.colorhash])
	comparison(images, name="difference", algorithms=[imagehash.dhash])
