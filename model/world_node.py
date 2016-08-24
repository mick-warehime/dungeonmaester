def enum(**enums):
    return type('Enum', (), enums)

NODE_CLASSIFIERS = enum(NONE = 0, NPC = 1, CITY = 2)

class WorldNode():

    def __init__(self, node_classifier = NODE_CLASSIFIERS.NONE):
        self.classifier = node_classifier

    def get_classifier(self):
        return self.classifier