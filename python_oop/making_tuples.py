def making_tuples(my_dict):
    return my_dict.items()

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
print(list(making_tuples(my_dict)))