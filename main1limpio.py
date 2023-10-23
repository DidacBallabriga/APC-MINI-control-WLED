import rtmidi
import mido
from buttons_functions import *

def setup_midi_device():
    midiin = rtmidi.MidiIn()
    ports = midiin.get_ports()
    midiout = rtmidi.MidiOut()
    if ports:
        midiin.open_port(0)
    else:
        print('No MIDI ports found. Are you sure your controller is connected?')
        midiin.close_port()
        exit()
    return midiin, midiout

def map_notes_to_buttons():
    button_dict = {
        #ROW 1
        0x38: {"name": "Track Button 21", "behavior": 0x96, "color": 0x03, "function": web_0x38, "modifiable": False},
        0x39: {"name": "Track Button 39", "behavior": 0x96, "color": 0x03, "function": web_0x39, "modifiable": False},
        0x3A: {"name": "Track Button 3A", "behavior": 0x96, "color": 0x03, "function": web_0x3A, "modifiable": False},
        0x3B: {"name": "Track Button 3B", "behavior": 0x96, "color": 0x21, "function": web_0x3B, "modifiable": True},
        0x3C: {"name": "Track Button 3C", "behavior": 0x96, "color": 0x21, "function": web_0x3C, "modifiable": True},
        0x3D: {"name": "Track Button 3D", "behavior": 0x96, "color": 0x21, "function": web_0x3D, "modifiable": True},
        0x3E: {"name": "Track Button 3E", "behavior": 0x96, "color": 0x21, "function": web_0x3E, "modifiable": True},
        0x3F: {"name": "Track Button 3F", "behavior": 0x96, "color": 0x21, "function": web_0x3F, "modifiable": True},
        #ROW 2
        0x30: {"name": "Track Button 30", "behavior": 0x96, "color": 0x6D, "function": web_0x30, "modifiable": False},
        0x31: {"name": "Track Button 31", "behavior": 0x96, "color": 0x6D, "function": web_0x31, "modifiable": False},
        0x32: {"name": "Track Button 32", "behavior": 0x96, "color": 0x6D, "function": web_0x32, "modifiable": False},
        0x33: {"name": "Track Button 33", "behavior": 0x96, "color": 0x21, "function": web_0x33, "modifiable": True},
        0x34: {"name": "Track Button 34", "behavior": 0x96, "color": 0x21, "function": web_0x34, "modifiable": True},
        0x35: {"name": "Track Button 35", "behavior": 0x96, "color": 0x21, "function": web_0x35, "modifiable": True},
        0x36: {"name": "Track Button 36", "behavior": 0x96, "color": 0x21, "function": web_0x36, "modifiable": True},
        0x37: {"name": "Track Button 37", "behavior": 0x96, "color": 0x21, "function": web_0x37, "modifiable": True},
        #ROW 3
        0x28: {"name": "Track Button 28", "behavior": 0x96, "color": 0x09, "function": web_0x28, "modifiable": False},
        0x29: {"name": "Track Button 29", "behavior": 0x96, "color": 0x09, "function": web_0x29, "modifiable": False},
        0x2A: {"name": "Track Button 2A", "behavior": 0x96, "color": 0x09, "function": web_0x2A, "modifiable": False},
        0x2B: {"name": "Track Button 2B", "behavior": 0x96, "color": 0x21, "function": web_0x2B, "modifiable": True},
        0x2C: {"name": "Track Button 2C", "behavior": 0x96, "color": 0x21, "function": web_0x2C, "modifiable": True},
        0x2D: {"name": "Track Button 2D", "behavior": 0x96, "color": 0x21, "function": web_0x2D, "modifiable": True},
        0x2E: {"name": "Track Button 2E", "behavior": 0x96, "color": 0x21, "function": web_0x2E, "modifiable": True},
        0x2F: {"name": "Track Button 2F", "behavior": 0x96, "color": 0x21, "function": web_0x2F, "modifiable": True},
        #ROW 4
        0x20: {"name": "Track Button 20", "behavior": 0x96, "color": 0x05, "function": web_0x20, "modifiable": False},
        0x21: {"name": "Track Button 21", "behavior": 0x96, "color": 0x05, "function": web_0x21, "modifiable": False},
        0x22: {"name": "Track Button 22", "behavior": 0x96, "color": 0x05, "function": web_0x22, "modifiable": False},
        0x23: {"name": "Track Button 23", "behavior": 0x96, "color": 0x21, "function": web_0x23, "modifiable": True},
        0x24: {"name": "Track Button 24", "behavior": 0x96, "color": 0x21, "function": web_0x24, "modifiable": True},
        0x25: {"name": "Track Button 25", "behavior": 0x96, "color": 0x21, "function": web_0x25, "modifiable": True},
        0x26: {"name": "Track Button 26", "behavior": 0x96, "color": 0x21, "function": web_0x26, "modifiable": True},
        0x27: {"name": "Track Button 27", "behavior": 0x96, "color": 0x21, "function": web_0x27, "modifiable": True},
        #ROW 5
        0x18: {"name": "Track Button 18", "behavior": 0x96, "color": 0x52, "function": web_0x18, "modifiable": False},
        0x19: {"name": "Track Button 19", "behavior": 0x96, "color": 0x52, "function": web_0x19, "modifiable": False},
        0x1A: {"name": "Track Button 1A", "behavior": 0x96, "color": 0x52, "function": web_0x1A, "modifiable": False},
        0x1B: {"name": "Track Button 1B", "behavior": 0x96, "color": 0x21, "function": web_0x1B, "modifiable": True},
        0x1C: {"name": "Track Button 1C", "behavior": 0x96, "color": 0x21, "function": web_0x1C, "modifiable": True},
        0x1D: {"name": "Track Button 1D", "behavior": 0x96, "color": 0x21, "function": web_0x1D, "modifiable": True},
        0x1E: {"name": "Track Button 1E", "behavior": 0x96, "color": 0x21, "function": web_0x1E, "modifiable": True},
        0x1F: {"name": "Track Button 1F", "behavior": 0x96, "color": 0x21, "function": web_0x1F, "modifiable": True},
        #ROW 6
        0x10: {"name": "Track Button 10", "behavior": 0x96, "color": 0x21, "function": web_0x10, "modifiable": False},
        0x11: {"name": "Track Button 11", "behavior": 0x96, "color": 0x21, "function": web_0x11, "modifiable": False},
        0x12: {"name": "Track Button 12", "behavior": 0x96, "color": 0x21, "function": web_0x12, "modifiable": False},
        0x13: {"name": "Track Button 13", "behavior": 0x96, "color": 0x21, "function": web_0x13, "modifiable": True},
        0x14: {"name": "Track Button 14", "behavior": 0x96, "color": 0x21, "function": web_0x14, "modifiable": True},
        0x15: {"name": "Track Button 15", "behavior": 0x96, "color": 0x21, "function": web_0x15, "modifiable": True},
        0x16: {"name": "Track Button 16", "behavior": 0x96, "color": 0x21, "function": web_0x16, "modifiable": True},
        0x17: {"name": "Track Button 17", "behavior": 0x96, "color": 0x21, "function": web_0x17, "modifiable": True},
        #ROW 7
        0x08: {"name": "Track Button 08", "behavior": 0x96, "color": 0x43, "function": web_0x08, "modifiable": False},
        0x09: {"name": "Track Button 09", "behavior": 0x96, "color": 0x43, "function": web_0x09, "modifiable": False},
        0x0A: {"name": "Track Button 0A", "behavior": 0x96, "color": 0x43, "function": web_0x0A, "modifiable": False},
        0x0B: {"name": "Track Button 0B", "behavior": 0x96, "color": 0x21, "function": web_0x0B, "modifiable": True},
        0x0C: {"name": "Track Button 0C", "behavior": 0x96, "color": 0x21, "function": web_0x0C, "modifiable": True},
        0x0D: {"name": "Track Button 0D", "behavior": 0x96, "color": 0x21, "function": web_0x0D, "modifiable": True},
        0x0E: {"name": "Track Button 0E", "behavior": 0x96, "color": 0x21, "function": web_0x0E, "modifiable": True},
        0x0F: {"name": "Track Button 0F", "behavior": 0x96, "color": 0x21, "function": web_0x0F, "modifiable": True},
        #ROW 8
        0x00: {"name": "Track Button 00", "behavior": 0x96, "color": 0x16, "function": web_0x00, "modifiable": False},
        0x01: {"name": "Track Button 01", "behavior": 0x96, "color": 0x16, "function": web_0x01, "modifiable": False},
        0x02: {"name": "Track Button 02", "behavior": 0x96, "color": 0x16, "function": web_0x02, "modifiable": False},
        0x03: {"name": "Track Button 03", "behavior": 0x96, "color": 0x21, "function": web_0x03, "modifiable": True},
        0x04: {"name": "Track Button 04", "behavior": 0x96, "color": 0x21, "function": web_0x04, "modifiable": True},
        0x05: {"name": "Track Button 05", "behavior": 0x96, "color": 0x21, "function": web_0x05, "modifiable": True},
        0x06: {"name": "Track Button 06", "behavior": 0x96, "color": 0x21, "function": web_0x06, "modifiable": True},
        0x07: {"name": "Track Button 07", "behavior": 0x96, "color": 0x21, "function": web_0x07, "modifiable": True},
        #ROW BOTTOM
        0x64: {"name": "VOL 64", "behavior": 0x90, "color": 0x00, "function": web_0x64, "modifiable": False},
        0x65: {"name": "PAN 65", "behavior": 0x90, "color": 0x00, "function": web_0x65, "modifiable": False},
        0x66: {"name": "SEND 66", "behavior": 0x90, "color": 0x00, "function": web_0x66, "modifiable": False},
        0x67: {"name": "DEVICE 67", "behavior": 0x90, "color": 0x01, "function": web_0x67, "modifiable": False},
        0x68: {"name": "UP 68", "behavior": 0x90, "color": 0x01, "function": web_0x68, "modifiable": False},
        0x69: {"name": "DOWN 69", "behavior": 0x90, "color": 0x01, "function": web_0x69, "modifiable": False},
        0x6A: {"name": "LEFT 6A", "behavior": 0x90, "color": 0x01, "function": web_0x6A, "modifiable": False},
        0x6B: {"name": "RIGHT 6B", "behavior": 0x90, "color": 0x01, "function": web_0x6B, "modifiable": False},
        #RIGHT SIDE
        0x70: {"name": "CLIP STOP 70", "behavior": 0x90, "color": 0x01, "function": web_0x70, "modifiable": False},
        0x71: {"name": "SOLO 71", "behavior": 0x90, "color": 0x01, "function": web_0x71, "modifiable": False},
        0x72: {"name": "MUTE 72", "behavior": 0x90, "color": 0x01, "function": web_0x72, "modifiable": False},
        0x73: {"name": "REC 73", "behavior": 0x90, "color": 0x01, "function": web_0x73, "modifiable": False},
        0x74: {"name": "SELECT 74", "behavior": 0x90, "color": 0x01, "function": web_0x74, "modifiable": False},
        0x75: {"name": "DRUM 75", "behavior": 0x90, "color": 0x01, "function": web_0x75, "modifiable": False},
        0x76: {"name": "NOTE 76", "behavior": 0x90, "color": 0x00, "function": web_0x76, "modifiable": False},
        0x77: {"name": "STOP ALL 77", "behavior": 0x90, "color": 0x01, "function": web_0x77, "modifiable": False},
        0x7A: {"name": "SHIFT 7A", "behavior": 0x90, "color": 0x00, "function": web_0x7A, "modifiable": False}
    }
    return button_dict

def send_message(midiout, button_value, behavior, color):
    msg = [behavior, button_value, color]
    midiout.open_port(1)
    midiout.send_message(msg)
    midiout.close_port()

def listen_for_midi_messages(midiin, button_dict, midiout):
    last_button_note = None
    while True:
        msg = midiin.get_message()
        if msg:
            mido_msg = mido.parse(msg[0])
            print(mido_msg)
            if mido_msg.type == 'note_on':
                button_note = mido_msg.note
                button = button_dict.get(button_note)
                if button: 
                    if button['modifiable']:
                        if last_button_note is not None:
                            last_button = button_dict.get(last_button_note)
                            if last_button['modifiable']:
                                    last_button['behavior'] = 0x96
                                    send_message(midiout, last_button_note, last_button["behavior"], last_button["color"])
                            else:
                                last_button['color'] = 0x01
                                send_message(midiout, last_button_note, last_button["behavior"], last_button["color"]) 
                        button['behavior'] = 0x9F
                        send_message(midiout, button_note, button["behavior"], button["color"])
                        button['function']()
                        last_button_note = button_note
                    else:
                        if button_note in [0x67, 0x68, 0x69, 0x6A, 0x6B, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77]:
                            if last_button_note is not None:
                                last_button = button_dict.get(last_button_note)
                                if last_button['modifiable']:
                                    last_button['behavior'] = 0x96
                                    send_message(midiout, last_button_note, last_button["behavior"], last_button["color"])
                                    button['color'] = 0x02
                                    send_message(midiout, button_note, button["behavior"], button["color"])
                                    last_button_note = button_note
                                else:
                                    last_button['color'] = 0x01
                                    send_message(midiout, last_button_note, last_button["behavior"], last_button["color"])   
                                    button['color'] = 0x02
                                    send_message(midiout, button_note, button["behavior"], button["color"])
                                    last_button_note = button_note
                        button['function']() 
                else:
                    print("Unregistered button pressed: ", button_note)
            if mido_msg.type == 'control_change': #faders
                fader = mido_msg.control
                value = mido_msg.value
                if fader == 48:
                    web_0x48(fader,value)
                elif fader == 49:
                    web_0x49(fader,value)
                elif fader == 50:
                    web_0x50(fader,value)
                elif fader == 51:
                    web_0x51(fader,value)            
                elif fader == 52:
                    web_0x52(fader,value)
                elif fader == 53:
                    web_0x53(fader,value)
                elif fader == 54:
                    web_0x54(fader,value)
                elif fader == 55:
                    web_0x55(fader,value)
                elif fader == 56:
                    if value <= 1:
                        web_0x56(fader,value)
                    elif value >= 127:
                        web_0x56(fader,value)

def main():
    midiin, midiout = setup_midi_device()
    button_dict = map_notes_to_buttons()
    for button_value, button_data in button_dict.items():
        print(f"Turning on light for {button_data['name']}")
        send_message(midiout, button_value, button_data["behavior"], button_data["color"]) 
    IP = input("Enter the IP of the WLED controller: ")   
    open_browser(IP)
    listen_for_midi_messages(midiin, button_dict, midiout)

if __name__ == "__main__":
    main()
