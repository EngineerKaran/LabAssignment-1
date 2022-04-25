print("Welcome!")
print("\nList items Deletion Program")
color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color = [x for (i,x) in enumerate(color) if i in (0,1,2,4,5)]
print("\n")
print(color)
#color = [x for (i,x) in enumerate(color) if i in (0,1,2,5)]
color[3] = "Purple"
color[4] = "Purple"
print(color)