'''Write a program that has three functions: sepia(), remove_all_red(), and gray_scale(). by Matthew Krause
In this code we are asked to display an image in it's original form. We are then asked to manipulate the image three times.
The second image displayed will be missing all of the red, the third will display sepia which is and old fashioned look,
and the third image displayed will be gray scale which looks like black and white photography'''
import cImage as image


def main():  # added a main fuction to keep the program together
    def draw_Orig():  # my simple function to display the original image all it does is draw the original image
        img = image.Image("luther.gif")
        orig = image.ImageWin("Original", img.getWidth(), img.getHeight())
        img.draw(orig)

    draw_Orig()

    def no_Red():  # the second image removes the red from the image
        img = image.Image('luther.gif')
        newimg = image.EmptyImage(img.getWidth(), img.getHeight())
        new = image.ImageWin("No Red", img.getWidth(), img.getHeight())

        for row in range(img.getHeight()):
            for col in range(img.getWidth()):
                p = img.getPixel(col, row)

                newred = 0  # in order to remove red we must set its rgb value to 0 while the others stay the same
                newgreen = p.getGreen()
                newblue = p.getBlue()

                newpixel = image.Pixel(newred, newgreen, newblue)
                img.setPixel(col, row, newpixel)

        img.draw(new)

    no_Red()

    def is_Sepia():  # function to display the sepia image
        img = image.Image('luther.gif')
        newimg = image.EmptyImage(img.getWidth(), img.getHeight())
        new = image.ImageWin("Sepia", img.getWidth(), img.getHeight())

        for row in range(img.getHeight()):
            for col in range(img.getWidth()):
                p = img.getPixel(col, row)

                newred = int((p.getRed() * 0.393) + (p.getGreen() * 0.769) + (
                            p.getBlue() * 0.189))  # the sepia image is a calculation on the red, blue and green
                if newred > 255:  # an if statement is needed to keep the value at a 255 ceiling or else we get an error
                    newred = 255
                newgreen = int((p.getRed() * 0.349) + (p.getGreen() * 0.686) + (
                            p.getBlue() * 0.168))  # the process needs repeated for blue and green as well
                if newgreen > 255:
                    newgreen = 255
                newblue = int((p.getRed() * 0.272) + (p.getGreen() * 0.534) + (p.getBlue() * 0.131))
                if newblue > 255:
                    newblue = 255

                newpixel = image.Pixel(newred, newgreen, newblue)
                img.setPixel(col, row, newpixel)

        img.draw(new)

    is_Sepia()

    def is_Gray_Scale():  # gray scale is developed very similar to sepia because it also requires calculation
        img = image.Image('luther.gif')
        newimg = image.EmptyImage(img.getWidth(), img.getHeight())
        new = image.ImageWin("Gray Scale", img.getWidth(), img.getHeight())

        for row in range(img.getHeight()):
            for col in range(img.getWidth()):
                p = img.getPixel(col, row)

                newred = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (
                            p.getBlue() * 0.114))  # the calculation is plugged in the same as sepia with differnt values
                if newred > 255:  # if statements are added to ensure we don't return errors
                    newred = 255
                newgreen = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (
                            p.getBlue() * 0.114))  # it is interesting to note that the calculations are the same for red, green, and blue
                if newgreen > 255:  # because you are taking the color out of the image
                    newgreen = 255
                newblue = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (p.getBlue() * 0.114))
                if newblue > 255:
                    newblue = 255

                newpixel = image.Pixel(newred, newgreen, newblue)
                img.setPixel(col, row, newpixel)
        img.draw(new)
        new.exitonclick()  # clicking on gray scale closes the windows

    is_Gray_Scale()


main()