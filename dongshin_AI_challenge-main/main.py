import cv2
import mediapipe as mp
import pyautogui as pa
from utils.mouse_pose import your_face_controll


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)



drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
    while capture.isOpened():
        
        cap, image = capture.read()
        ih, iw, ic = image.shape

        if not cap:
            print("Ignoring empty camera frame.")
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        

        results = face_mesh.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            
            for face_landmarks in results.multi_face_landmarks:
                nose_x = int((face_landmarks.landmark[4].x) * iw)
                nose_y = int((face_landmarks.landmark[4].y) * ih)
                down_x = int((face_landmarks.landmark[164].x) * iw)
                down_y = int((face_landmarks.landmark[164].y) * ih)
                boll_x = int((face_landmarks.landmark[36].x) * iw)
                boll_y = int((face_landmarks.landmark[36].y) * ih)

                face_x = int((face_landmarks.landmark[164].x * iw - face_landmarks.landmark[4].x * iw) * 100)
                face_y = int((face_landmarks.landmark[4].y * ih - face_landmarks.landmark[36].y * ih+10) * 100)
                your_face_controll.mouse_controll(x=face_x, y=face_y)
                
                
                

                    

                #마킹
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                cv2.line(img=image, pt1=(down_x, down_y), pt2=(down_x, down_y),color=(0, 0, 255), thickness=5)
                cv2.line(img=image, pt1=(nose_x, nose_y), pt2=(nose_x, nose_y),color=(255, 0, 0), thickness=5)
                cv2.line(img=image, pt1=(boll_x, boll_y), pt2=(boll_x, boll_y),color=(0, 255, 0), thickness=5)
                

        cv2.imshow("head", cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break


