from abc_exercise_randomizer.exercise_generator import ExerciseGenerator
from examples.example_input import *

if __name__ == "__main__":
    generator = ExerciseGenerator(note_distribution, length_distribution, tie_probability, syncopated, bar_length,
                                  number_of_bars)
    print(generator.generate_exercise())
