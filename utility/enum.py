"basic enumerated type"

def enum(**enums):
    return type('Enum', (), enums)


# usage
#
# FRUIT = enum(NONE=0, APPLE=1, ORANGE=2, JACKFRUIT="gross")
#
# print FRUIT.APPLE == FRUIT.JACKFRUIT



