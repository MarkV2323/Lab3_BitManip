/*	Author: Mark Vincent
 *  Partner(s) Name: NA
 *	Lab Section: A01
 *	Assignment: Lab #3  Exercise #4
 *	Exercise Description:
 *  We need to read an 8bit value from PINA and place the upper nibble into the
 *  lower nibble of PORTB (AP7-AP4 => BP3-BP0) and place the lower nibble into
 *  the upper nibble of PORTC (AP3-AP0 => CP7-CP4).
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    
    // Ports
    DDRA = 0x00; PORTA = 0xFF; // Configure PORTA as input
    DDRB = 0xFF; PORTB = 0x00; // Configure PORTB as output
    DDRC = 0xFF; PORTC = 0x00; // Configure PORTC as output
    
    // Vars
    unsigned char tmpA = 0x00;
    unsigned char tmpB = 0x00;
    unsigned char tmpC = 0x00;

    // Loop
    while (1) {
        
        // Read input
        tmpA = PINA & 0xFF;

        // Placing A7 - A4 into B3 - B0
        tmpB = tmpA >> 4;

        // Placing A3 - A0 into C7 - C4
        tmpC = tmpA << 4;

        // Write outputs
        PORTB = tmpB;
        PORTC = tmpC;

    }

    return 1;
}
