from PIL import Image
import imagehash
img1_path = "../beekeeping mural/IMG_6392.jpg"
img2_path = "../beekeeping mural/IMG_6394.jpg"
img3_path = "../beekeeping mural/IMG_6395.jpg"
br_path = '../bottlerturn6a14cdbb3c24e89c091361341023f440.jpeg'
realimg_path = "../beekeeping mural/71f42938e5180652b19e2b0d9a36a97c.jpeg"

hash_real = imagehash.average_hash(Image.open(realimg_path))
hash1 = imagehash.average_hash(Image.open(img1_path))
hash2 = imagehash.average_hash(Image.open(img2_path))
hash3 = imagehash.average_hash(Image.open(img3_path))
br_hash = imagehash.average_hash(Image.open(br_path))

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
