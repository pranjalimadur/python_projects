import cv2
import glob

images=glob.glob("*.jpg")

#re_img=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
#re_img1=cv2.resize(img, (100,100))

#cv2.imshow("Galaxy",re_img)
#cv2.imwrite("GalaxyResize.jpg",re_img1)
