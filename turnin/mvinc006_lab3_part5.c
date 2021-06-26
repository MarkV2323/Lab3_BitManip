/*	Author: Mark Vincent
 *  Partner(s) Name: NA
 *	Lab Section: A01
 *	Assignment: Lab #3  Exercise #5
 *	Exercise Description:
 *
 *  We are getting input from PORTD and Pin B0 from a car seat weight sensor.
 *  If the weight is >= 70lbs, the airbag should be 1 on Pin B1.
 *  If the weight is >= 5lbs but <= 70lbs, the airbag off should be 1 on PinB2
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    
    // PORTS
    DDRB = 0x06; PORTB = 0xF9; // Pins B1 and B2 are OUTPUT, rest is INPUT
    DDRD = 0x00; PORTD = 0xFF; // CONFIGURE PORTD as INPUT

    // VARS
    unsigned char tmpBin = 0x00;
    unsigned char tmpBout = 0x00;
    unsigned char tmpD = 0x00;
    
    unsigned short totalWeight = 0x0000;

    while (1) {
    
    // Reads input
    tmpBin = PINB & 0x09;
    tmpD   = PIND & 0xFF;

    // Add entire input D onto totalWeight and shift left 1.
    totalWeight = tmpD;
    totalWeight = totalWeight << 1;

    // Adds extra 1 bit from tmpB onto totalWeight.
    totalWeight = totalWeight + (tmpBin & 0x01);
    
    // Decides if what lights need to go on.
    if (totalWeight >= 70) {
        // B1 needs to go to 1
        tmpBout = (tmpBin & 0x01) | 0x02;
    } else if (totalWeight >= 5) {
        // B2 needs to go to 1
        tmpBout = (tmpBin & 0x01) | 0x04;
    } else {
        // ignore if less than 5 lbs.
    }

    // Writes output
    PORTB = tmpBout;
    // reset tmpB
    tmpBout = 0x00;

    }

    return 1;
}
