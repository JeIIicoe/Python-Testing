from Bird import *
print('\nClass Instances Of:\n', Bird.__doc__)

polly = Bird('Squawk squawk!')
print('\nNumber of Birds:', polly.count)
print('Polly Says:', polly.talk())

barry = Bird('Tweet tweet!')
print('\nNumber of Birds:', barry.count)
print('Barry says:', barry.talk())