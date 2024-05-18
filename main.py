# 1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
# 2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt kateqoriya(subdirectory) yaradırıq.
# 3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
# (şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
# 4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları subdirectorydən çıxarıb Example directory-sinə göndərirsiniz.

import os
from pathlib import Path
from PIL import Image
import shutil

# os.mkdir("Example")
# os.makedirs("Example/subdirect")



# ______________________Sekil part____________________________
##Let's add a image from root directory (Python 11 task)
# source_path = 'kaist7.png'
# image = Image.open(source_path)
# save_path = os.path.join('Example','subdirect','kaist7.png')
# image.save(save_path)

# print(f"Image saved to {save_path}")
# os.remove(source_path)  #Deleting the original one from root


###Let's add another image from root
# source_path = 'm7.jpg'
# image = Image.open(source_path)
# dest_path = os.path.join('Example','subdirect','m7.jpg')

# shutil.move(source_path, dest_path)
# os.remove(source_path)  #Deleting the original one from root



#### To show image from another directory
# image_path = os.path.join('Example','subdirect', 'kaist7.png')
# image = Image.open(image_path)
# image.show()

# #Terminal shows the second image after 7 seconds later
# image_path = os.path.join('Example','subdirect', 'm7.jpg')
# image = Image.open(image_path)
# image.show()

# ---------------------Text fayli part---------------------------------




