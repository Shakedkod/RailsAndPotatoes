string = """
        #level -> {i}#
        if self.buttons.l_{i}_unlocked and self.buttons.l_{i}_completed:
            data[{i}]["data"] = 2
        elif self.buttons.l_{i}_unlocked:
            data[{i}]["data"] = 1
        else:
            data[{i}]["data"] = 0
            """

for x in range(1, 55):
    print (string.format(i = x))