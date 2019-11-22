from aiy.board import Board, Led
from aiy.voice.audio import AudioFormat, play_wav, record_file

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
            play_wav('/home/pi/breatheresponsibly/speech.wav')


if __name__ == '__main__':
    print("Starting")
    main()
