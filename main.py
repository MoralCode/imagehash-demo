from PIL import Image
import imagehash
img1_path = "../beekeeping mural/IMG_6392.jpg"
img2_path = "../beekeeping mural/IMG_6394.jpg"
img3_path = "../beekeeping mural/IMG_6395.jpg"
hash = imagehash.average_hash(Image.open(img1_path))
print(hash)
#ffd7918181c9ffff
otherhash = imagehash.average_hash(Image.open(img2_path))
print(otherhash)
#9f172786e71f1e00
print(hash == otherhash)
#False
print(hash - otherhash)  # hamming distance
#33