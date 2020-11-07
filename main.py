# Simle application to test Light sensor from Smart home kit 
# Application measures light intensity , it is in range 0-100
# and result is dispayed on LED matrix (0=0LEDs, 100=25LEDs)
# !!! If there's no light sensor connected to the PIN, system returns constant value 25 !!!

ligt_intensity = 0
min_n = 0
max_n = 100



serial.redirect_to_usb()


def on_forever():
    global ligt_intensity, min_n, max_n
    ligt_intensity = smarthome.read_light_intensity(AnalogPin.P1)
    serial.write_value("x", ligt_intensity) 
    Higlight_X_dots((ligt_intensity - min_n) * (25/max_n))
    pause(1000)

    
   

basic.forever(on_forever)



def Higlight_X_dots(Number_of_Dots):
    Line_num = 0
    Row_num = 0
    
    basic.clear_screen()

    if Number_of_Dots > 25:
        Number_of_Dots = 25

    if Number_of_Dots <= 0:
        basic.clear_screen()

    for i in range(Number_of_Dots):
        led.plot(Line_num, Row_num)
        Line_num = Line_num + 1
        #Row_num = Row_num + 1
        if Line_num > 4:
            Line_num = 0
            Row_num = Row_num + 1
    


def on_button_pressed_a():
    global min_n
    min_n -= 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global max_n
    max_n += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global max_n, min_n
    basic.show_string("Min" + str(min_n))
input.on_button_pressed(Button.AB, on_button_pressed_ab)
