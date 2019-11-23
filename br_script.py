from aiy.board import Board, Led
from aiy.voice.audio import AudioFormat, play_wav, record_file
import random 
  
def main():
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    with Board() as board:
        while True:
            board.button.wait_for_press()
            print('ON')
            board.led.state = Led.ON
            board.button.wait_for_release()
            print('OFF')
            board.led.state = Led.OFF
            # Generates a random number between 
            # a given positive range 
            r1 = random.randint(1, 6) 
            print("Random number between 1 and 6 is % s" % (r1)) 
            wav = "/home/pi/breatheresponsibly/%s.wav" % r1
            print(wav)
            play_wav(wav)


if __name__ == '__main__':
    print("Starting")
    main()
