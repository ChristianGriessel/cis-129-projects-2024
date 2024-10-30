# Christian Griessel
# Pig Latin program for CIS 129
# Take a sentence and turns it into pig latin

def main():
    sentence = pig_grabber()
    scramble = pig_it(sentence)
    scramble = capitalize_sentences(scramble)
    pig_printer(scramble)


def pig_grabber():
    #grabs setence from user
    sentence = input("What is your sentence?:\n\n")
    return sentence


def pig_it(text):
    #generates an empty list and a list with just the words.
    pig_list = []
    words = text.split()

    for word in words:
        #extracts chars
        alpha_part = ''.join(char for char in word if char.isalpha())
        #extracts punctuation
        punct_part = ''.join(char for char in word if not char.isalpha())

        #to conform with piglatin convention this checks if the word starts with a vowel or not. If it does then the structure doesn't change
        if alpha_part:
            if alpha_part[0].lower() in 'aeiou':
                pig_word = alpha_part + 'yay'
        #if the word doesn't start with a vowel this handles the logic behind chopping off the first char and adding it to the end
            else:
                pig_word = alpha_part[1:] + alpha_part.lower()[0] + 'ay'
        #if punctuation was present this adds it back onto the word
            pig_list.append(pig_word + punct_part)
        else:
            pig_list.append(word)

    return ' '.join(pig_list)

def capitalize_sentences(text):
    import re

    # this tells Python to scan my sentence and split it into a list wherever it sees punctiation followed by a space
    sentences = re.split('([.!?] *)', text)
    # This capitalizes everything then the list is put back together
    capitalized_sentences = ''.join([sentences[i].capitalize() for i in range(len(sentences))])
    return capitalized_sentences


def pig_printer(platin):
    print(platin)


if __name__ == "__main__":
    main()
