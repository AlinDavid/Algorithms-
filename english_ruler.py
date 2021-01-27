'''
The intuition behind recursion can be used to draw the marking of a typical English Ruler. 
An English Ruler is a long, flat piece of plastic or metal with straight edges, usually 
marked in inches or centimeters. It is a complex example of the application of recursion when 
compared to the factorial operation above.
'''



def draw_line(tick_length, tick_label=" "):

    line = "-" * tick_length

    if tick_label:
        line += " " + tick_label
        print(line)


def draw_interval(center_length):

    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):

    draw_line(major_length, "0")

    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
