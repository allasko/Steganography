from PIL import Image
import numpy as np
def steganography(filePath, photoPath):
    # EOF stamp
    eof = '11111111111111111111111111111111'

    # Importing txt file
    file = open(filePath, "r")
    txt = file.read()
    file.close()
    txt = txt + eof
    # Getting an image
    image = Image.open(photoPath)
    image.show("zdjęcie pi")
    image = image.convert('RGB')

    # Getting data from image
    width = image.size[0] #define W and H
    height = image.size[1]
    max = width*height*3

    if width*height*3 < len(txt):
        raise ValueError("Rozmiar zdjęcia jest za mały! Maksymalna długość ciągu to: {}, a minimalne zdjęcie "
                         "powinno zawierać przynajmniej {} pikseli.".format(max, len(txt)))

    # last = ''
    # last1 = ''
    p=0
    # Changing last bit in RGB values
    for y in range(0, height): #each pixel has coordinates height
        row = ""
        for x in range(0, width): #width

            RGB = image.getpixel((x,y))
            R, G, B = RGB
           # print("R: " + str(R) + " G: " + str(G) + " B: " + str(B))
            Rr = bin(R).replace("0b", "").zfill(8)
            Gg = bin(G).replace("0b", "").zfill(8)
            Bb = bin(B).replace("0b", "").zfill(8)
            #print("R " + str(Rr) + " G " + str(Gg) + " B " + str(Bb))
            # last += Rr[7]
            # last += Gg[7]
            # last += Bb[7]
            if p < len(txt):
                Rr = Rr[:-1] + txt[p]
                p += 1
                if p < len(txt):
                    Gg = Gg[:-1] + txt[p]
                    p += 1
                    if p < len(txt):
                        Bb = Bb[:-1] + txt[p]
                        p += 1
                    else:
                        Rr = Rr
                        Gg = Gg
                        Bb = Bb
                else:
                    Rr = Rr
                    Gg = Gg
                    Bb = Bb
            else:
                Rr = Rr
                Gg = Gg
                Bb = Bb

            # last1 += Rr[7]
            # last1 += Gg[7]
            # last1 += Bb[7]
            #print("R1 "+str(Rr) + " G1 " + str(Gg) + " B1 " +str(Bb))
            R = int("".join(str(x) for x in Rr), 2)
            G = int("".join(str(x) for x in Gg), 2)
            B = int("".join(str(x) for x in Bb), 2)
            #print("R1: " + str(R) + " G1: " + str(G) + " B1: " + str(B))
            image.putpixel((x, y), (R, G, B))



    last = ''
    # Reading back from photo
    for y in range(0, height): #each pixel has coordinates height
        row = ""
        for x in range(0, width): #width
            RGB = image.getpixel((x, y))
            R, G, B = RGB
            # print("R: " + str(R) + " G: " + str(G) + " B: " + str(B))
            Rr = bin(R).replace("0b", "").zfill(8)
            Gg = bin(G).replace("0b", "").zfill(8)
            Bb = bin(B).replace("0b", "").zfill(8)
            last += Rr[7]
            last += Gg[7]
            last += Bb[7]


    head, sep, tail = last.partition(eof)
    print(head)
    numerek = 1
    image.save("zaszyfrowny" + str(numerek) + ".png")
    image.show()
    # Reading from photo
def reading(photoPath):
    # EOF stamp
    eof = '11111111111111111111111111111111'
    # Getting an image
    image = Image.open(photoPath)
    image.show()
    image = image.convert('RGB')
    width = image.size[0]  # define W and H
    height = image.size[1]
    last = ''
    # Reading back from photo
    for y in range(0, height): #each pixel has coordinates height
        row = ""
        for x in range(0, width): #width
            RGB = image.getpixel((x, y))
            R, G, B = RGB
            # print("R: " + str(R) + " G: " + str(G) + " B: " + str(B))
            Rr = bin(R).replace("0b", "").zfill(8)
            Gg = bin(G).replace("0b", "").zfill(8)
            Bb = bin(B).replace("0b", "").zfill(8)
            last += Rr[7]
            last += Gg[7]
            last += Bb[7]


    head, sep, tail = last.partition(eof)
    print(head)
    return head