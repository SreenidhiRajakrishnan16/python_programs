from pages.frames import Frames



def test_frame(base_page):
    driver = base_page
    frames = Frames(driver)
    frames.navigate_frames()