groups = {"빅뱅" : ["GD", " 태양", "탑","대성", "승리"],
          "마마무": ["문별", "솔라","휘인","화사"]}

for i, j in groups.items():
    print(f"{i}의 멤버")
    for member in j:
        if member != "승리":
            print(member)

