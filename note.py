#/usr/bin/python
class NotesApplication (object):
  
  not_id = 0
  def __init__(self,author='Author'):
    NotesApplication.not_id +=1
    self.author=author
    self.my_saved_notes = []
    self.id = NotesApplication.not_id

#  def input_(self):
#      note_content = raw_input("any notes for today ?\n " )
#      self.create(note_content)
#     self.list()
 

  def create(self, note_content =''):
      note_content = raw_input("any notes for today ?  " )
      self.my_saved_notes.append(note_content)  
     

  def list(self):
      for item in self.my_saved_notes:
          print("note id: ",self.id)
          print item
          print("by Author : "+ self.author)
  
  #return the note 
  def get (self,note_id):
      return str(self.my_saved_notes[note_id])
  
# search 
  def search (self, search_text=''):
    search_text=raw_input('input search text...  ')
    for note in self.my_saved_notes:
       # for text in note:
        if search_text in note:
            print 'result for search %s ' % note
        else:
            print ' No match found for %s ' % search_text    


  def delete(self,note_id):
    self.my_saved_notes.pop(note_id)

  
  def edit(self,note_id,new_content):
    new_content = raw_input('new content ')
    my_saved_notes[note_id] = new_content
    self.list()
    print '/n'  
s= NotesApplication('qusai')
a= NotesApplication('sam')
c= NotesApplication('jaguar')


print s.create()
#print s.get(1)
print s.search()



          



               

          




      
