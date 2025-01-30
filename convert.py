import yaml
import random

VOWELS = ["a", "e", "i", "o", "u", 'y']

with open("char_substitutions.yaml", "r") as f:
    CHAR_DICT = yaml.safe_load(f)

def obfuscate_word(
        word,
        num_char_replace: int = 1,
        char_substitutions: dict = CHAR_DICT,
        vowel_prob: float = None,
        debug: bool = False
        ):
    '''
    Obfuscates a word from moderation, with modifyable probability of replacing vowels vs consonents. (Since in my exp, most people replaces vowels)

    :param word: The word to obfuscate.
    :param num_char_replace: Maximum number of characters to replace (1-3).
    :param vowel_prob: Probability of prioritizing vowels for replacement. Pass None to randomly choose.
    :param char_substitutions: Dictionary of character substitutions.

    :return: Obfuscated word.
    '''
    if not word:
        return ""
    
    char_list = list(word)
    num_replacements = random.randint(0, min(num_char_replace, len(word)))  # Replace 1, 2, or 3 characters
    
    # Get unique indices to replace
    if vowel_prob is None:
        replace_indices = random.sample(range(len(word)), min(num_replacements, len(word)))

    else:
        # Weighting vowels vs consonants
        # Separate vowels and consonants in the word
        vowel_indices = [i for i, char in enumerate(word) if char.lower() in VOWELS]
        consonant_indices = [i for i, char in enumerate(word) if char.lower() not in VOWELS]

        # Choose indices based on vowel probability weighting
        replace_indices = []
        for _ in range(num_replacements):
            if vowel_indices and (random.random() < vowel_prob or not consonant_indices):
                replace_indices.append(vowel_indices.pop(random.randint(0, len(vowel_indices) - 1)))
            elif consonant_indices:
                replace_indices.append(consonant_indices.pop(random.randint(0, len(consonant_indices) - 1)))

    if debug:
        print(num_replacements, replace_indices, char_list)
    
    for index in replace_indices:
        char = char_list[index].lower()
        if char in char_substitutions.keys():
            char_list[index] = random.choice(char_substitutions[char])  # Replace with a random substitute
    
    return "".join(char_list)

SPLITTERS = [' ', '-', '_', '.', ','] 
def split_word(word, 
               splitters = SPLITTERS,
               stretch_prob: float = 0.5,
               
               ):    
    if random.random() < stretch_prob:
        char_list = list(word)
        insert_char = random.choice(splitters)
        return insert_char.join(char_list)
    else:
        return word 

def repeat_char(word, 
                num_char_repeat: int = 1,
                repeat_max_freq: int = 3,
                repeat_prob: float = 0.5):
    if random.random() < repeat_prob:
        indices = random.sample(range(len(word)), min(num_char_repeat, len(word)))
        for index in indices:
            repeat_freq = random.randint(1, repeat_max_freq)
            word = word[:index] + word[index] * repeat_freq + word[index+1:]

    return word

def pluralize_word(word, plural_prob: float = 0.5):
    es_suffixes = tuple(['s', 'ch', 'sh', 'ss', 'x', 'z'])
    
    if random.random() < plural_prob:
        lower_word = word.lower() 
        if lower_word.endswith("y"):
            return word[:-1] + "ies"
        elif lower_word.endswith(es_suffixes):
            return word + "es"
        else:
            return word + "s" 
    else:
        return word   

if __name__ == "__main__":
    example_word = "pussy"

    #Replace chars
    obfuscated_word = obfuscate_word(
        example_word,
        num_char_replace=2,
        vowel_prob=None,
        debug= True
        )

    #Pluralize word
    obfuscated_word = pluralize_word(
        obfuscated_word,
        plural_prob=0.5
        )

    # Repeat chars
    obfuscated_word = repeat_char(
        obfuscated_word,
        num_char_repeat=1,
        repeat_max_freq=3,
        repeat_prob=0.5
        )    
    
    #Insert splitter
    obfuscated_word = split_word(
        obfuscated_word,
        stretch_prob=0.2
        )
    

    print(obfuscated_word)