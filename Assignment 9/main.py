# =============================================================================
# ENGR 1210 - Morse Optical Comms
# =============================================================================
# GOAL
#   Blink a Morse message on an LED - first on your LAPTOP, then, with the SAME
#   file and no changes, on a real Pico 2 in Wokwi. That "it just works on the
#   board too" moment is the whole idea of a HAL (Hardware Abstraction Layer).
#
# =============================================================================

import hal_pc as hw
#import hal_pico as hw  # uncomment this line to run on the real Pico 2
from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message


def blink_pattern(pattern):

    # pattern is one letter, like '...'
    for index in range(len(pattern)):
        symbol = pattern[index]

        if symbol == '.':
            on_ms = DOT_MS
        elif symbol == '-':
            on_ms = DASH_MS
        else:
            continue

        hw.set_led_timed(True, on_ms)

        if index < len(pattern) - 1:
            hw.set_led_timed(False, SYMBOL_GAP_MS)
    hw.set_led(False)



# The SAME loop runs in both worlds. You type a morse pattern; the HAL blinks it.
# On the laptop, "the LED" is the [LED] ON/OFF lines. On the board, it's the
# real onboard LED (type your message in the serial console / Wokwi's Serial
# Monitor). 
print("Board:", hw.board_info())
print("Type a message and watch it blink. Type 'quit' to stop.")

while True:
    message = input("\nType a message to blink (or 'quit'): ").strip()
    if message.lower() == "quit":
        break
    if message:
        patterns = encode_message(message)

        for index in range(len(patterns)):
            pattern = patterns[index]

            if pattern == ' ':
                hw.set_led_timed(False, WORD_GAP_MS)
            else:
                blink_pattern(pattern)

                if index < len(patterns) - 1:
                    if patterns[index + 1] != ' ':
                        hw.set_led_timed(False, LETTER_GAP_MS)

        print("...done")