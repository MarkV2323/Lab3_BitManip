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

    # FL = 11, PC4-PC0 are 1, hex is 0x1F
    {'description': 'PINA: 0x0B => PORTC: 0x1F',
    'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 3 } ],
    'expected': [('PORTC',0x1F)],
    },

    # FL = 7, PC3-PC0 are 1, PC6 is 1, hex is 0x4F
    {'description': 'PINA: 0x07 => PORTC: 0x4F',
    'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 3 } ],
    'expected': [('PORTC',0x4F)],
    },

    # FL = 5, PC2-PC0 are 1, PC6 is 1, hex is 0x47
    {'description': 'PINA: 0x05 => PORTC: 0x47',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 3 } ],
    'expected': [('PORTC',0x47)],
    },

    # FL = 4, PC1-PC0 are 1, hex is 0x1F
    {'description': 'PINA: 0x03 => PORTC: 0x43',
    'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 3 } ],
    'expected': [('PORTC',0x43)],
    },

    # FL = 1, PC0 is 1, PC6 is 1, hex is 0x41
    {'description': 'PINA: 0x01 => PORTC: 0x41',
    'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 3 } ],
    'expected': [('PORTC',0x41)],
    },

    # FL = 0, none are 1, PC6 is 1, hex is 0x40
    {'description': 'PINA: 0x00 => PORTC: 0x40',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 3 } ],
    'expected': [('PORTC',0x40)],
    },
      
      
    ]

# What variables to watch
watch = ['PORTA', 'PORTC', 'main::tmpA', 'main::lightLevel']

