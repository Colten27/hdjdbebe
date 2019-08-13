# import
from uagame import Window
from time import sleep

# create window
window = Window('Hacking game', 1000, 750)
window.set_font_color('cyan')
window.set_font_name('couriernew')
window.set_bg_color('yellow')
window.set_font_size(18)

# initialize variables
line_y = 0
string_height = window.get_font_height()

# display remaining attempts
window.draw_string ('3 attemps left', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

# display password list (similar to above, copy/paste for each password)
window.draw_string ('1password123', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('1passwords123', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('123456789', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('questionabke', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('erftgyhujkfjrughr', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('111222333', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('8319843712hfjkda3', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('JjfkdklJhfioOufLhw805H30Hfhadjkl7uLKHHUINghub', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('h4uuiuf89daui49080hfu890hf89fbheuieopqayf79qweuy8fhvuie80t4', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('ug89sdfj89fy892nuirfy89YYY9urfh894hugh89dan4y89ty', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('ifjoj4j8js8904', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string ('1111111111111111111111111', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height


# prompt user for password
guess = window.input_string('Guess the password > ', 0, line_y)

# clear window
window.clear()

# create outcome
if guess == 'This Password Is Impossible':
    window.draw_string('access granted', 0, 0)
    window.update()
else:
    window.draw_string('access denied', 0, 0)
    window.update()
sleep(2)

# clear window
window.clear()

# prompt for end
window.input_string('press enter to end the game', 0, 0)

# close window
window.close()

