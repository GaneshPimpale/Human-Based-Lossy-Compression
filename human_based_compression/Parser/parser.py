import math
from ImageElement import Element


class Parser:

    # [method and letter equivalent)
    # crop (pixels)  =  P  (pixels)
    # crop (ratios)  =  K  (krop)
    # rotate         =  O  (oscillate)
    # resize         =  R  (resize)
    # flip           =  M  (mirror)
    # blur           =  S  (smudge)
    # translate      =  T  (translate)

    # key:
    # Crop(0, 0, .8, ,8) <-> k0.0.8.8
    #                         ^ ^ ^
    #             '.' separates parameter fields
    #
    # the value 45.45 is 45x45 with 45 and .45 as 2 separate hex values
    #

    # for Element:
    # img = Element(canvas, [pathname], [anchor], [displayBorder] <-> [pathname][anchor][]

    def __init__(self, canvas):  # commandString):

        self.commands = open(file="commands.txt", mode="r")
        self.editor = open(file="edit_commands.txt", mode="w+")

        self.allFunctions = [[], []]

        self.commands.seek(0)
        for command in self.parseBetween(self.commands.read(), ">", False):
            currString = self.parseBetween(command, '%', False)

            self.allFunctions[0].append(currString[0])

            print(self.allFunctions)
            self.allFunctions[1].append(self.parseBetween(currString[1], "pkstorm", True))

        print(self.allFunctions)

        #for i in range(10):
        #self.file.write("This is line %d\r\n" % (i + 1))
        self.commands.close()
        self.editor.close()


    @staticmethod
    def parseBetween(partialStrings, string, inclusive):
        partialStringsList = []
        startIndex = 0
        for endIndex in range(1, len(partialStrings)):
            #print(partialStrings[endIndex])
            #print(partialStrings[startIndex:endIndex])
            if partialStrings[endIndex] in string:
                partialStringsList.append(partialStrings[startIndex:endIndex])
                startIndex = endIndex + int(not inclusive)

        partialStringsList.append(partialStrings[startIndex:])
        return partialStringsList

    '''
        ENCODER: converts: translate(0.7690761, 0.834) => t495845a.342 '''
    @staticmethod
    def encode(partialString):

        idMap = {"cropPixel": 'p',
                 "cropRatio": 'k',
                 "oscillate": 'o',
                 "resize": 'r',
                 "mirror": 'm',
                 "smudge": 's',
                 "translate": 't'}

        funcID = idMap.get(partialString[:partialString.find('(')], "")

        parameters = []
        currentIndex = partialString.find('(') + 1
        while (partialString[currentIndex:-1]).find(", ") is not -1:
            parameters.append(str(partialString[currentIndex:(currentIndex + partialString[currentIndex:].find(", "))]))
            currentIndex += (partialString[currentIndex:-1].find(", ") + 2)

        parameters.append(str(partialString[currentIndex:-1]))
        print(parameters)
        for i in range(0, len(parameters)):

            if parameters[i].find('.') > 0:
                parameters[i] = f"{str(hex(int(parameters[i][:parameters[i].find('.')])))[2:]}x" \
                    f"{str(hex(int(parameters[i][(parameters[i].find('.') + 1):])))[2:]}"

            elif parameters[i].find('.') == 0:
                parameters[i] = f"x{str(hex(int(parameters[i][(parameters[i].find('.') + 1):])))[2:]}"

            else:
                parameters[i] = str(hex(int(parameters[i])))[2:]

        for i in range(0, len(parameters) - 1):
            funcID += f"{parameters[i]}."

        return funcID + parameters[-1]

    '''
    DECODER: converts: t495845a.342 => translate(0.7690761, 0.834)
    helper methods:
        extractParameters()
        createString()
        decodeMap() '''
    @staticmethod
    def decodeFunction(partialString):

        parameterList = commandParser.extractParameters(partialString[1:])
        return commandParser.decodeMap(partialString) + commandParser.createString(parameterList=parameterList)

    @staticmethod
    def decodeID(partialString):
        return


    '''
    Extracts parameters from proper syntax is @return list
    syntax: {methodName}(a, b, c, d) => [a, b, c, d] '''
    @staticmethod
    def extractParameters(partialString):

        if len(partialString) is 0:
            return []

        parameterList = []

        previous_parameter = 0

        for i in range(0, len(partialString)):
            if partialString[i] is '.':
                parameterList.append(partialString[previous_parameter:i])
                previous_parameter = i+1
        parameterList.append(partialString[previous_parameter:len(partialString)])

        for i in range(0, len(parameterList)):
            currParameter = parameterList[i]
            if 'x' in currParameter:
                intVal = float(int(currParameter[0:currParameter.find('x')], 16))
                decimalVal = float(int(currParameter[currParameter.find('x')+1:], 16))
                decimalVal /= (10 ** int(math.log10(decimalVal) + 1))
                parameterList[i] = intVal + decimalVal
            else:
                parameterList[i] = int(currParameter[:], 16)

        return parameterList

    '''
    combines all parameters into tuple-like string
    [a, b, c, d] => (a, b, c, d)
    '''
    @staticmethod
    def createString(parameterList, currentString=""):

        if len(parameterList) is 0:
            return f"({currentString[:-2]})"

        return commandParser.createString(parameterList[1:], currentString + f"{parameterList[0]}, ")

    '''
    from letterID returns fullMethod name
    e.g.: k => crop '''
    @staticmethod
    def decodeMap(partialString):
        idMap = {'p': "cropPixel",
                 'k': "cropRatio",
                 'o': "oscillate",
                 'r': "resize",
                 'm': "mirror",
                 's': "smudge",
                 't': "translate"}
        return idMap.get(partialString[0], "")

    '''                                                                  (hex values)
    executes function of class object such that commandFunc has syntax: k45.32x3.345
                                                                        ^             
                                                                    (letter id) '''
    @staticmethod
    def executeFunction(Object, commandFunc):
        return getattr(Object, commandParser.decodeMap(commandFunc), "")(*commandParser.extractParameters(commandFunc[1:]))

# END CLASS
