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
    
    # FL = 15, PC5-PC0 are 1, hex is 0x3F
    {'description': 'PINA: 0x0F => PORTC: 0x3F',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 3 } ],
    'expected': [('PORTC',0x3F)],
    },

    # FL = 11, PC5-PC1 are 1, hex is 0x3E
    {'description': 'PINA: 0x0B => PORTC: 0x1F',
    'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 3 } ],
    'expected': [('PORTC',0x3E)],
    },

    # FL = 7, PC5-PC2 are 1, hex is 0x3C
    {'description': 'PINA: 0x07 => PORTC: 0x3C',
    'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 3 } ],
    'expected': [('PORTC',0x3C)],
    },

    # FL = 5, PC5-PC3 are 1, hex is 0x38
    {'description': 'PINA: 0x05 => PORTC: 0x38',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 3 } ],
    'expected': [('PORTC',0x38)],
    },

    # FL = 4, PC5-PC4 are 1, PC6 is 1 hex is 0x70
    {'description': 'PINA: 0x03 => PORTC: 0x70',
    'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 3 } ],
    'expected': [('PORTC',0x70)],
    },

    # FL = 1, PC5 is 1, PC6 is 1, hex is 0x60
    {'description': 'PINA: 0x01 => PORTC: 0x60',
    'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 3 } ],
    'expected': [('PORTC',0x60)],
    },

    # FL = 0, none are 1, PC6 is 1, hex is 0x40
    {'description': 'PINA: 0x00 => PORTC: 0x40',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 3 } ],
    'expected': [('PORTC',0x40)],
    },
    
     # Checking seatbelt light
     # No seatbelt light in this case
     # FL = 11, PA6-PA4 are all 1, PC5-PC1 are 1, PC hex is 0x3E
    {'description': 'PINA: 0x7B => PORTC: 0x3E',
    'steps': [ {'inputs': [('PINA',0x7B)], 'iterations': 3 } ],
    'expected': [('PORTC',0x3E)],
    },
    
    # Checking seatbelt light
    # Seatbelt light PC7 should be 1.
    # FL = 7, PA6 is 0, PA5-PA4 are 1, PC5-PC2 are 1, PC7 is 1, hex is 0xBC
    {'description': 'PINA: 0x37 => PORTC: 0xBC',
    'steps': [ {'inputs': [('PINA',0x37)], 'iterations': 3 } ],
    'expected': [('PORTC',0xBC)],
    },

 
    ]

# What variables to watch
watch = ['PORTA', 'PORTC', 'main::tmpA', 'main::lightLevel', 'main::tmpC']
