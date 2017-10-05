import re
import sys

class Parser:
    def __init__(self, input):
        self.input_filepath = input

    def analyse(self, pat):
        pattern = re.compile(pat)
        output_filepath = self.input_filepath[:-4]+'_v2'+self.input_filepath[-4:]
        print(output_filepath)
        output = open("output.txt", "w")
        with open(self.input_filepath) as file:
            for line in file.readlines():
                m=pattern.search(line)
                if m is not None:
                    finalString = int(m.group())+5
                    line = pattern.sub(str(finalString), line)
                output.write(line)



if __name__ == "__main__":

    def main(input_filepath):
        input_filepath = "This.m2s"
        parser = Parser(input_filepath)
        parser.analyse('\d\d+')

    main(sys.argv[1])
