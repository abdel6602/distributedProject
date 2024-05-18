from PIL import Image
from mpi4py import MPI
import cv2
import numpy as np
from simple_operations import *



def split_image(image, horizontal_pieces, upperLimit, lowerLimit, rank):
    image_height, _, _ = image.shape

    piece_height = image_height // horizontal_pieces

    piece = image[((piece_height*rank) - piece_height) - upperLimit:((piece_height*rank) - 1) + lowerLimit, :]

    return piece

def remove_ghostCells(image, ghost, case = 0):

    if case == 1:
        piece = image[:-ghost + 1, :]
    elif case == 2:
        piece = image[ghost:, :]
    else:
        piece = image[ghost:-ghost + 1, :]

    return piece


def reconstruct_image(pieces):
        min_val = np.min([np.min(piece) for piece in pieces if piece is not None])
        max_val = np.max([np.max(piece) for piece in pieces if piece is not None])
        pieces = [
            ((piece - min_val) * (255 / (max_val - min_val))).astype("uint8")
            for piece in pieces
            if piece is not None
        ]
        pieces = np.concatenate(pieces)
        if len(pieces.shape) == 2:
            image = Image.fromarray(pieces, "L")
        else:
            image = Image.fromarray(pieces, "RGB")
        return image

''' NOTE!!!!!!!!!!!!!!!!!!!!!
make sure if we don't use kernel make it 0
IF YOU DON'T YOU MAY KILL YOUR PC
'''

def main():
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    kernalSize = 0 #modifiable 
    
    ghostCells = kernalSize // 2 #DO NOT TOUCH!!!


    image = cv2.imread("./download.jpeg")
    
    gathered_pieces = []

    
    if rank == 0:
        if size > 1:
            #Sending Picture
            for index in range(1, size):
                 if index == 1:
                    piece = split_image(image, size - 1, 0, ghostCells, index)
                 elif index == size - 1:
                    piece = split_image(image, size - 1, ghostCells, 0, index)
                 else:
                     piece = split_image(image, size - 1, ghostCells, ghostCells, index)
                 comm.send(piece, dest=index)
            #Receving Picture    
            for index in range(1, size):
                chunk = comm.recv(source=index, tag=0)
                gathered_pieces.append(chunk)
            processImage = reconstruct_image(gathered_pieces)
            processImage.save("new_image.png")
    else: 
        chunk = comm.recv(source=0, tag=0)
        modifiedChunk = apply_canny(chunk, 10,200)
        if kernalSize != 0:
            if rank == 1:
                modifiedChunk = remove_ghostCells(modifiedChunk, ghostCells, 1)
            elif rank == size - 1:
                modifiedChunk = remove_ghostCells(modifiedChunk, ghostCells, 2)
            else:
                modifiedChunk = remove_ghostCells(modifiedChunk, ghostCells)

        comm.send(modifiedChunk, dest=0)


if __name__ == "__main__":
    main()
