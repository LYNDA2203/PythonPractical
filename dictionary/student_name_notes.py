def topnotes(student):
    return{
        "name" : student["name"],
        "top_note": max(student["notes"])
    }


print(topnotes({"name":"john","notes":[3,5,4]})) 