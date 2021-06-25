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
    
    # Does 8 1's in PINA and PINB, PORTC should have count of 16, 0x10 in hex. 
    {'description': 'PINA: 0xFF, PINB: 0xFF => PORTC: 0x10',
    'steps': [ {'inputs': [('PINA',0xFF), ('PINB',0xFF)], 'iterations': 1 } ],
    'expected': [('PORTC',0x10)],
    },
    
    # Does 4 1's in PINA, 5 1's PINB, PORTC should have count of 9, 0x09 in hex. 
    {'description': 'PINA: 0x0F, PINB: 0x1F => PORTC: 0x09',
    'steps': [ {'inputs': [('PINA',0x0F), ('PINB',0x1F)], 'iterations': 1 } ],
    'expected': [('PORTC',0x09)],
    },

    # Does 0 1's in PINA, 0 1's PINB, PORTC should have count of 0, 0x00 in hex. 
    {'description': 'PINA: 0x00, PINB: 0x00 => PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x00), ('PINB',0x00)], 'iterations': 1 } ],
    'expected': [('PORTC',0x00)],
    },
        
    
]

# What variables to watch
watch = ['PORTC']

