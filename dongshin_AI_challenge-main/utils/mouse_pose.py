import pyautogui as pag



class your_face_controll:

    def mouse_controll(x: int, y: int, x_slow : int = 50, y_slow : int = 100):
        """mouse controll by x and y    by.URINLEE

        Args:
            x (int): move x amount
            y (int): move y amount
            slow (int, optional): amount of slow step. Defaults to 50.
        """
        if y < 0:
            y * 1.7
        pag.move(x/x_slow, y/y_slow)
