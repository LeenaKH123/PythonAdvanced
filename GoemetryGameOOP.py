class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print(self)

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
            and lowleft[1] < self.y < upright[1]:
            print("Im in the rectangle")
            return True
        else:
            print("Im not in the rectangle")
            return False

# class Point:
#     def __init__(self, x, y):
#         this_object.x = x
#         this_object.y = y
#         print(self)
        

point1 = Point(3, 4)
point2 = Point(6, 7)
# type(point1)