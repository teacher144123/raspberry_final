import spi


if __name__ == '__main__':
    register = spi.SPI(clk=22, cs=27, mosi=17, miso=None, verbose=True)

    ### Disable code B decode mode on all digits
    max7219.put(int("100100000000",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    ### Set intensity low
    max7219.put(int("101000000000",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    ### Enable all digits in scan-limit register
    max7219.put(int("101100000111",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    ### Disable test mode
    max7219.put(int("111100000000",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    ### Disable shutdown mode
    max7219.put(int("110000000001",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    input("Press any key to shut down.")