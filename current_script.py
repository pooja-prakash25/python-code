import other_script
print("")
print("****inside current script.py*****")
print("__name__ ",__name__)


'''You will now realize that previously when we ran other_script.py, 
it gave us the value for __name__ as __main__. But now since we ran
 it as an import in current_script.py, the value of __name__ suddenly 
 changed to the name of the imported script which is other_script.'''