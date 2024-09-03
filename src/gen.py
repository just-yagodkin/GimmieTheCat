import torch
from utils import save_image, denorm

generator = torch.load('model/generator_weights.pth', weights_only=False, map_location=torch.device('cpu'))

noise = torch.randn(1, 128, 1, 1)

pic = generator(noise)
pic = denorm(pic)

save_image(pic, 'pics/gen_cat.png')
