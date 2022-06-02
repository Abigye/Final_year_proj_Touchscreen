import numpy as np
# import cv2

# img = cv2.imread('images/foo.jpg',1)

# img = cv2.resize(img,(0,0),fx=2,fy=2)

# img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)
# # cv2.imwrite('new_img.jpg',img)

# cv2.imshow('Image',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture("myvid.mp4")

# while True:
#     ret, frame  = cap.read()

#     width = int(cap.get(3))
#     height = int(cap.get(4))

#     image = np.zeros(frame.shape, np.uint8)

#     smaller_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)

#     image[:height//2,:width//2] = smaller_frame
#     image[height//2:, :width//2] = smaller_frame
#     image[:height//2, width//2:] = smaller_frame
#     image[height//2:, width//2:] = smaller_frame



#     cv2.imshow('frame', image)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cap.destroyAllWindows()


# cap = cv2.VideoCapture('rtmp://localhost/live/stream')

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# cap = cv2.VideoCapture('climbing_clip.mp4')

# # if not cap.isOpened():
# #     print("Error opening video")

# # while(cap.isOpened()):
# #     status, frame = cap.read()
# #     if status:
# #         # buf = cv2.flip(frame, 0)
# #         # image_texture = Texture.create(
# #         #     size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
# #         # image_texture.blit_buffer(
# #         #     buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
# #         # video = self.ids.image_source
# #         # video.texture = image_texture
# #             cv2.imshow('frame', frame)
# #     key = cv2.waitKey(500)

# #     if key == 32:
# #         cv2.waitKey()
# #     elif key == ord('q'):
# #         break

# # # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()



# cap1 = cv2.VideoCapture('climbing_clip.mp4')
# cap2 = cv2.VideoCapture('discrepancy.mp4')
# while cap1.isOpened() or cap2.isOpened():

#     okay1, frame1 = cap1.read()
#     okay2, frame2 = cap2.read()
 
#     if okay1:
#         # hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
#         cv2.imshow('fake', frame1)

#     if okay2:
#         # hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
#         cv2.imshow('real', frame2)

#     if not okay1 or not okay2:
#         print('Cant read the video , Exit!')
#         break

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     cv2.waitKey(1)

# cap1.release()
# cap2.release()
# cv2.destroyAllWindows()



import os
print(os.path.abspath('climbing_clip.mp4'))
print(os.path.dirname(os.path.abspath('climbing_clip.mp4')))


