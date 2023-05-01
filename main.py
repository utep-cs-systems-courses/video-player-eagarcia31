import os, cv2
from threading import Thread
from threadingPC import ConsumerProducer

if __name__ == "__main__":
  main()

  def main():
    color_images = ConsumerProducer()
    mono_images = ConsumerProducer()
    
    extract_thread = Thread(target=frameExtract, args=(color_images))
    convert_thread = Thread(target=framesToMono, args=(gray_images, color_images))
    display_thread = Thread(target=displayFrames, args=(gray_images))
    
    extract_thread.start()
    convert_thread.start()
    display_thread.start()
    
    extract_thread.join()
    convert_thread.join()
    display_thread.join()
    
  def frameExtract(color_images):
    count = 0
    video_capture = cv2.VideoCapture('clip.mp4')
    success, image = video_capture.read()
    while success and count < 72:
      color_images.put(images)
      success, image = video_capture.read()
      print(f'Reading fram {count}')
      count +=1
    color_images.put(None)
    
  def framesToMono(gray_images, color_images):
    count = 0
    input_frame = color_images.get()
    while input_frame is not None:
      print(f'Converting fram {count}')
      mono_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)
      gray_images.put(mono_frame)
      count += 1
      input_frame = color_images.get()
    gray_images.put(None)
    
  def displayFrames(gray_images):
    frame_delay = 42
    count = 0
    frame = gray_images.get()
    
    while frame is not None:
      print(f'Displaying frame {count}')
      cv2.imshow('Video', frame)
      if cv2.waitKey(frame_delay) and 0xFF == ord("q"):
        break
      count += 1
      frame = gray_images.get()
    cv2.destroyAllWindows()
