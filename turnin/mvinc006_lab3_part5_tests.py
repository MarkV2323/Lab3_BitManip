# Array of tests to run (in order)

# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test

# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).

# Our Tests (default for now)
tests = [ 
    
    # Total input on pins is 0 0001 1111 = 31. <70 >5 so B2 will be 1, B1 is 0.
    # output pin should be PINB = 0000 0101 or 0x05.
    {'description': 'PINB: 0x01, PIND: 0x0F => PINB: 0x04',
    'steps': [ {'inputs': [('PINB',0x01), ('PIND',0x0F)], 'iterations': 3 } ],
    'expected': [('PORTB',0x04)],
    },
   
    # Total input on pins is 1 1111 0011 = 249. >70 >5 so B1 will be 1, B2 is 0.
    # output pin should be PINB = 0000 0011 or 0x03.
    {'description': 'PINB: 0x01, PIND: 0xF9 => PINB: 0x02',
    'steps': [ {'inputs': [('PINB',0x01), ('PIND',0xF9)], 'iterations': 3 } ],
    'expected': [('PORTB',0x02)],
    },
    
    # Total input on pins is 0 0000 0010 = 0. <70 <5 so B2 will be 0, B1 is 0.
    # output pin should be PINB = 0000 0000 or 0x00.
    {'description': 'PINB: 0x00, PIND: 0x01 => PINB: 0x00',
    'steps': [ {'inputs': [('PINB',0x00), ('PIND',0x01)], 'iterations': 3 } ],
    'expected': [('PORTB',0x00)],
    },
    
    # Total input on pins is 0 0100 0101 = 69. <70 >5 so B1 will be 0, B2 is 1.
    # output pin should be PINB = 0000 0011 or 0x03.
    {'description': 'PINB: 0x01, PIND: 0x22 => PINB: 0x04',
    'steps': [ {'inputs': [('PINB',0x01), ('PIND',0x22)], 'iterations': 3 } ],
    'expected': [('PORTB',0x04)],
    },
    
    # Total input on pins is 0 0000 0011 = 3. <70 <5 so B2 will be 0, B1 is 0.
    # output pin should be PINB = 0000 0000 or 0x00.
    {'description': 'PINB: 0x01, PIND: 0x02 => PINB: 0x00',
    'steps': [ {'inputs': [('PINB',0x01), ('PIND',0x02)], 'iterations': 3 } ],
    'expected': [('PORTB',0x00)],
    },


    ]

# What variables to watch
watch = ['PORTB', 'PORTD', 'main::tmpBin', 'main::tmpD', 'main::totalWeight']

