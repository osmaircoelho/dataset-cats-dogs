import os
import shutil

# configuracao dos caminhos
base_path = os.path.dirname(os.path.abspath(__file__))

source_cats = os.path.join(base_path, 'archive/dogvscat_small/train/cats')
source_dogs = os.path.join(base_path, 'archive/dogvscat_small/train/dogs')
dest_cats = os.path.join(base_path, 'cats')
dest_dogs = os.path.join(base_path, 'dogs')

# funcao para copias 200 arquivos
def copy_images(source, dest, limit=200):
	count = 0 
	for file_name in os.listdir(source):
		if count >= limit: #se ja copiamos 200, paramos
			break
		
		# copiar apenas arquivos de imagem
		if file_name.lower().endswith('.jpg'):
			shutil.copy(os.path.join(source, file_name), os.path.join(dest, file_name))
			count += 1
	print(f"{count} imagens copiadas para {dest}")
	
# copiar 200 imagens de cada categoria
copy_images(source_cats, dest_cats, limit=200)
copy_images(source_dogs, dest_dogs, limit=200)