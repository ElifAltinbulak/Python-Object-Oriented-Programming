"""
Photo book class
Create a python program to manage a photo book using object-oriented programming.

To start, create a class called PhotoBook with a private attribute numPages of type int. It must also have a public method GetNumberPages that will return the number of photo book pages.

The default constructor will create an album with 16 pages. There will be an additional constructor, with which we can specify the number of pages we want in the album.

There is also a BigPhotoBook class whose constructor will create an album with 64 pages.

Finally create a PhotoBookTest class to perform the following actions:

Create a default photo book and show the number of pages
Create a photo book with 24 pages and show the number of pages
Create a large photo book and show the number of pages
"""


class PhotoBook:
    def __init__(self,numPages=16):
        self.__numPages=numPages
    def GetNumberPages(self):
        return self.__numPages
class BigPhotoBook:
    def __init__(self,numPages):
        self.numPages=numPages
        print(numPages)
class PhotoBookTest:
    pb=PhotoBook()
    print(pb.GetNumberPages())
    pb=PhotoBook(24)
    print(pb.GetNumberPages())
    bpb=BigPhotoBook(64)
pbt=PhotoBookTest()
