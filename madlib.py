story = '''
The girl was walking to the {}
when she heard a loud {} behind her.
"{}" she exclaimed, and turned around.
Before her stood a tall {}.
The {} waved its {} in greeting.
It then turned around and {} into the beyond.
'''

def main():
    place = input('Enter a place, such as a grocery store or the moon:')
    noise = input('Enter a type of noise, such as a bang or growl:')
    shout = input('Enter something you might say when you are surprised:')
    animal = input('Enter a type of animal, such as a dog or bird:')
    bodypart = input('Enter a body part, such as a finger, wing, or toe:')
    past_verb = input('Enter a verb in past tense:')

    mad_lib = story.format (place,
                            noise,
                            shout,
                            animal,
                            animal,
                            bodypart,
                            past_verb)
    print(mad_lib)

main()
