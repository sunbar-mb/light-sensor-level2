//  Simle application to test Light sensor from Smart home kit 
//  Application measures light intensity , it is in range 0-100
//  and result is dispayed on LED matrix (0=0LEDs, 100=25LEDs)
//  !!! If there's no light sensor connected to the PIN, system returns constant va
let ligt_intensity = 0
let min_n = 0
let max_n = 100
serial.redirectToUSB()
basic.forever(function on_forever() {
    
    ligt_intensity = smarthome.ReadLightIntensity(AnalogPin.P1)
    serial.writeValue("x", ligt_intensity)
    Higlight_X_dots((ligt_intensity - min_n) * (25 / max_n))
    pause(1000)
})
function Higlight_X_dots(Number_of_Dots: number) {
    let Line_num = 0
    let Row_num = 0
    basic.clearScreen()
    if (Number_of_Dots > 25) {
        Number_of_Dots = 25
    }
    
    if (Number_of_Dots <= 0) {
        basic.clearScreen()
    }
    
    for (let i = 0; i < Number_of_Dots; i++) {
        led.plot(Line_num, Row_num)
        Line_num = Line_num + 1
        // Row_num = Row_num + 1
        if (Line_num > 4) {
            Line_num = 0
            Row_num = Row_num + 1
        }
        
    }
}

function on_button_pressed_a() {
    
    min_n -= 1
}

input.onButtonPressed(Button.A, on_button_pressed_a)
function on_button_pressed_b() {
    
    max_n += 1
}

input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    basic.showString("Min" + ("" + min_n))
})
