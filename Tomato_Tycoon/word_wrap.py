def word_wrap(surf,font,color,string,rect):
    "For word wrapping helping with description"
    word_list = string.split(" ")
    cur_line = ""
    broken_lines = []
    for word in word_list:
        if font.size(cur_line + word)[0] > rect[2]:
            broken_lines.append(cur_line)
            cur_line = word + " "
        else:
            cur_line += word + " "
    if len(cur_line) > 0:
        broken_lines.append(cur_line)
    y = rect[1]
    for line in broken_lines:
        font_surf = font.render(line,1,color)
        y += font.size(cur_line)[1]
        surf.blit(font_surf,(rect[0],y))