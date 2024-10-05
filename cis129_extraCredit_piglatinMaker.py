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
    #full disclosure, I couldn't for the life of me get this to work so I got a friend who is a professional programer to help me with it lol
    #If this seems like the most advanced thing in the program that's because I had help writing it
    import re

    #this tells Python to scan my sentence and split it into a list wherever it sees punctiation followed by a space
    sentences = re.split('([.!?] *)', text)
    #This checks if we are at an even or odd indecies in the sentence. We know all letters will be even and all punctuation will be odd
    #If it is even we capitalize the sentence. If it isn't we just add it straight back into the list because we know it's punctuation
    capitalized_sentences = ''.join([sentences[i].capitalize() if i % 2 == 0 else sentences[i] for i in range(len(sentences))])
    return capitalized_sentences


def pig_printer(platin):
    print(platin)


if __name__ == "__main__":
    main()
