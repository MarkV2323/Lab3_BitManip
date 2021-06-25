/*	Author: Mark Vincent
 *  Partner(s) Name: NA
 *	Lab Section: A01
 *	Assignment: Lab #3  Exercise #1
 *	Exercise Description:
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
    DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
	DDRB = 0x00; PORTB = 0xFF; // Configure port B's 8 pins as inputs
   	DDRC = 0xFF; PORTC = 0x00; // Configure port C's 8 pins as outputs
    
    // Vars
    unsigned char tmpA  = 0x00; // Stores info from A
    unsigned char tmpB  = 0x00; // Stores info from B
    //unsigned char tmpC  = 0x00; // Stores info to write to C

    unsigned char count = 0x00; // Stores number of counted 1s from A and B

    // Loop
    while (1) {
        // reads inputs
        tmpA = PINA & 0xFF;
        tmpB = PINB & 0xFF;
        
        // begins counting from A.
        for (int i = 0; i < 8; i++) {
            // Checks A0
            if ((tmpA & 0x01) == 0x01) {
                count = count + 1;
            }
            // Shift tmpA by 1 to the right
            tmpA = tmpA >> 1;
        }

        // begins counting from B.
        for (int i = 0; i < 8; i++) {
            // Checks B0
            if ((tmpB & 0x01) == 0x01) {
                count = count + 1;
            }
            // Shift tmpB by 1 to the right
            tmpB = tmpB >> 1;
        }
        
        // Writes count to PORTC
        PORTC = count;

        // resets count
        count = 0x00;
    }

    return 1;
}
