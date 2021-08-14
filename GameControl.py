import ctypes
import logging
import os
import sys
import time
import traceback
import random
import cv2
import numpy as np
import win32api
import win32con
import win32gui
import win32ui
from timeit import default_timer as timer
from PIL import Image




class GameControl():
    def __init__(self, hwnd, quit_game_enable=1):
        '''
        initialization

            : param hwnd: the window handle to be bound

            : param quit_game_enable: Whether to exit the game when the program dies. 
            True is yes, False is no
        '''
        self.run = True
        self.hwnd = hwnd
        self.quit_game_enable = quit_game_enable
        self.debug_enable = False
        l1, t1, r1, b1 = win32gui.GetWindowRect(self.hwnd)
        #print(l1,t1, r1,b1)
        l2, t2, r2, b2 = win32gui.GetClientRect(self.hwnd)
        # print(l2,t2,r2,b2)
        self._client_h = b2 - t2
        self._client_w = r2 - l2
        self._border_l = ((r1 - l1) - (r2 - l2)) // 2
        self._border_t = ((b1 - t1) - (b2 - t2)) - self._border_l
        self.client = 0
      
    def init_mem(self):
        self.hwindc = win32gui.GetWindowDC(self.hwnd)
        self.srcdc = win32ui.CreateDCFromHandle(self.hwindc)
        self.memdc = self.srcdc.CreateCompatibleDC()
        self.bmp = win32ui.CreateBitmap()
        self.bmp.CreateCompatibleBitmap(
            self.srcdc, self._client_w, self._client_h)
        self.memdc.SelectObject(self.bmp)

    def window_full_shot(self, file_name=None, gray=0):
        '''
       Window screenshot

            : param file_name = None: save name of screenshot file

            : param gray = 0: whether to return grayscale image, 0: return BGR color image, others: return grayscale black and white image

            : return: return RGB data if file_name is empty
        '''
        try:
            if (not hasattr(self, 'memdc')):
                self.init_mem()
            if self.client == 0:
                self.memdc.BitBlt((0, 0), (self._client_w, self._client_h), self.srcdc,
                                  (self._border_l, self._border_t), win32con.SRCCOPY)
            else:
                self.memdc.BitBlt((0, -35), (self._client_w, self._client_h), self.srcdc,
                                  (self._border_l, self._border_t), win32con.SRCCOPY)
            if file_name != None:
                self.bmp.SaveBitmapFile(self.memdc, file_name)
                return
            else:
                signedIntsArray = self.bmp.GetBitmapBits(True)
                #img = np.fromstring(signedIntsArray, dtype='uint8')
                img = np.frombuffer(signedIntsArray, dtype='uint8')
                img.shape = (self._client_h, self._client_w, 4)
                #cv2.imshow("image", cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
                # cv2.waitKey(0)
                if gray == 0:
                    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                else:
                    return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        except Exception:
            self.init_mem()
            #logging.warning('window_full_shot执行失败')
            #a = traceback.format_exc()
            #logging.warning(a)

    def window_part_shot(self, pos1, pos2, file_name=None, gray=0):
        '''
        Screenshot of the window area

            : param pos1: (x, y) coordinates of the upper left corner of the screenshot area

            : param pos2: (x, y) coordinates of the lower right corner of the screenshot area

            : param file_name = None: save path of screenshot file

            : param gray = 0: whether to return grayscale image, 0: return BGR color image, others: return grayscale black and white image

            : return: return RGB data if file_name is empty
        '''
        w = pos2[0]-pos1[0]
        h = pos2[1]-pos1[1]
        hwindc = win32gui.GetWindowDC(self.hwnd)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, w, h)
        memdc.SelectObject(bmp)
        if self.client == 0:
            memdc.BitBlt((0, 0), (w, h), srcdc,
                         (pos1[0]+self._border_l, pos1[1]+self._border_t), win32con.SRCCOPY)
        else:
            memdc.BitBlt((0, -35), (w, h), srcdc,
                         (pos1[0]+self._border_l, pos1[1]+self._border_t), win32con.SRCCOPY)
        if file_name != None:
            bmp.SaveBitmapFile(memdc, file_name)
            srcdc.DeleteDC()
            memdc.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, hwindc)
            win32gui.DeleteObject(bmp.GetHandle())
            return
        else:
            signedIntsArray = bmp.GetBitmapBits(True)
            img = np.frombuffer(signedIntsArray, dtype='uint8')
            img.shape = (h, w, 4)
            srcdc.DeleteDC()
            memdc.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, hwindc)
            win32gui.DeleteObject(bmp.GetHandle())
            #cv2.imshow("image", cv2.cvtColor(img, cv2.COLOR_BGRA2BGR))
            # cv2.waitKey(0)
            if gray == 0:
                return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            else:
                return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    def find_color(self, region, color, tolerance=0):
        '''
        Looking for color

            : param region: ((x1, y1), (x2, y2)) coordinates of the upper left corner and lower right corner of the area to be searched

            : param color: (r, g, b) The color to search

            : param tolerance = 0: tolerance value

            : return: successfully returns the coordinates of the client area, -1 if it fails
        '''
        img = Image.fromarray(self.window_part_shot(
            region[0], region[1]), 'RGB')
        width, height = img.size
        r1, g1, b1 = color[:3]
        for x in range(width):
            for y in range(height):
                try:
                    pixel = img.getpixel((x, y))
                    r2, g2, b2 = pixel[:3]
                    if abs(r1-r2) <= tolerance and abs(g1-g2) <= tolerance and abs(b1-b2) <= tolerance:
                        return x+region[0][0], y+region[0][1]
                except Exception:
                    logging.warning('find_color failed to execute')
                    a = traceback.format_exc()
                    logging.warning(a)
                    return -1
        return -1

    def check_color(self, pos, color, tolerance=0):
        '''
        Compare the color of a point in the window

            : param pos: (x, y) the coordinates to compare

            : param color: (r, g, b) the color to be compared

            : param tolerance = 0: tolerance value

            : return: returns True on success, False on failure
        '''
        img = Image.fromarray(self.window_full_shot(), 'RGB')
        r1, g1, b1 = color[:3]
        r2, g2, b2 = img.getpixel(pos)[:3]
        if abs(r1-r2) <= tolerance and abs(g1-g2) <= tolerance and abs(b1-b2) <= tolerance:
            return True
        else:
            return False

    def find_img(self, img_template_path, part=0, pos1=None, pos2=None, gray=0, center=True,delay=0.1):
        '''
        Find pictures

            : param img_template_path: the path of the image to be found

            : param part = 0: whether to search in full screen, 1 is no, other is yes

            : param pos1 = None: the coordinates of the upper left corner of the range to be searched

            : param pos2 = None: the coordinates of the lower right corner of the range to be searched

            : param gray = 0: whether to search by color, 0: find color pictures, 1: find black and white pictures

            : return: (maxVal, maxLoc) maxVal is the correlation, the closer to 1, the better, maxLoc is the obtained coordinate
        '''
        time.sleep(delay)
        # Get screenshot
        if part == 1:
            img_src = self.window_part_shot(pos1, pos2, None, gray)
            #print('take part shot')
        else:
            img_src = self.window_full_shot(None, gray)
            #print('take full shot')
        # show_img(img_src)

        # Read file
        if gray == 0:
            img_template = cv2.imread(img_template_path, cv2.IMREAD_COLOR)
        else:
            img_template = cv2.imread(img_template_path, cv2.IMREAD_GRAYSCALE)

        #show_img(img_template)
        try:
            res = cv2.matchTemplate(
                img_src, img_template, cv2.TM_CCOEFF_NORMED)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
            if self.debug_enable:
                if part == 1:
                    img = self.window_part_shot(pos1,pos2,None,gray)
                else :
                    img = self.window_full_shot()
                self.img = cv2.rectangle(img, maxLoc, (maxLoc[0]+img_template.shape[1],maxLoc[1]+img_template.shape[0]), (0, 255, 0), 3)
                show_img(img)
                print("Top left point location: ",maxLoc)
                print("Score: ",maxVal)
            if center:
                maxLoc=list(maxLoc)
                maxLoc[0]=int(maxLoc[0]+(img_template.shape[1]/2))
                maxLoc[1]=int(maxLoc[1]+(img_template.shape[0]/2))
            return maxVal, maxLoc
        except Exception:
            #logging.warning('find_img failed to execute')
            #a = traceback.format_exc()
            #logging.warning(a)
            return 0, 0

    def find_img_knn(self, img_template_path, part=0, pos1=None, pos2=None, gray=0, thread=0, center=True):
        '''
        Find pictures, knn algorithm
        param img_template_path: the path of the image to be found
        param part = 0: whether to search in full screen, 1 is no, other is yes
        param pos1 = None: the coordinates of the upper left corner of the range to be searched
        param pos2 = None: the coordinates of the lower right corner of the range to be searched
        param gray = 0: whether to search by color, 0: find color pictures, 1: find black and white pictures
        return: coordinates (x, y), return (0, 0) if not found, -1 if it fails
        '''
        # Get screenshot
        if part == 1:
            img_src = self.window_part_shot(pos1, pos2, None, gray)
        else:
            img_src = self.window_full_shot(None, gray)

        # show_img(img_src)

        # Read file
        if gray == 0:
            img_template = cv2.imread(img_template_path, cv2.IMREAD_COLOR)
        else:
            img_template = cv2.imread(img_template_path, cv2.IMREAD_GRAYSCALE)

        try:
            maxLoc = match_img_knn(img_template, img_src, thread)
            # print(maxLoc)
            if self.debug_enable:
                if part == 1:
                    img = self.window_part_shot(pos1,pos2,None,gray)
                else :
                    img = self.window_full_shot()

                self.img = cv2.rectangle(img, maxLoc, (maxLoc[0]+img_template.shape[1],maxLoc[1]+img_template.shape[0]), (0, 255, 0), 3)
                print("Top left point location: ",maxLoc)
                #print("Score: ",maxVal)
                show_img(img)
            if center:
                maxLoc=list(maxLoc)
                maxLoc[0]=int(maxLoc[0]+(img_template.shape[1]/2))
                maxLoc[1]=int(maxLoc[1]+(img_template.shape[0]/2))
                maxLoc=tuple(maxLoc)
            return maxLoc
        except Exception:
            logging.warning('find_img_knn failed to execute')
            a = traceback.format_exc()
            logging.warning(a)
            return -1

    def find_multi_img(self, *img_template_path, part=0, pos1=None, pos2=None, gray=0):
        '''
        Find multiple pictures
        : param img_template_path: list of image paths to find
        : param part = 0: whether to search in full screen, 1 is no, other is yes
        : param pos1 = None: the coordinates of the upper left corner of the range to be searched
        : param pos2 = None: the coordinates of the lower right corner of the range to be searched
        : param gray = 0: whether to search by colo:r, 0: find color pictures, 1: find black and white pictures
        : return: (maxVal, maxLoc) maxVal is the correlation list, the closer to 1, the better, maxLoc is the obtained coordinate list
        '''
        
        # Window screenshot
        if part == 1:
            img_src = self.window_part_shot(pos1, pos2, None, gray)
        else:
            img_src = self.window_full_shot(None, gray)

        # Return value list
        maxVal_list = []
        maxLoc_list = []
        for item in img_template_path:
            # Read file
            if gray == 0:
                img_template = cv2.imread(item, cv2.IMREAD_COLOR)
            else:
                img_template = cv2.imread(item, cv2.IMREAD_GRAYSCALE)

            # Start recognition
            try:
                res = cv2.matchTemplate(
                    img_src, img_template, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
                maxVal_list.append(maxVal)
                maxLoc_list.append(maxLoc)
            except Exception:
                logging.warning('find_multi_img执行失败')
                a = traceback.format_exc()
                logging.warning(a)
                maxVal_list.append(0)
                maxLoc_list.append(0)
        # Back to list
        return maxVal_list, maxLoc_list

    def activate_window(self):
        user32 = ctypes.WinDLL('user32.dll')
        user32.SwitchToThisWindow(self.hwnd, True)

    def mouse_move(self, pos, pos_end=None):
        '''
        Simulate mouse movement
        : param pos: (x, y) the coordinates of the mouse movement
        : param pos_end = None: (x, y) If pos_end is not empty, 
        the mouse moves to a random position in the area where pos is the upper left corner coordinate pos_end is the lower right corner coordinate
        '''
        pos2 = win32gui.ClientToScreen(self.hwnd, pos)
        if pos_end == None:
            win32api.SetCursorPos(pos2)
        else:
            pos_end2 = win32gui.ClientToScreen(self.hwnd, pos_end)
            pos_rand = (random.randint(
                pos2[0], pos_end2[0]), random.randint(pos2[1], pos_end2[1]))
            win32api.SetCursorPos(pos_rand)

    def mouse_click(self):
        '''
        Mouse click
        '''
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(random.randint(20, 80)/1000)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def mouse_drag(self, pos1, pos2):
        '''
        Mouse drag
        : param pos1: (x, y) starting point coordinates
        : param pos2: (x, y) end point coordinates
        '''
        pos1_s = win32gui.ClientToScreen(self.hwnd, pos1)
        pos2_s = win32gui.ClientToScreen(self.hwnd, pos2)
        screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        start_x = pos1_s[0]*65535//screen_x
        start_y = pos1_s[1]*65535//screen_y
        dst_x = pos2_s[0]*65535//screen_x
        dst_y = pos2_s[1]*65535//screen_y
        move_x = np.linspace(start_x, dst_x, num=20, endpoint=True)[0:]
        move_y = np.linspace(start_y, dst_y, num=20, endpoint=True)[0:]
        self.mouse_move(pos1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        for i in range(20):
            x = int(round(move_x[i]))
            y = int(round(move_y[i]))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE |
                                 win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
            time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def mouse_click_bg(self, pos, pos_end=None):
        '''
            Background mouse click
            : param pos: (x, y) the coordinates of the mouse click
            : param pos_end = None: (x, y) If pos_end is not empty, 
            the mouse clicks a random position in the area where pos is the upper left corner coordinate pos_end is the lower right corner coordinate
        '''
        if self.debug_enable:
            img = self.window_full_shot()
            self.img = cv2.rectangle(img, pos, None, (255, 0, 0), 3)
            show_img(img)

        if pos_end == None:
            pos_rand = pos
        else:
            pos_rand = (random.randint(
                pos[0], pos_end[0]), random.randint(pos[1], pos_end[1]))
        if self.client == 0:
            #win32gui.SendMessage(self.hwnd, win32con.BM_CLICK,300,300)
            win32gui.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE,
                                 0, win32api.MAKELONG(pos_rand[0], pos_rand[1]))
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN,
                                 0, win32api.MAKELONG(pos_rand[0], pos_rand[1]))
            time.sleep(random.randint(20, 80)/1000)
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP,
                                 0, win32api.MAKELONG(pos_rand[0], pos_rand[1]))
        else:
            command = str(pos_rand[0]) + ' ' + str(pos_rand[1])
            os.system('adb shell input tap ' + command)

    def mouse_drag_bg(self, pos1, pos2,delay=0.04):
        '''
            :param pos1: (x,y) 
            :param pos2: (x,y) 
        '''
        if self.client == 0:
            move_x = np.linspace(pos1[0], pos2[0], num=20, endpoint=True)[0:]
            move_y = np.linspace(pos1[1], pos2[1], num=20, endpoint=True)[0:]
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN,
                                 0, win32api.MAKELONG(pos1[0], pos1[1]))
            for i in range(20):
                x = int(round(move_x[i]))
                y = int(round(move_y[i]))
                win32gui.SendMessage(
                    self.hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))
                time.sleep(delay)
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP,
                                 0, win32api.MAKELONG(pos2[0], pos2[1]))
        else:
            command = str(pos1[0])+' ' + str(pos1[1]) + \
                ' '+str(pos2[0])+' '+str(pos2[1])
            os.system('adb shell input swipe '+command)

    def wait_game_img(self, img_path, max_time=100, quit=True):
        """
        Waiting for game image
        : param img_path: image path
        : param max_time = 60: timeout time
        : param quit = True: whether to quit after timeout
        : return: return coordinates successfully, False if failed
        """
        self.rejectbounty()
        start_time = time.time()
        while time.time()-start_time <= max_time and self.run:
            maxVal, maxLoc = self.find_img(img_path)
            if maxVal > 0.9:
                return maxLoc
            if max_time > 5:
                time.sleep(1)
            else:
                time.sleep(0.1)
        if quit:
            # Time out to exit the game
            self.quit_game()
        else:
            return False

    def wait_game_img_knn(self, img_path, max_time=100, quit=True, thread=0):
        '''
        Waiting for game image
        : param img_path: image path
        : param max_time = 60: timeout time
        : param quit = True: whether to quit after timeout
        : return: return coordinates successfully, False if failed
        '''
        self.rejectbounty()
        start_time = time.time()
        while time.time()-start_time <= max_time and self.run:
            maxLoc = self.find_img_knn(img_path, thread=thread)
            if maxLoc != (0, 0):
                return maxLoc
            if max_time > 5:
                time.sleep(1)
            else:
                time.sleep(0.1)
        if quit:
            # Time out to exit the game
            self.quit_game()
        else:
            return False

    def wait_game_color(self, region, color, tolerance=0, max_time=60, quit=True):
        '''
       Waiting for game color
        : param region: ((x1, y1), (x2, y2)) The region to search
        : param color: (r, g, b) the color to wait for
        : param tolerance = 0: tolerance value
        : param max_time = 30: timeout time
        : param quit = True: whether to quit after timeout
        : return: Returns True on success, False on failure
        '''
        self.rejectbounty()
        start_time = time.time()
        while time.time()-start_time <= max_time and self.run:
            pos = self.find_color(region, color)
            if pos != -1:
                return True
            time.sleep(1)
        if quit:
            # Time out to exit the game
            self.quit_game()
        else:
            return False

    def quit_game(self):
        '''
        exit the game
        '''
        #self.takescreenshot()  # Save the scene
        self.clean_mem()    # Clean up memory
        #logging.info('Exit, the last display has been saved to the /img/screenshots folder')
        sys.exit(0)

    def takescreenshot(self):
        '''
        Screenshot
        '''
        name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        img_src_path = 'img/screenshots/%s.png' %(name)
        self.window_full_shot(img_src_path)
        logging.info('Screenshot has been saved to img/screenshots/%s.png' %(name))

    def rejectbounty(self):
        '''
        Refusal
        return: refuse to return True, otherwise return False
        '''
        maxVal, maxLoc = self.find_img('./screenshots/coopwanted.png',thread=0.8)
        if maxVal > 0.9:
            self.mouse_click_bg((749, 453))
            return True
        return False

    def find_game_img(self, img_path, part=0, pos1=None, pos2=None, gray=1, center=True,thread=0.9):
        '''
        Find pictures
        : param img_path: search path
        : param part = 0: whether to search in full screen, 0 is no, other is yes
        : param pos1 = None: the coordinates of the upper left corner of the range to be searched
        : param pos2 = None: the coordinates of the lower right corner of the range to be searched
        : param gray = 0: whether to find black and white pictures, 0: find color pictures, 1: find black and white pictures
        : param thread = 0.9: custom threshold
        : return: Returns the position coordinates after successful search, otherwise returns False
        '''
        #self.rejectbounty()
        maxVal, maxLoc = self.find_img(img_path, part, pos1, pos2, gray,center)
        # print(maxVal)
        if maxVal > thread:
            return list(maxLoc)
        else:
            return False

    def find_game_img_knn(self, img_path, part=0, pos1=None, pos2=None, gray=1, center=True, thread=0):
        '''
        Find pictures
        : param img_path: search path
        : param part = 0: whether to search in full screen, 0 is no, other is yes
        : param pos1 = None: the coordinates of the upper left corner of the range to be searched
        : param pos2 = None: the coordinates of the lower right corner of the range to be searched
        : param gray = 0: whether to find black and white pictures, 0: find color pictures, 1: find black and white pictures
        : param thread = 0:
        : return: Returns the position coordinates after successful search, otherwise returns False
        '''
        #self.rejectbounty()
        maxLoc = self.find_img_knn(img_path, part, pos1, pos2, gray, thread,center)
        # print(maxVal)
        if maxLoc != (0, 0):
            return maxLoc
        else:
            return False

    def debug(self):
        '''
        Self-test resolution and click range
        '''

        self.debug_enable = True

    
        self.img = self.window_full_shot()
        logging.info('Game resolution:' + str(self.img.shape))

        while(1):
  
            cv2.imshow('Click Area (Press \'q\' to exit)', self.img)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break

        cv2.destroyAllWindows()
        self.debug_enable = False

    def clean_mem(self):
        '''
        Clean up memory
        '''
        self.srcdc.DeleteDC()
        self.memdc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.hwindc)
        win32gui.DeleteObject(self.bmp.GetHandle())


# For testing

def match_img_knn(queryImage, trainingImage, thread=0):
    thread=0
    sift = cv2.xfeatures2d.SIFT_create()  
    #sift=cv2.ORB_create(nfeatures=2500)
    #sift=cv2.xfeatures2d.SURF_create()
    kp1, des1 = sift.detectAndCompute(queryImage, None)
    kp2, des2 = sift.detectAndCompute(trainingImage, None)
  
    FLANN_INDEX_KDTREE = 1
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)
    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    matches = flann.knnMatch(des1, des2, k=2)

    good = []

    matchesMask = [[0, 0] for i in range(len(matches))]
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7*n.distance: 
            matchesMask[i] = [1, 0]
            good.append(m)

    s = sorted(good, key=lambda x: x.distance)
    
    '''
    drawParams=dict(matchColor=(0,0,255),singlePointColor=(255,0,0),matchesMask=matchesMask,flags=0) #给特征点和匹配的线定义颜色
    resultimage=cv2.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams) #画出匹配的结果
    show_img(resultimage)
    '''

    if len(good) > thread:
        maxLoc = kp2[s[0].trainIdx].pt
        return (int(maxLoc[0]), int(maxLoc[1]))
    else:
        return (0, 0)

def show_img(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)

def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True

# hwnds = {}
# win32gui.EnumChildWindows(hwnd, callback, hwnds)
# for key, value in hwnds.items():
#     yys = GameControl(value, 0)

    


def main():
    hwnd = win32gui.FindWindow(0, 'Onmyoji')
    yys = GameControl(hwnd, 0)
    yys.activate_window()
    yys.mouse_click_bg((681, 351))
    #REGION_FIND_FULL_EXP_SOLO=[(0,0),(520, 600)]
    #IMAGE_SOUL_INVITE_DIALOG_PATH="/screenshots/Soul/inviteDialog.png"
    #yys.debug_enable=True
    #a=yys.window_full_shot()
    #show_img(a)

    #yys.find_img("screenshots/Soul/inviteDialog.png")
    #IMAGE_STORY_FULL1_PATH="./screenshots/Story/full2.png"
    #REGION_CHANGE_EXP_SOLO=[(387, 61),(1105, 374)]
    #IMAGE_STORY_SHIKIGAMI_SELECTED_PATH="./screenshots/Story/shikigamiSelected8.png"

    #yys.debug()
    # start = timer() 
    # s=yys.find_game_img('test.png',gray=0)
    # print("\nnormal rgb:", timer()-start,'\n')

    # start = timer() 
    # s=yys.find_game_img('test.png',gray=1)
    # print("normal gray:", timer()-start,'\n')
    
    # start = timer() 
    # s=yys.find_game_img_knn('test.png',gray=0)
    # print("knn:", timer()-start,'\n')

    # start = timer() 
    # s=yys.find_game_img_knn('test.png',gray=1)
    # print("knn gray:", timer()-start,'\n')
    
    #show_img(s)
    #print("with GPU:", timer()-start) 
    #yys.debug_enable=False
    

if __name__ == '__main__':
    main()
