from PIL import Image
import numpy as np
import random

def generate_key(seed):
    random.seed(seed)

def encrypt_image(input_path, output_path, seed):
    img = Image.open(input_path)
    img_array = np.array(img)
    shape = img_array.shape
    
    flat_array = img_array.flatten()
    indices = list(range(len(flat_array)))
    random.shuffle(indices)

    encrypted_array = flat_array[indices]
    encrypted_image = Image.fromarray(encrypted_array.reshape(shape).astype('uint8'))
    encrypted_image.save(output_path)
    np.save("encryption_indices.npy", indices)  
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, seed):
    img = Image.open(input_path)
    img_array = np.array(img)
    shape = img_array.shape

    indices = np.load("encryption_indices.npy")
    reverse_indices = np.argsort(indices)

    flat_array = img_array.flatten()
    decrypted_array = flat_array[reverse_indices]
    decrypted_image = Image.fromarray(decrypted_array.reshape(shape).astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

input_image = "matrix.jpeg" 
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"

encryption_seed = 212 #any integer can be used

generate_key(encryption_seed)
encrypt_image(input_image, encrypted_image, encryption_seed)
decrypt_image(encrypted_image, decrypted_image, encryption_seed)
