users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
        print ("\n%s" %key)

        for index, value in enumerate(data,1):

            full_name = value['first_name'] + ' ' + value['last_name']
            full_name_upper = full_name.upper()
            name_count = len(full_name) -1
            print ("%d - %s - %s" %(index, full_name_upper, name_count))
