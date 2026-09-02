import emoji
def main():
        emo = input("Input: ")
        print("Output:" , emoji.emojize(emo,language = 'alias'))
main()