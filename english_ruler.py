#!/usr/bin/env python3

def draw_line(tick_length, tick_label = ''):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a cental tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

if __name__ == "__main__":
    inches = int(input("Enter amount of inches: "))
    length = int(input("Length of major tick: "))
    draw_ruler(inches, length)
    
