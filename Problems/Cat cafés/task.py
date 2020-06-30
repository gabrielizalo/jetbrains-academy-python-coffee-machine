cat_cafe = input()
chosen_cafe_name = ''
chosen_cafe_cats = 0

while cat_cafe != 'MEOW':
    cat_cafe_new = cat_cafe.split()
    if int(cat_cafe_new[1]) > chosen_cafe_cats:
        chosen_cafe_name = cat_cafe_new[0]
        chosen_cafe_cats = int(cat_cafe_new[1])
    cat_cafe = input()

print(chosen_cafe_name)
