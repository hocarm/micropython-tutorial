#include <SPI.h>
char buf;
volatile byte pos;
volatile boolean isAvailable;
void setup()
{
    Serial.begin(9600); // for debugging
    // SPI slave mode
    SPCR |= bit(SPE);
    SPCR |= _BV(SPIE);
    isAvailable = false;
    pos = 0;
    pinMode(MISO, OUTPUT);
    SPI.attachInterrupt();
}
ISR(SPI_STC_vect)
{
    byte c = SPDR;
    if (c > 64 && c < 91)
    {
        buf = c;
        isAvailable = true;
    }
}
void loop()
{
    if (isAvailable)
    {
        Serial.println(buf);
        isAvailable = false;
    }
}