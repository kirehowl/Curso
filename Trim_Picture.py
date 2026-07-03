from PIL import Image
import os

# Parámetros
#input_folder = '.'  # Carpeta actual
input_folder = os.path.dirname(os.path.abspath(__file__))
print(input_folder)
output_folder = input_folder + '/imagenes_recortadas'
target_size = (6600, 3800)

# Crear carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

def crop_top_left(img, crop_width, crop_height):
    return img.crop((0, 0, crop_width, crop_height))

# Procesar imágenes en la misma carpeta que el script
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        if filename == os.path.basename(__file__):  # Evitar procesar el propio script
            continue
        path = os.path.join(input_folder, filename)
        with Image.open(path) as img:
            print(f"Procesando: {filename} - tamaño: {img.size}")
            if img.width >= target_size[0] and img.height >= target_size[1]:
                img_cropped = crop_top_left(img, *target_size)
                output_path = os.path.join(output_folder, filename)
                img_cropped.save(output_path)
                print(f"Imagen recortada: {filename}")
            else:
                print(f"Imagen demasiado pequeña: {filename} - tamaño: {img.size}")
