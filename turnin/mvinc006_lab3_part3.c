/*	Author: Mark Vincent
 *  Partner(s) Name: NA
 *	Lab Section: A01
 *	Assignment: Lab #3  Exercise #3
 *	Exercise Description: 
 *  
 *  Designing a fuel level sensor, PA3 - PA0 holds a
 *	value between 0 and 15 which will in turn, indicate which values of PC5 -
 *	PC0 to be 1. PC6 contains a low fuel light, which is 1 if 4 or less values
 *	of PC5 - PC0 are 1. 
 *
 *  We also need to add in support for PA4 (key in), PA5 (driver seated) and 
 *  PA6 (driver seatbelt fastened). PC7 should be 1 if the key is in, the
 *  driver is seated, but the seatbelt is not fastened. Or in other words, 
 *  PC7 = PA4 && PA5 && !PA7
 *
 *  Fuel Level 1 or 2   => PC5 is 1
 *  Fuel Level 3 or 4   => PC5 - PC4 is 1
 *  Fuel Level 5 or 6   => PC5 - PC3 is 1
 *  Fuel Level 7 to 9   => PC5 - PC2 is 1
 *  Fuel Level 10 to 12 => PC5 - PC1 is 1
 *  Fuel Level 13 to 15 => PC5 - PC0 is 1
 *
 *  Low Fuel Level at 7 to 9 => PC6 is 1
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
    DDRC = 0xFF; PORTC = 0x00; // Configure PORTC as output

    // Vars
    unsigned char tmpA = 0x00;
    unsigned char tmpC = 0x00;
    
    unsigned char lightLevel = 0x00;

    // Loop
    while (1) {
        
        // read input
        tmpA = PINA & 0xFF;
        
        // gather lightLevel
        lightLevel = tmpA & 0x0F;

        // begin setting light levels
        if (lightLevel >= 13) {
            // 1 on pins PC5 - PC0
            tmpC = 0x3F;

        } else if (lightLevel >= 10) {
            // 1 on pins PC4 - PC0
            tmpC = 0x1F;

        } else if (lightLevel >= 7)  {
            // 1 on pins PC3 - PC0 and PC6
            tmpC = 0x4F;
            
        } else if (lightLevel >= 5)  {
            // 1 on pins PC2 - PC0 and PC6
            tmpC = 0x47;

        } else if (lightLevel >= 3)  {
            // 1 on pins PC1 - PC0 and PC6
            tmpC = 0x43;

        } else if (lightLevel > 0) {
            // 1 on pins PC0 and PC6
            tmpC = 0x41;

        } else {
            // fuel is empty, no lights except fuel light empty
            tmpC = 0x40;

        }
        
        // checks for seatbelt light
        // PC7 = PA4 && PA5 && !PA6
        if ((tmpA & 0x10) && (tmpA & 0x20) && !(tmpA & 0x40)) {
            // Writes a 1 to PC7 in tmpC.
            tmpC = tmpC | 0x80;
        }

        // Writes to PORTC
        PORTC = tmpC;

        // Reset tmpC
        tmpC = 0x00;
    }

    return 1;
}
